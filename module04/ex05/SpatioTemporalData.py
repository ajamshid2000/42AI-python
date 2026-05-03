"""
SpatioTemporalData class for analyzing Olympic event locations and years.
"""

import pandas as pd
from typing import List


class SpatioTemporalData:
    """A class to analyze spatio-temporal data from Olympic events."""

    def __init__(self, dataframe_given: pd.DataFrame) -> None:
        """
        Initialize with Olympic data.

        Args:
            dataframe_given: DataFrame with Olympic event data.
        """
        self.dataframe = dataframe_given

    def when(self, location: str) -> List[int]:
        """
        Get all years when the Olympics were held in a specific city.

        Args:
            location: Name of the city.

        Returns:
            List of years sorted.
        """
        data = self.dataframe[self.dataframe["City"] == location]
        years = sorted(data["Year"].unique().tolist())
        return years

    def where(self, year: int) -> List[str]:
        """
        Get all cities that hosted the Olympics in a specific year.

        Args:
            year: The Olympic year.

        Returns:
            List of cities.
        """
        data = self.dataframe[self.dataframe["Year"] == year]
        locations = data["City"].unique().tolist()
        return locations