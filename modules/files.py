import os
if os.path.exists('guess.py'):
    print('its exist')
else:
    print('its doesnt exist')


#создаем файл
newf = open('testfily.txt', 'w', encoding = 'utf-8')
print(newf.writable())
newf.write('Welcome to the world of files')
newf.write('This is ure second line')
newf.close()#самостоятельное управление памятью

f = open('fibo.py', encoding = 'utf-8')
lines = f.readlines()
print(type(lines))
for x in lines:
    print(x)

f.close()#самостоятельное управление памятью
#os.remove('testfile.txt') #это удаляет полностью файл из машины
print(os.getcwd())

