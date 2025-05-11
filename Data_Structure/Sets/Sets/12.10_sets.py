a = {1,2,3,5,2,1,4,6,8,2,4,1,0,0,6,5,8}
print(a)
b = {'hi','ha','ho', 'gn', 'hi', 'ha', 'ho'}
print(b)
c = set([1,2,3,4,5,2,1,3,4,8,5,1])
print(c)
d = set('abracadabra')
print(d)
e = set(range(5))
print(e)
f = ()
print(type(f))

set1 = {'Fender', 'Gibson', 'Marshall', 'Ibanez'}
set2 = {'Fender', 'Boss','Peavy', 'Milky'}
set3 = {'Fender', 'Peavy','Boss', }


print('Checking for set content equality: ', set1==set1)
print('Проверка на равенство содержимого набора: ', set1==set1)

print('------------------------------------------------1--')
#interaction allows extraction of unique values from
print('Unique elements from both sets: ', set1.intersection(set2))
print('Уникальные элементы из обоих наборов: ', set1.intersection(set2))
#print('Unique elements from both sets: ', set1.interaction_update(set2))
print('------------------------------------------------2--')

#show unique elements of one set with difference
print('Unique elements in the first sets: ', set1.difference(set2))
print('Уникальные элементы в первом наборе: ', set1.difference(set2))

print('------------------------------------------------3--')

#Show non-common elements from both sets 
print(' elements that are not shared by both sets are: ', set1.symmetric_difference(set2))
print(' элементы, не являющиеся общими для обоих наборов, являются: ', set1.symmetric_difference(set2))

print('------------------------------------------------4--')


#Show unique elements of one set with difference() method
print('Unique elements in the first set: ', set1.difference(set2))
print('Уникальные элементы в первом наборе: ', set1.difference(set2))

print('------------------------------------------------5--')


#show everything or two sets
print('Union of two sets: ', set1.union(set2))
print('Объединение двух множеств: ', set1.union(set2))
print('------------------------------------------------4--')

#Check for contents equality = the same elements are present
print('Checking for set content: ', set2==set3)
print('Проверка содержимого набора: ', set2==set3)
print('------------------------------------------------5--')
print('Checking for reference equality: ', set2 is set3)
print('Проверка на равенство ссылок: ', set2 is set3)
print('------------------------------------------------5--')
print(id(set2), id(set3))
print(dir(set3))
print('------------------------------------------------5--')

#testing sets using predicate methods
print('Checking for disjoints: ', set1.isdisjoint(set2))
print('Проверка на наличие расхождений: ', set1.isdisjoint(set2))
print('------------------------------------------------5--')
print('Checking for subsets: ', set1.issubset(set2))
print('Проверка наличия подмножеств: ', set1.issubset(set2))
print('------------------------------------------------5--')
print('Checking for superset: ', set1.issuperset(set2))
print('Проверка на наличие суперсетов: ', set1.issuperset(set2))


#Accessing individual elements of a set using a for loop
for x in set1:
    if x =='Fender':
        print(set1)





















