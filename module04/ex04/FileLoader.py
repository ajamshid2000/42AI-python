"""
FileLoader class for reading and displaying CSV data using pandas.
"""

import pandas as pd
from typing import Optional, Union
import sys


class FileLoader:
    """A class to load and display CSV files using pandas."""

    @staticmethod
    def load(path: str) -> Optional[pd.DataFrame]:
        """
        Load a CSV file into a pandas DataFrame.

        Args:
            path: Path to the CSV file.

        Returns:
            DataFrame if successful, None otherwise.
        """
        if not isinstance(path, str):
            print("Error: path is expected to be a string", file=sys.stderr)
            return None

        try:
            data = pd.read_csv(path)
            print(f"Loading dataset of dimensions {data.shape}")
            return data
        except FileNotFoundError:
            print(f"Error: File '{path}' not found", file=sys.stderr)
            return None
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    @staticmethod
    def display(df: Optional[pd.DataFrame], n: int) -> None:
        """
        Display the first n rows of a DataFrame.

        Args:
            df: DataFrame to display.
            n: Number of rows to display.
        """
        if not isinstance(df, pd.DataFrame):
            print("Error: df is expected to be a pandas.DataFrame", file=sys.stderr)
            return
        if not isinstance(n, int):
            print("Error: n is expected to be an integer", file=sys.stderr)
            return

        print(df.head(n))