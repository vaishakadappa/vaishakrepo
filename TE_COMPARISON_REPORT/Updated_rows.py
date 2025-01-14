import pandas as pd


def find_updated_rows(df1, df2, category_column="endNodeCategory"):
    """
    Finds updated rows between two DataFrames and returns them in a transposed format.

    Args:
        df1 (DataFrame): Previous DataFrame (with 'TCPN' as index).
        df2 (DataFrame): Current DataFrame (with 'TCPN' as index).
        category_column (str): The column representing the category (e.g., "Enodecategory").

    Returns:
        DataFrame: Transposed DataFrame with updated rows in the format:
                   'Part Number', 'Previous', 'Current', 'Attribute', 'From-Data', 'To-Data'.
    """
    changes = []

    for tcpn in df2.index:
        if tcpn in df1.index:
            # Compare each column (attribute) for the current Part Number
            for column in df1.columns:
                if column in df2.columns:
                    # Values in the previous and current files
                    value1 = str(df1.at[tcpn, column]).strip() if pd.notna(df1.at[tcpn, column]) else ""
                    value2 = str(df2.at[tcpn, column]).strip() if pd.notna(df2.at[tcpn, column]) else ""

                    if value1 != value2:  # Only add changes
                        changes.append({
                            "Part Number": tcpn,
                            "Previous": df1.at[tcpn, category_column] if category_column in df1.columns else "N/A",
                            "Current": df2.at[tcpn, category_column] if category_column in df2.columns else "N/A",
                            "Attribute": column,
                            "From-Data": value1,
                            "To-Data": value2
                        })

    # Return as a DataFrame
    return pd.DataFrame(changes)
