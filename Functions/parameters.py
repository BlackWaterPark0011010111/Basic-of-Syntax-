print("-----------------------------------------------1----")
def isOdd(n):
    return n % 2 !=0
def isEven(n):
    return n % 2== 0
print(isOdd(1), isEven(1))
print(isOdd(6578363), isEven(773498))
print(isOdd(0)), isEven(0)

print("----------------------------------------------2-----")

def get_parity(number, parity):
    if parity =='odd':
        return number % 2 != 0
    elif parity == 'even':
        return number % 2 == 0
    else:
        return " parity indicates is unknown"
print(get_parity(1, 'odd'), get_parity(1, 'even'))
print(get_parity(657842, 'odd'), get_parity(657842, 'even'))
print(get_parity(0, 'odd'), get_parity(0, 'even'))
print(get_parity(-2, 'number'))
    
print("----------------------------------------------3-----")
def sumAll(*lists):
    total = 0
    for l in lists:
        total +=sum(l)
        return total
    
test1 = [[0,2,4,5]]
test2 = [[0,2,4,5], [6], 0,2,4,5,1,4,3,2]
print(sumAll(*test1))
print(sumAll(*test2))

print("----------------------------------------------4-----")
def pig_latin(*words, suffix="ay", single=False):
    vowels = 'aeiouAEOIU'
    result = []
    for phrase in words:
        new_words = []
        for word in phrase.split():
            if word[0] in vowels:
                new_words.append(word + suffix)
            else:
                new_words.append(word[1:] + word[0] + suffix)
            result.append(" ".join(new_words))
        return result[0] if single else result
    
test1= ["Word", "Apple"]
test1_config = {}

test2 = ["Python", "Function"]
test2_config = {"suffix": "oy"}

test3 = ["If the word starts with vowes", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1, **test1_config))
print(pig_latin(*test2, **test2_config))
print(pig_latin(*test3, **test3_config))
print("-----------------------------------------------5----")

print("---------------------------------------------------")


print("---------------------------------------------------")
print("---------------------------------------------------")
