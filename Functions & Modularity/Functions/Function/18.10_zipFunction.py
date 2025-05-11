from ctypes import sizeof
from itertools import count
from pprint import pprint


list1 = ['string', 'another', True, False, 1,2,3]
list2 = {1:1,2:2,3:3,4:4,5:5,6:6,7:7}

list3 = zip(list1, list2)
print(list3)##покажет hex тип 

for x in list3:
    print(x)



data = {
  'key1': 1,
  'key2': 2,
  'key3': 3,
  'key4': 4,
  'key5': 5,
  'key6': 6,
}
def chunks(data):
    chunk_list = []
    curr_chunk = {}

    for key, values in data.items():
    
        if len(curr_chunk) == size:
            chunk_list.append(curr_chunk)
    
   

    print(chunk_list)
    print(curr_chunk)
print(chunks(data))



from pprint import pprint


def chunk(data, size):
    chunks = []
    current_chunk = {}

    for key, value in data.items():
        current_chunk[key] = value

        if len(current_chunk) == size:
            chunks.append(current_chunk)
            current_chunk = {}

    if current_chunk:
        chunks.append(current_chunk)
    return chunks


data = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4,
    'key5': 5,
    'key6': 6,
    'key7': 7,
    'key8': 8
}


result = chunk(data, 2)

pprint(result)




string = 'Elephant'
result = count(string)
print(result)

pprint([{'name': i, 
        'value': data[i]} 
        for i in data])



def score(name, participants, score):
    lowercase = name.lower()
    if lowercase in score:
        print(f'{name} scored {score[lowercase]} points ')
    else:
        print(f'{name} did not participate')

participants= ['Brian', 'Britney', 'Ben']
scores = {
'brian' : 25,
'britney': 80,
'ben': 50

} 
score('Paul', participants, scores)
score('Britney', participants, scores)