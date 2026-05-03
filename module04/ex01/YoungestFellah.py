
"""
Utility to find the youngest male and female athletes in a given year.
"""

import pandas as pd
from typing import Dict


def youngest_fellah(data: pd.DataFrame, year: int) -> Dict[str, float]:
    """
    Find the youngest male and female athletes in a given year.

    Args:
        data: DataFrame containing athlete data with columns 'Year', 'Sex', 'Age'.
        year: The year to filter by.

    Returns:
        Dictionary with keys 'f' and 'm' and their minimum ages.
    """
    yearly_data = data[data["Year"] == year]
    male_data = yearly_data[yearly_data["Sex"] == 'M']
    female_data = yearly_data[yearly_data["Sex"] == 'F']

    return {
        'f': float(female_data["Age"].min()),
        'm': float(male_data["Age"].min())
    }


if __name__ == "__main__":
    # Example usage
    # Load data and call youngest_fellah
    pass