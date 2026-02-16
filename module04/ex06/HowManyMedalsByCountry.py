import pandas

def how_many_medals_by_country(data, country_name):
    medals = {}
    country_data = data[data['Team'] == country_name]
    dates = country_data["Year"].unique().tolist()
    for date in dates:
        G = 0
        S = 0
        B = 0
        date_data = country_data[country_data["Year"] == date]
        for x in date_data["Medal"]:
            if(x == 'Gold'):
                G += 1
            elif x == 'Silver':
                S +=1
            elif x == 'Bronze':
                B += 1
        medals[date] = {'G': G, 'S': S, 'B': B}

    print(medals)
    