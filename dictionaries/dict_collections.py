import random

print("--------------------------------------------1-")
"""Create a variable called person which should hold a dictionary. The dictionary should have the key name with the value Bart Simpson and the key address with the value 742 Evergreen Terrace. Print the name and the address separated by comma to the screen."""
person = {
    "name": "Bart Simpson",
    "address": "742 Evergreen Terrace"
}
print(person["name"] + "," + person["address"])
print("--------------------------------------------2-")
"""Create two variables one called bart and the other called homer. Each stores a dictionary, one with the key name and the value Bart Simpson, the other one with the same key but the value Homer Simpson. Create a third variable address with a dictionary which only has one key address.Use update to add the address to both bart and homer. Print bart['address'] to the screen."""

bart = {"name": "Bart Simpson"}
homer = {"name": "Homer Simpson"}
address = {"address": "742 Evergreen Terrace"}
bart.update(address)
homer.update(address)
print(bart["address"])
print("--------------------------------------------3-")
"""Create a variable ages which holds a dictionary with the key Peter and the value 36, the key Robin and the value 29 and the key Michael with the value 33. Loop over the dictionary and print the name with the age."""

ages = {
    "Peter": 36,
    "Robin": 29,
    "Michael": 33
}
for name, age in ages.items():
    print(f"{name} is {age} years old")
print("--------------------------------------------4-")

"""Store the animals Alligator, Tiger, Parrot, Hamster, and Dolphin as keys in a dict. Use random numbers as values. Now remove all keys ending with r from the dictionary and print the resulting dict to the screen."""
animals = {
    "Alligator": random.randint(1,10),
    "Tiger": random.randint(1,10),
    "Parrot": random.randint(1,10),
    "Hamster": random.randint(1,10),
    "Dolphin": random.randint(1,10)

}
animals = {key: value for key, value in animals.items() if not key.endswith("r")}
print(animals)

print("--------------------------------------------5-")

"""You're given two dictionaries. Both have the same keys a, b, c with their values being random numbers. You need to multiply the values with the same key value in the other dict and sum all results."""
dict1 = {
    'a': 4,
    'b': 16,
    'c': 3
}

dict2 = {
    'a': 8,
    'b': 2,
    'c': 3
}

result = sum(dict1[key] * dict2[key] for key in dict1)
print(result)
print("--------------------------------------------6-")

"""Different programming languages use different kind of schemes to name things. For example Python uses snake_case, JavaScript uses camelCase. You might also come across kebap-case - sometimes also called dash-case. You can read more about naming conventions in programming the matching Wikipedia article.

When an API you are using is implemented using a different language it might not match Python's convention of naming things. Hence your task is to implement a method that converts a dictionary with natural cased keys like A random key to a_random_key."""

def to_snake_case(natural_dict):
    return {key.lower().replace(" ", "_"): value for key, value in natural_dict.items()}

natural_case_a = {
    'Company name': 'Digital Career Institute',
    'Street': 'Vulkanstraße',
    'House Number': 1,
    'City': 'Berlin'
}
print(to_snake_case(natural_case_a))

natural_case_b = {
        'Movie name': 'James Bond 007: Skyfall',
    'Director': 'Sam Mendes',
    'Production Year': 2012,
    'Duration in minutes': 143,
    'Production countries': ['US', 'UK']
}
print(to_snake_case(natural_case_b))

print("--------------------------------------------7-")
"""You are given two lists. One with color names (['red', 'green', 'blue']) and the other one with their RGB hex value (['#FF0000','#00FF00', '#0000FF']). Create a combined dict colors from those two lists so that for example printing colors['green'] shows #008000 on the screen."""


color_names = ['red', 'black', 'blue']
rgb_val = ['#FF0000', '#00FF00', '#0000FF']
colors = dict(zip(color_names, rgb_val))
print(colors["black"])