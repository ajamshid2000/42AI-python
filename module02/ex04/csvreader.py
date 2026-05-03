
"""
CSV reader context manager for reading and processing CSV files.
"""

import csv
from typing import List, Optional


class CsvReader:
    """
    A context manager for reading CSV files with header, skip options.

    Attributes:
        filename: Path to the CSV file.
        sep: Delimiter character.
        header: Whether to extract header row.
        skip_top: Number of rows to skip from top.
        skip_bottom: Number of rows to skip from bottom.
    """

    def __init__(self, filename: Optional[str] = None, sep: str = ',',
                 header: bool = False, skip_top: int = 0, skip_bottom: int = 0) -> None:
        """
        Initialize the CSV reader.

        Args:
            filename: Path to CSV file.
            sep: Delimiter (default: comma).
            header: Extract header row.
            skip_top: Skip rows from top.
            skip_bottom: Skip rows from bottom.
        """
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        self.file = None
        self.reader = None
        self.data: Optional[List[List[str]]] = None
        self.header_value: Optional[List[str]] = None

    def __enter__(self) -> Optional['CsvReader']:
        """
        Enter context manager.

        Returns:
            Self if file is valid, None otherwise.
        """
        if self.filename is None:
            return None

        try:
            self.file = open(self.filename, newline='', encoding='utf-8')
            self.reader = csv.reader(self.file, delimiter=self.sep)
            self.data = list(self.reader)
        except Exception:
            return None

        # Validate data
        if not self.data or len(self.data) == 0:
            return None

        # Check for inconsistent column counts or empty cells
        first_row_len = len(self.data[0])
        for row in self.data:
            if len(row) != first_row_len or any(len(cell) == 0 for cell in row):
                return None

        # Extract header
        if self.header:
            self.header_value = self.data[0]

        # Skip rows from top and bottom
        if self.skip_top > 0:
            self.data = self.data[self.skip_top:]
        if self.skip_bottom > 0:
            self.data = self.data[:-self.skip_bottom]

        return self

    def __exit__(self, *args) -> None:
        """Exit context manager and close file."""
        if self.file:
            self.file.close()

    def getdata(self) -> Optional[List[List[str]]]:
        """
        Retrieve data from skip_top to skip_bottom.

        Returns:
            Nested list of data rows.
        """
        return self.data

    def getheader(self) -> Optional[List[str]]:
        """
        Retrieve the header row.

        Returns:
            List of header values if header=True, None otherwise.
        """
        return self.header_value


if __name__ == "__main__":
    with CsvReader('good.csv', header=True) as file:
        if file is not None:
            data = file.getdata()
            header = file.getheader()
            for row in data:
                print(row)
            print(header)