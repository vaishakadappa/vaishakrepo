import os
import pandas as pd
import logging
from configparser import ConfigParser
from Updated_rows import find_updated_rows
from attribut_comparison import compare_all_headers
from enodecategory_comparison import compare_enodecategory


def setup_logging(log_file_path):
    """
    Sets up logging for the script.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )


def convert_to_parquet(input_file, parquet_file, chunk_size=10000):
    """
    Processes an input file (Excel/CSV) in chunks and writes to Parquet format.

    Parameters:
        input_file (str): Path to the input file.
        parquet_file (str): Path to the output Parquet file.
        chunk_size (int): Number of rows per chunk to process.

    Returns:
        str: Path to the output Parquet file.
    """
    logging.info(f"Starting chunk-wise processing of {input_file}.")
    print(f"Starting chunk-wise processing of {input_file}.")

    rows_processed = 0
    chunks = []

    if input_file.endswith('.xlsx') or input_file.endswith('.xls'):
        full_df = pd.read_excel(input_file, dtype=str)  # Read entire Excel file
        total_rows = len(full_df)
        chunks = [
            full_df.iloc[i:i + chunk_size]
            for i in range(0, total_rows, chunk_size)
        ]
    elif input_file.endswith('.csv'):
        reader = pd.read_csv(input_file, dtype=str, chunksize=chunk_size, encoding='utf-8')
        for chunk in reader:
            chunks.append(chunk)
    else:
        raise ValueError("Unsupported file format. Only Excel and CSV are supported.")

    for chunk_index, chunk in enumerate(chunks):
        rows_processed += len(chunk)
        logging.info(f"Processing chunk {chunk_index + 1}: {len(chunk)} rows.")
        print(f"Processing chunk {chunk_index + 1}: {len(chunk)} rows.")

    logging.info("Combining all chunks into a single DataFrame.")
    print("Combining all chunks into a single DataFrame.")
    full_df = pd.concat(chunks, ignore_index=True)

    logging.info(f"Writing final DataFrame to Parquet: {parquet_file}")
    print(f"Writing final DataFrame to Parquet: {parquet_file}")
    full_df.to_parquet(parquet_file, index=False, engine='pyarrow')

    logging.info(f"Completed processing of {input_file}. Total rows processed: {rows_processed}.")
    print(f"Chunk-wise processing completed: {rows_processed} rows processed.")
    return parquet_file


def compare_files_in_chunks(df1_path, df2_path, parquet_report_file, part_reference_column, attribute_reference_column,
                            category_comparison_columns, chunk_size=10000):
    """
    Compares two files in chunks and writes the comparison results into a Parquet file.
    """
    logging.info("Starting comparison of Parquet files in chunks.")
    print("Starting comparison of Parquet files in chunks.")

    df1 = pd.read_parquet(df1_path)
    df1[part_reference_column] = df1[part_reference_column].astype(str).str.strip()
    df1.set_index(part_reference_column, inplace=True)

    df2_full = pd.read_parquet(df2_path)
    total_rows = len(df2_full)
    chunks = [
        df2_full.iloc[i:i + chunk_size]
        for i in range(0, total_rows, chunk_size)
    ]

    new_rows = []
    deleted_rows = df1.copy()
    updated_rows = []

    for chunk_index, df2_chunk in enumerate(chunks):
        logging.info(f"Processing chunk {chunk_index + 1}")
        print(f"Processing chunk {chunk_index + 1}")

        df2_chunk[part_reference_column] = df2_chunk[part_reference_column].astype(str).str.strip()
        df2_chunk.set_index(part_reference_column, inplace=True)

        # Identify deleted rows
        deleted_rows = deleted_rows[~deleted_rows.index.isin(df2_chunk.index)]

        # Identify new rows
        for tcpn in df2_chunk.index.difference(df1.index):
            new_row = df2_chunk.loc[tcpn].to_dict()
            new_row[part_reference_column] = tcpn
            new_rows.append(new_row)

        # Identify updated rows
        updated_rows += find_updated_rows(df1, df2_chunk)

    # Perform attribute and category comparisons
    attribute_comparison_results = compare_all_headers(df1, df2_full, reference_column=attribute_reference_column)
    enode_results = compare_enodecategory(df1, df2_full, reference_column=category_comparison_columns)

    # Create a dictionary to store all DataFrames
    report_data = {}

    # Add summary data
    summary_df = pd.DataFrame({
        'Description': [
            '# Parts data updated',
            '# New Parts',
            '# Deleted Parts',
            'Attribute_Details_No_Change',
            'Attribute_Details_New',
            'Attribute_Details_Deleted',
            'Attribute_Details_updated',
            'Category_Details_No_Change',
            'Category_Details_New',
            'Category_Details_updated',
            'Category_Details_Deleted'
        ],
        'Count': [
            len(updated_rows),
            len(new_rows),
            len(deleted_rows),
            len(attribute_comparison_results[attribute_comparison_results['Status'] == 'No Change']),
            len(attribute_comparison_results[attribute_comparison_results['Status'] == 'New']),
            len(attribute_comparison_results[attribute_comparison_results['Status'] == 'Deleted']),
            len(attribute_comparison_results[attribute_comparison_results['Status'] == 'Updated']),
            len(enode_results[enode_results['Status'] == 'No_Change']),
            len(enode_results[enode_results['Status'] == 'New']),
            len(enode_results[enode_results['Status'] == 'Updated']),
            len(enode_results[enode_results['Status'] == 'Deleted'])
        ]
    })
    summary_df = pd.DataFrame(summary_df)

    # Combine all results into a single DataFrame
    combined_results = pd.DataFrame()

    # Add summary results
    combined_results = pd.concat([combined_results, summary_df.assign(Type='Summary')])

    # Add updated rows
    if not updated_rows.empty:
        updated_rows_df = updated_rows.assign(Type='Updated Rows')
        combined_results = pd.concat([combined_results, updated_rows_df])

    # Add new rows
    if new_rows:
        new_df = pd.DataFrame(new_rows)
        new_df = reorder_columns(new_df, part_reference_column)  # Ensure TCPN is the first column
        new_df = new_df.assign(Type='New Rows')
        combined_results = pd.concat([combined_results, new_df])

    # Add deleted rows
    if not deleted_rows.empty:
        deleted_df = deleted_rows.assign(Type='Deleted Rows')
        combined_results = pd.concat([combined_results, deleted_df])

    # Add attribute comparison results
    if not attribute_comparison_results.empty:
        attribute_comparison_results = attribute_comparison_results.assign(Type='Attribute Details')
        combined_results = pd.concat([combined_results, attribute_comparison_results])

    # Add enode results
    if not enode_results.empty:
        enode_results = enode_results.assign(Type='Category Details')
        combined_results = pd.concat([combined_results, enode_results])

    # Write combined results to a single CSV file
    combined_results.to_csv(excel_report_file, index=False)

    print(f"Report generated in a single CSV file at: {excel_report_file}/combined_report.csv")


def reorder_columns(df, first_column):
    """
    Reorders the columns of the DataFrame to place `first_column` at the start.
    """
    columns = [first_column] + [col for col in df.columns if col != first_column]
    return df[columns]


def format_rows(writer, sheet_name, color):
    workbook = writer.book
    worksheet = writer.sheets[sheet_name]
    format_color = workbook.add_format({'font_color': color})
    worksheet.set_column('A:Z', 20)  # Adjust column width as necessary
    worksheet.set_row(0, None, workbook.add_format({'bold': True}))  # Bold header
    for row_num in range(1, worksheet.dim_rowmax + 1):  # Skip header
        worksheet.set_row(row_num, None, format_color)


def convert_parquet_to_excel(parquet_report_file, excel_report_file):
    """
    Converts the Parquet report to an Excel file.
    """
    logging.info(f"Converting Parquet report to Excel: {excel_report_file}")
    print(f"Converting Parquet report to Excel: {excel_report_file}")

    result_df = pd.read_parquet(parquet_report_file)

    with pd.ExcelWriter(excel_report_file, engine='xlsxwriter') as writer:
        for sheet_name, df in result_df.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    logging.info(f"Excel report generated: {excel_report_file}")
    print(f"Excel report generated: {excel_report_file}")


if __name__ == "__main__":
    config_file = r"C:\\Accuris_Kapow\\TE_COMPARISON REPORT\\Config.ini"

    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Configuration file not found: {config_file}")

    config = ConfigParser()
    config.read(config_file)

    log_filepath = config['Paths']['log_filepath']
    input_file_1 = config['Paths']['input_file_1']
    input_file_2 = config['Paths']['input_file_2']
    parquet_report_file = config['Paths']['parquet_report_file']
    excel_report_file = config['Paths']['excel_report_file']
    reference_column = config['Settings']['reference_column']
    attribute_reference_column = config['Settings']['attribute_reference_column']
    category_comparison_columns = config['Settings']['category_comparison_columns']

    setup_logging(log_filepath)

    parquet_file_1 = convert_to_parquet(input_file_1, "file1.parquet")
    parquet_file_2 = convert_to_parquet(input_file_2, "file2.parquet")

    compare_files_in_chunks(
        parquet_file_1,
        parquet_file_2,
        parquet_report_file,
        reference_column,
        attribute_reference_column,
        category_comparison_columns
    )

    convert_parquet_to_excel(parquet_report_file, excel_report_file)
