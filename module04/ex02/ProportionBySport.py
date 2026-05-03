
"""
Utility to calculate the proportion of athletes in a sport for a given sex and year.
"""

import pandas as pd
from typing import Optional


def proportion_by_sport(data: pd.DataFrame, year: int, sport: str, sex: str) -> Optional[float]:
    """
    Calculate the proportion of athletes in a specific sport by sex and year.

    Args:
        data: DataFrame containing athlete data.
        year: The year to filter by.
        sport: The sport to filter by.
        sex: The sex to filter by ('M' or 'F').

    Returns:
        Proportion of athletes in the sport, or None if invalid input.
    """
    yearly_data = data[data["Year"] == year]
    sex_data = yearly_data[yearly_data["Sex"] == sex].drop_duplicates(subset=["Name", "Age", "Sport"])
    sport_sex_data = yearly_data[
        (yearly_data["Sport"] == sport) & (yearly_data["Sex"] == sex)
    ].drop_duplicates(subset=["Name", "Age"])

    if sex_data.shape[0] == 0:
        return None

    proportion = sport_sex_data.shape[0] / sex_data.shape[0]
    return proportion


if __name__ == "__main__":
    # Example usage
    # Load data and call proportion_by_sport
    pass
    