import matplotlib.pyplot as plt

years = [2015, 2016, 2017, 2018, 2019]
population = [2.5, 2.7, 2.9, 3.0, 3.2]

plt.plot(years, population, marker='o')
plt.xlabel("Year")
plt.ylabel("Population (millions)")
plt.title("Population Growth Over Years")
plt.grid(True)
plt.show()