from pprint import pprint
# student = {
#     "name": "Rox",
#     "surname": "Ford",
#     "age": 28,
#     "family Members": {"Father":"John", "Mother": "Maria", "Brother":"Sebastian"},
#     "wins in last for years": [2, 4, 11, 8],
#     "favourite courses": {
#         "Python": {
#             "Teacher": "Paul",
#             "Surname": "Polanski",
#             "Topics": ["Lists", "Sets", "Tuples", "Dictionaries"],
#             "Earnings": [[23, 24], [25, 26], [27, 28, 29]]
#         },
#         "HTML": {
#             "Teacher": "Unknown",
#             "Surname": "Mr Good"
#         }
#     }
# }

# pprint(student["favourite courses"]["Python"]["Earnings"][0][0])
# pprint(student["favourite courses"]["Python"]["Earnings"][1][0])
# pprint(student["favourite courses"]["Python"]["Earnings"][2][0])
# student["name"] = "Angelina"
# student["interests"] = "Programming"

data = {
  'students': [
    {
      'name': 'Josephine',
      'subjects': [
        {
          'name': 'English',
          'teacher': 'Mr. Hoover'
        }
      ]
    },
    {
      'name': 'Luke',
      'subjects': [
        {
          'name': 'History',
          'teacher': 'Mrs. Peters'
        }
      ]
    },
    {
      'name': 'Julia',
      'subjects': [
        {
          'name': 'Chemistry',
          'teacher': 'Mrs. Fauci'
        }
      ]
    }
  ]
}

# print(data['students'][2]['subjects'][0]["teacher"])
list2 = {
    'name': 'Rox',
    'subjects': [
        {
            'name': "Python Fundamentals",
            'teacher': "Paul Polanski"
        },
        {
            'name': "Programming fundamentals",
            'teacher': "Mr X"
        }
    ]
}
data['students'].append(list2)

for element in data.values():
    for subelement in element:
        for x in subelement.values():
            if x == "Rox":
                print("Great, we found Rox in this huge dictionary!")

