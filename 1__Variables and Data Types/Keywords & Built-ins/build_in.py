x=dir(['what' ,'i' ,'can', 'use', 'with', 'list'])
y=dir(1)
print('*'*20)

print(x)
print('*'*20)

print(y)

print('='*20)
popcorn='я люблю попкорн'
print(dir(popcorn))


# не в одну строку,все таки принт
my_prog='''print('бутерброд') 
print('с колбасой')'''
print(exec(my_prog))
# exec = просто выполняет код,он не возвращает результат