
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

# for idx in range(len(data['cars'])):
#     print(data['cars'][idx], data['prices'][idx])
#     # data['prices'][idx] += 1000  # подорожание!

for pos, (car, price) in enumerate(zip(data['cars'], data['prices'])):
    print(f"Pos {pos}: {car} - {price}")
    # if pos == 1: print("Second element!")
    # data['prices'][pos] = price * 0.9  # скидка 10%

car_features = {
    "BMW": ["sport", "red"],
    "Volvo": ["family", "blue"],
    "Ford": ["truck", "black"],
    "Mercedes": ["luxury", "silver"]
}
