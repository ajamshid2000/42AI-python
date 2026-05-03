"""
Utility to count the number of medals earned by an athlete by year.
"""

import pandas as pd
from typing import Dict, Optional


def how_many_medals(data: pd.DataFrame, athlete_name: str) -> Optional[Dict[int, Dict[str, int]]]:
    """
    Count the number of Gold, Silver, and Bronze medals earned by an athlete per year.

    Args:
        data: DataFrame containing athlete data.
        athlete_name: Name of the athlete to filter by.

    Returns:
        Dictionary with years as keys and medal counts {'G': int, 'S': int, 'B': int}.
    """
    medals: Dict[int, Dict[str, int]] = {}
    athlete_data = data[data["Name"] == athlete_name]

    if athlete_data.empty:
        return None

    for _, row in athlete_data.iterrows():
        year = row["Year"]
        medal_type = row["Medal"]

        if year not in medals:
            medals[year] = {'G': 0, 'S': 0, 'B': 0}

        if medal_type == "Gold":
            medals[year]['G'] += 1
        elif medal_type == "Silver":
            medals[year]['S'] += 1
        elif medal_type == "Bronze":
            medals[year]['B'] += 1

    return medals if medals else None


if __name__ == "__main__":
    # Example usage
    # Load data and call how_many_medals
    pass