
data = {
    'cars': ["BMW", "Volvo", "Ford", "Mercedes"],
    'prices': [50000, 40000, 30000, 60000]
}

# for car in data['cars']:
#     print(car)
#     # print(car.upper() + "!")

i = 0
while i < len(data['cars']):
    print(f"Index {i}: {data['cars'][i]} costs ${data['prices'][i]}")
    i += 1
    # if data['cars'][i] == "Ford": break
    # print("Still going...")
