"""Task - Access nested keys
Accessing a value in a nested dictionary can lead to difficult to read syntax like: data['really']['deeply']['nested']['value'].

Implement a method get that takes a dictionary and a nested key name with levels seperated by . (really.deeply.nested.value in the example) and returns the value if it exists and None if it doesn't.

A key can also be an integer like in.a.list.0.

Input:
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
Output:
> get(data, 'students.1.subjects.0.name')
History

> get(data, 'students.0.subjects.0.teacher')
Mr. Hoover"""


def get(data, path):
    keys = path.split('.')  
    # Разделяем путь по точкам
    # Split the path by points
    for key in keys:
        try:
            # Check if the key is a number (for list indexing)
            # Проверяем, является ли ключ числом (для индексации списка)
            if key.isdigit():
                key = int(key)
            data = data[key]  
            # Moving on to the next level
            # Переходим к следующему уровню
        except (KeyError, IndexError, TypeError):
            return None  
        # If the key or index could not be found, return None
        # Если не удалось найти ключ или индекс, возвращаем None
    return data


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


print(get(data, 'students.1.subjects.0.name'))  #output: history
print(get(data, 'students.0.subjects.0.teacher'))  #output: mr. hoover
