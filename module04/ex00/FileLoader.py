import pandas

class FileLoader:
    def load(self, path):
        if(not isinstance(path, str)):
            print("path is expected to be string")
            return
        try:
            data = pandas.read_csv(path)
            print("Loading dataset of dimensions", data.shape)
            # print(type(data))
            return pandas.DataFrame(data)
        except Exception as e:
            print(e)
        
    def display(self, df, n):
        if(not isinstance(df, pandas.DataFrame)):
            print("df is expected to be pandas.dataFrame")
            return
        if(not isinstance(n, int)):
            print("n is expected to be int")
        print(df[:n])