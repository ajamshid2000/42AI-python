import pandas


def how_many_medals(data, str):
    medals = {}
    athlete_data = data[data["Name"] == str]
    
    for _, x in athlete_data.iterrows():
        if x["Year"] not in medals:
            medals[x["Year"]] = {'G':0, 'S':0,'B':0}
        if(x["Medal"] == "Gold"):
            medals[x["Year"]]["G"] += 1
        if(x["Medal"] == "Silver"):
            medals[x["Year"]]["S"] += 1
        if(x["Medal"] == "Bronze"):
            medals[x["Year"]]["B"] += 1
    for year, counts in medals.items():
        print(year, counts)