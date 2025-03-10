import datetime
# Create a lambda function that adds 15 to a given number passed in as an argument. Assign the lambda function to a variable name called add15.
print("-------------------------------------------------------1----")
add= lambda x: x + 15
print(add(1))
print(add(-2))
print("------------------------------------------------------2-----")
#Define the functions isOdd, isEven and getParity from previous exercises, but now as lambda functions assigned to variables.


is_Odd = lambda n: n%2 !=0
is_Even = lambda n: n% 2 ==0
getParity = lambda n,p:(n% 2!= 0 if p == 'odd' else n % 2 == 0) if p in ['odd'  'even'] else "Parity indicated is unknown"
print(is_Odd(2), is_Even(2))
print(is_Odd(1), is_Even(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))

print("------------------------------------------------------3-----")
# Define a lambda function assigned to a variable named starts_with_p that takes a single argument as a string. Returns True if this string starts with P (case insensitive) and False if it does not.

starrts_with_p = lambda s: s.lower(). startswith('p')
print(starrts_with_p("Python"))
print(starrts_with_p("Java"))
print(starrts_with_p("pirate"))

print("-------------------------------------------------------4----")
# For a given list of numbers, use a lambda function to return the result of multiplying each number by a given number stored in a variable named factor in the global scope.

num = [2,4,5,7,9, 14]
factor = 2
result = list(map(lambda x: x  * factor, num))
print(result)