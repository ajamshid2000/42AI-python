
import pandas

def proportion_by_sport(data, year, sport, sex):
    yearly_data = data[data["Year"] == year]
    sport_data = yearly_data[yearly_data["Sport"] == sport]
    sex_data = yearly_data[yearly_data["Sex"] == sex].drop_duplicates(subset=["Name", "Age", "Sport"])
    sport_sex_data = sport_data[sport_data["Sex"] == sex].drop_duplicates(subset=["Name", "Age"])
    print(sex_data.shape[0], sport_sex_data.shape[0], sport_sex_data.shape[0]/sex_data.shape[0])
    