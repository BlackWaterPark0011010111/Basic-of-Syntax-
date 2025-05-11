from functools import reduce
from collections import Counter


temperatures_in_celsius = [20.5, 22.4, 19.8, 21.3, 18.9]
pollutants = ["CO2", "Ozone", "CO2", "SO2", "CO2"]
air_quality_index = [45, 62, 150, 55, 112]
humidity_levels = [45, 55, 60, 48, 53]


"""Temperature Conversion:
Use the map function to convert each temperature from Celsius to Fahrenheit. Formula: (celsius * 9/5) + 32
Store the results in a new list called temperatures_in_fahrenheit."""
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Applying map to the list of temperatures
temperatures_in_fahrenheit = list(map(celsius_to_fahrenheit, temperatures_in_celsius))


"""Poor Air Quality Identification:
Use the filter function to identify values in air_quality_index that exceed 100.
Store these values in a new list called poor_air_quality."""
def is_poor_air(index):
    return index > 100

# Applying filter to get locations with poor air quality
poor_air = list(filter(is_poor_air, air_quality_index))

"""Using the collections.Counter class, determine the most common pollutant in the pollutants list."""
pollutant_counts = Counter(pollutants)

most_common_pollutant = pollutant_counts.most_common(1)[0][0]  # Most common pollutant

"""Using the collections.Counter class, determine the most common pollutant in the pollutants list."""
total_humidity = reduce(lambda x, y: x + y, humidity_levels)
average_humidity = total_humidity / len(humidity_levels)

for index, (temp, air_quality, pollutant) in enumerate(zip(temperatures_in_fahrenheit, air_quality_index, [most_common_pollutant]*len(air_quality_index))):
    if air_quality > 100:
        print(f"Location {index+1}:")
        print(f"  Temperature: {temp:.2f}°F")
        print(f"  Air Quality Index: {air_quality}")
        print(f"  Most Common Pollutant: {pollutant}")
        print()


print(f"Temperatures in Fahrenheit: {temperatures_in_fahrenheit}")
print(f"Poor Air Quality Locations: {poor_air}")
print(f"Most Common Pollutant: {most_common_pollutant}")
print(f"Average Humidity: {average_humidity:.2f}%")
