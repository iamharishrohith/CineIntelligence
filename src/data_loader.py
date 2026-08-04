import os
import pandas as pd

def load_data(filepath=None):
    """
    Loads dataset from CSV file.
    If no path is provided, loads default dataset/imdb_movies_dataset.csv.
    """
    if filepath is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = os.path.join(base_dir, 'dataset', 'imdb_movies_dataset.csv')
    
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset file not found at: {filepath}. Run src/generate_dataset.py first.")
    
    df = pd.read_csv(filepath)
    return df

def inspect_data(df):
    """
    Returns diagnostic summary statistics of the dataset.
    """
    summary = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'column_types': {col: str(dtype) for col, dtype in df.dtypes.items()},
        'category_distribution': df['rating_category'].value_counts().to_dict() if 'rating_category' in df else {}
    }
    return summary

if __name__ == '__main__':
    data = load_data()
    info = inspect_data(data)
    print("Dataset Loaded Successfully.")
    print(f"Total Rows: {info['total_rows']}, Total Columns: {info['total_columns']}")
    print("Category Distribution:", info['category_distribution'])
