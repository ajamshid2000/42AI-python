import pandas
import matplotlib.pyplot as plt

class MyPlotLib:
    def histogram(self, data, features):
        for feature in features:
            plt.hist(data[feature])
            plt.title(feature)
            plt.show()
    
    def density(self, data, features):
        for feature in features:
            plt.plot(data[feature])
            plt.title(feature)
            plt.show()
    
    def pair_plot(self, data, features):
        for feature in features:
            plt.hist(data[feature])
            plt.title(feature)
            plt.show()
    
    def box_plot(self, data, features):
        for feature in features:
            plt.boxplot(data[feature])
            plt.ylabel(feature)
            plt.show()
    