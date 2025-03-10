

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584,
fibo0 = 0
fibo1 = 1
border = 50
while fibo0+fibo1<border:
    fibo2 = fibo0 + fibo1
    fibo0 = fibo1
    
    fibo1 = fibo2
    
    print(fibo1)


