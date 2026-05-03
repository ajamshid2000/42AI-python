"""
Utility to count the number of medals earned by a country by year.
"""

import pandas as pd
from typing import Dict, Optional


def how_many_medals_by_country(data: pd.DataFrame, country_name: str) -> Optional[Dict[int, Dict[str, int]]]:
    """
    Count the number of Gold, Silver, and Bronze medals earned by a country per year.

    Args:
        data: DataFrame containing Olympic athlete data.
        country_name: Name of the country (Team).

    Returns:
        Dictionary with years as keys and medal counts {'G': int, 'S': int, 'B': int}.
    """
    medals: Dict[int, Dict[str, int]] = {}
    country_data = data[data['Team'] == country_name]

    if country_data.empty:
        return None

    years = country_data["Year"].unique().tolist()

    for year in years:
        gold_count = 0
        silver_count = 0
        bronze_count = 0

        year_data = country_data[country_data["Year"] == year]
        for medal in year_data["Medal"]:
            if medal == 'Gold':
                gold_count += 1
            elif medal == 'Silver':
                silver_count += 1
            elif medal == 'Bronze':
                bronze_count += 1

        medals[year] = {'G': gold_count, 'S': silver_count, 'B': bronze_count}

    return medals if medals else None


if __name__ == "__main__":
    # Example usage
    # Load data and call how_many_medals_by_country
    pass

    print(medals)
    