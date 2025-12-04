
import csv
class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        
        self.file = None
        self.reader = None
        self.data = None
        self.header_value = None
        
    def __enter__(self):
        if self.filename == None:
            return None
        self.file = open(self.filename, newline="")
        self.reader = csv.reader(self.file, delimiter = self.sep)
        
        # or i can do it simply self.data = list(self.reader)
        self.data = [x for x in self.reader]
        
        if any(len(x) != len(self.data[0]) or any(len(i) == 0 for i in x ) for x in self.data):
            return None
        
        if(not self.header_value and self.header == True):
            self.header_value = self.data[0]
            
        if(self.skip_top > 0):
            self.data = self.data[self.skip_top:]
        if(self.skip_bottom > 0):
            self.data = self.data[:-self.skip_bottom]

        return self
    def __exit__(self, *args):
        if self.file:
            self.file.close()
    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        return self.data
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if(self.header_value):
            return self.header_value
        else: return None
        

if __name__ == "__main__":
    with CsvReader('good.csv', header = True) as file:
        data = file.getdata()
        header = file.getheader()
for x in data:
    print(x) 
# print(data)
print(header)