import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('/Users/bokense1/Desktop/PyData/countries.csv')

countries = []
countries_data = []

for i in range(0,1704):
    if (i % 12 == 0):
        countries.append(data.country[i])

for i in range(0,len(countries)):
    countries_data.append(data[data.country == countries[i]])


for i in range(0,len(countries_data)):

    plt.plot(countries_data[i].year,countries_data[i].population / 10 ** 6)

plt.legend(countries)
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.show()
