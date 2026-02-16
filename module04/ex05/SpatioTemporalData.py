import pandas

class SpatioTemporalData:
    def __init__(self, dataframe_given):
        self.datafame = dataframe_given

    def when(self, location):
        data = self.datafame[self.datafame["City"] == location]
        date = data["Year"].unique().tolist()
        print(date)
    
    def where(self , date):
        data = self.datafame[self.datafame["Year"] == date]
        location = data["City"].unique().tolist()
        print(location)