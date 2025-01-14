
from fuzzywuzzy import fuzz
import pandas as pd


def filter_unique_data(df, reference_column):
    """
    Clean and normalize data by stripping spaces and converting to lowercase.
    """
    df = df.copy()
    df['normalized'] = df[reference_column].astype(str).str.strip().str.lower()
    return df.drop_duplicates(subset=['normalized'])


def compare_enodecategory(df1, df2, reference_column='enodecategory', threshold=80):
    """
    Compare 'enodecategory' between two DataFrames and identify status:
    No_Change, Updated, New, or Deleted.
    Retains original format for reporting.
    """
    summary_counts = {'No_Change': 0, 'Updated': 0, 'New': 0, 'Deleted': 0}
    # Clean and normalize data
    df1_cleaned = filter_unique_data(df1, reference_column)
    df2_cleaned = filter_unique_data(df2, reference_column)

    # Create dictionaries for normalized-to-original mapping
    df1_dict = dict(zip(df1_cleaned['normalized'], df1_cleaned[reference_column]))
    df2_dict = dict(zip(df2_cleaned['normalized'], df2_cleaned[reference_column]))

    # Create sets for comparison
    df1_categories = set(df1_cleaned['normalized'])
    df2_categories = set(df2_cleaned['normalized'])

    # Initialize results
    comparison_results = []

    # Find "No_Change" and "Updated"
    matched_categories = set()
    for cat1 in df1_categories:
        best_match = None
        best_score = 0
        for cat2 in df2_categories:
            score = fuzz.ratio(cat1, cat2)  # Fuzzy string matching
            if score > best_score:
                best_score = score
                best_match = cat2
        if best_score == 100:  # Exact match
            comparison_results.append({
                'Previous': df1_dict[cat1],
                'Current': df2_dict[best_match],
                'Status': 'No_Change'
            })
            summary_counts['No_Change'] += 1
            matched_categories.add(cat1)
            matched_categories.add(best_match)
        elif best_score >= threshold:  # Similar but not identical
            comparison_results.append({
                'Previous': df1_dict[cat1],
                'Current': df2_dict[best_match],
                'Status': 'Updated'
            })
            summary_counts['Updated'] += 1

            matched_categories.add(cat1)
            matched_categories.add(best_match)

    # Find "Deleted" categories
    for cat1 in df1_categories - matched_categories:
        comparison_results.append({
            'Previous': df1_dict[cat1],
            'Current': '',
            'Status': 'Deleted'
        })
        summary_counts['Deleted'] += 1

    # Find "New" categories
    for cat2 in df2_categories - matched_categories:
        comparison_results.append({
            'Previous': '',
            'Current': df2_dict[cat2],
            'Status': 'New'
        })
    summary_counts['New'] += 1

    return pd.DataFrame(comparison_results)
