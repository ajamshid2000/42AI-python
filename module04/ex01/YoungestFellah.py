
import pandas

def youngest_fellah(data, year):
    yearly_data = data[data["Year"] == year]
    male_data = yearly_data[yearly_data["Sex"] == 'M']
    female_data = yearly_data[yearly_data["Sex"] == 'F']
    print(f'\'f\': {female_data["Age"].min()}, \'m\': {male_data["Age"].min()}')