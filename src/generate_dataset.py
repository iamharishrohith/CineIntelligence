import os
import sys

SRC_DIR = os.path.dirname(os.path.abspath(__file__))
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from ingest_external_datasets import ingest_external_datasets

def generate_imdb_dataset(num_samples=None, random_seed=42):
    """
    Ingests official IMDb and TMDB 5000 external datasets into dataset/imdb_movies_dataset.csv.
    """
    return ingest_external_datasets()

if __name__ == "__main__":
    df_dataset = generate_imdb_dataset()
    print("Dataset generation pipeline connected to External Datasets.")
