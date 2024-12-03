import numpy as np
import matplotlib.pyplot as plt

# Dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000], # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020], # Day 5
    [1800, 2300, 2100, 1500, 1050], # Day 6
    [1900, 2400, 2200, 1600, 1100], # Day 7
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Basic Statistics
print("the total number of cases reported in each country over the 7 days : - ")
total_cases = covid_data.sum(axis=0)  # column-wise
for x,y in (zip(countries,total_cases)):
    print(f"{x} -> {y}")
print("The country with the highest total cases :-")
highest_cases_country = countries[np.argmax(total_cases)]
print(highest_cases_country)

# Daily Analysis
daily_totals = covid_data.sum(axis=1)
average_daily_cases = daily_totals.mean()
print("the average number of cases reported per day across all countries:-")
print(average_daily_cases)
day_highest_cases = np.argmax(daily_totals) + 1
print("Day with Highest Total Cases Across All Countries:", day_highest_cases)

# Trends: Percentage Change
percent_changes = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
country_highpercent = countries[np.argmax(percent_changes)]
print("Percentage Increase in Cases from Day 1 to Day 7:", percent_changes)
print("Country with Highest Percentage Increase:", country_highpercent)

# Data Transformation: Normalization
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))
print("Normalized Data:")
print(normalized_data)

# Visualization
plt.figure(figsize=(10, 6))
for i, country in enumerate(countries):
    plt.plot(covid_data[:, i], label=country, marker='o')

plt.legend()
plt.title("Daily COVID-19 Cases by Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.xticks(ticks=np.arange(7), labels=[f"Day {i+1}" for i in range(7)])
plt.grid(True)
plt.show()