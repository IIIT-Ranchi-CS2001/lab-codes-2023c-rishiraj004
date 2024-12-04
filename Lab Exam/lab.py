#RISHI RAJ
#2023UG2005
#SET-3

import pandas as pd  # Importing Modules
import numpy as np

# Reading CSV
df = pd.read_csv(r"C:\Users\rishi\lab-codes-2023c-rishiraj004\Lab Exam\AQI_Data.csv")

# Display First eight rows
print("First Eight Rows")
print(df.head(8))

#Display Last five rows
print("\nLast 5 rows")
print(df.tail(5))

# Display data types of each column
print("\nData Types:")
print(df.dtypes)

# Display the number of non-null values in each column
print("\nNumber of Non-Null Values:")
print(df.notnull().sum())

#Mean AQI
print("\nMean AQI for each city : ")
print(df.groupby('City')['AQI'].mean())

# Max PM 2.5
print("\nMaximum PM 2.5 for each city : ")
print(df.groupby('City')['PM2.5'].max())

# Min PM 10
print("\nMinimum PM 10 for each city : ")
print(df.groupby('City')['PM10'].min())

grouped = df.groupby("City")

# Calculate the required statistics for each city
city_stats = grouped.agg({
    "AQI": "mean",       # Average AQI
    "PM2.5": "max",      # Maximum PM2.5
    "PM10": "min"        # Minimum PM10
})

# Convert the DataFrame into a dictionary of lists
result = city_stats.to_dict(orient="index")

# Display the result
print("\n\nStatistical Information for Each City:")
print(result)