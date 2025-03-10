import json

def filter_data(data, **filters):
    filtered_data = []
    for item in data:
        match = True
        for key, value in filters.items():
            if key in item and item[key] != value:
                match = False
                break
        if match:
            filtered_data.append(item)
    return filtered_data

# Example usage
data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

filters = {"age": 30, "city": "San Francisco"}

filtered_results = filter_data(data, **filters)
print(json.dumps(filtered_results, indent=2))
