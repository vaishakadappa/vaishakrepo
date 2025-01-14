
import pandas as pd
from fuzzywuzzy import fuzz  # Importing fuzzywuzzy for similarity calculation


def compare_all_headers(df1, df2, reference_column='endNodeCategory', similarity_threshold=80):
    """
    Compare attributes of each category in the reference column with fuzzy matching and generate a report.

    Args:
        df1 (pd.DataFrame): DataFrame for the first file.
        df2 (pd.DataFrame): DataFrame for the second file.
        reference_column (str): Column name used to identify categories.
        similarity_threshold (int): Similarity score threshold for fuzzy matching.

    Returns:
        pd.DataFrame: A DataFrame summarizing the attribute comparison.
    """

    summary_counts = {'No Change': 0, 'Updated': 0, 'New': 0, 'Deleted': 0}
    result = []

    # Get unique categories from both files
    categories_file1 = df1[reference_column].dropna().unique()
    categories_file2 = df2[reference_column].dropna().unique()

    # Get the union of all unique categories
    all_categories = set(categories_file1).union(set(categories_file2))

    for category in all_categories:
        # Filter rows belonging to the current category in both dataframes
        df1_subset = df1[df1[reference_column] == category]
        df2_subset = df2[df2[reference_column] == category]

        # Identify non-empty columns (attributes) for the current category
        attributes_file1 = df1_subset.columns[df1_subset.notna().any()].tolist()
        attributes_file2 = df2_subset.columns[df2_subset.notna().any()].tolist()

        # Compare attributes
        deleted_attributes = set(attributes_file1) - set(attributes_file2)
        new_attributes = set(attributes_file2) - set(attributes_file1)
        unchanged_attributes = set(attributes_file1).intersection(set(attributes_file2))

        # Append results for deleted attributes
        for attr in deleted_attributes:
            result.append({
                'Previous': category,
                'Current': category,
                'Previous_Attribute': attr,
                'Current_Attribute': None,
                'Status': 'Deleted'
            })
            summary_counts['Deleted'] += 1

        # Append results for new attributes
        for attr in new_attributes:
            result.append({
                'Previous': category,
                'Current': category,
                'Previous_Attribute': None,
                'Current_Attribute': attr,
                'Status': 'New'
            })
            summary_counts['New'] += 1

        # Append results for unchanged attributes with fuzzy matching
        for attr in unchanged_attributes:
            # Compare attributes using fuzzy matching
            similarity = fuzz.ratio(attr, attr)  # Compare `Previous_Attribute` with `Current_Attribute`
            if similarity >= similarity_threshold:
                result.append({
                    'Previous': category,
                    'Current': category,
                    'Previous_Attribute': attr,
                    'Current_Attribute': attr,
                    'Status': 'No Change'
                })
                summary_counts['No Change'] += 1
            else:
                result.append({
                    'Previous': category,
                    'Current': category,
                    'Previous_Attribute': attr,
                    'Current_Attribute': attr,
                    'Status': 'Updated'
                })
                summary_counts['Updated'] += 1

    # Convert the result to a DataFrame
    return pd.DataFrame(result)
