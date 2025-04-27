"""clean_text (lambda) -мы чистим текст (убираем знаки препинания и приводим текст к нижнему регистру).
Разбиваем текст на отдельные слова с помощью re.findall().Перед анализом текста нужно убрать лишние символы и стандартизировать его.
мы используем регулярное выражение, которое ищет слова. - re.findall(r'\b\w+\b', text.lower()).get_top_words (lambda) - сначала фильтруем слова по длине (filter()),
затем считаем их частоту с помощью Counter(), а после сортируем по убыванию.Считаем частоту каждого слова, сортируем слова по убыванию частоты.
для нахождения наиболее часто встречающихся слов. Возвращает top_n самых частых слов, благодаря этому нам позволяется быстро получить статистику по наиболее 
частым словам.filter(lambda word: len(word) >= min_length, words) - убираем слишком короткие слова.
Counter() - считает количество вхождений слов. 
sorted(..., key=lambda item: item[1], reverse=True) - сортирует слова по убыванию частоты.
и используем в analyze_text(), чтобы показать, какие слова встречаются чаще всего.
analyze_text(text)-- основная функция, здесь мы запускаем анализ текста. analyze_text(text) --использует clean_text() 
clean_text(text) - очищаем текст
top_words = get_top_words(words) - получаем список частых слов. и выводим статистику топ-5 слов
analyze_text(text)--это главная функция анализа текста.Она вызывает
clean_text()-анализ и get_top_words() - для анализа частоты.
В add_one (lambda) - мы принимаем число и увеличиваем его на 1. 
is_even и is_odd (lambda)-- проверяют, четное число или нечетное.
в @decorator (lambda)- модифицируем функцию, и оборачиваем её 
и добавляем print() до и после вызова функции.
"""
"""‘‘’clean_text (lambda) - we clean the text (remove punctuation marks and lowercase the text).
We break the text into individual words using re.findall().Before analysing the text, we need to remove unnecessary characters and standardise it.
We use a regular expression that searches for words. - re.findall(r‘\b\w+\b’, text.lower()).get_top_words (lambda) - First we filter the words by length (filter()),
then count their frequency using Counter(), and then sort them in descending order. Count the frequency of each word, sort the words in descending order of frequency.
To find the most frequent words. Returns the top_n of the most frequent words, this allows us to quickly get statistics on the most 
filter(lambda word: len(word) >= min_length, words) - remove words that are too short.
Counter() - counts the number of occurrences of words. 
sorted(..., key=lambda item: item[1], reverse=True) - sorts words by decreasing frequency.
and use it in analyse_text() to show which words occur most often.
analyze_text(text)-- the main function, this is where we run the text analysis. analyze_text(text)-- uses clean_text() 
clean_text(text)--clean text
top_words = get_top_words(words) - get the list of frequent words. and display the statistics of top 5 words.
analyze_text(text)-this is the main function of text analysis. It calls
clean_text()-analysis and get_top_words() - to analyse the frequency.
In add_one(lambda)--we take a number and increment it by 1. 
is_even and is_odd (lambda)-- prov

Translated with DeepL.com (free version)"""
import sys
import re
from collections import Counter

# Устанавливаем кодировку, чтобы поддерживать эмодзи и спецсимволы
sys.stdout.reconfigure(encoding='utf-8')

# === Часть 1: Анализ текста ===
# Очищаем текст от знаков препинания и приводим к нижнему регистру
clean_text = lambda text: re.findall(r'\b\w+\b', text.lower())

# Подсчитываем частоту слов и выбираем самые популярные
get_top_words = lambda words, min_length=3, top_n=5: sorted(
    Counter(filter(lambda word: len(word) >= min_length, words)).items(),
    key=lambda item: item[1], 
    reverse=True
)[:top_n]

# Основная функция для анализа текста
def analyze_text(text):
    words = clean_text(text)
    top_words = get_top_words(words)
    
    print("\n\U0001F4CA Анализ текста:")
    print(f"\U0001F538 Всего слов в тексте: {len(words)}")
    print("\U0001F538 Топ-5 самых частых слов:")
    for word, freq in top_words:
        print(f"   - {word}: {freq} раз(а)")


sample_text = "We must not let fear command the mind; Otherwise we depart from our endeavours, Like a beast when he dreams.’"
analyze_text(sample_text)



add_one = lambda x: x + 1
print(add_one(2))  # Вывод: 3


add_numbers = lambda x, y: x + y
print(add_numbers(2, 3))  # Вывод: 5


hello = lambda: "Hello, lambda!"
print(hello())  # Вывод: "Привет, lambda!"


power = lambda x, y: x ** y
print(power(2, 5)) 

is_even = lambda x: x % 2 == 0
is_odd = lambda x: x % 2 != 0
print(is_even(4), is_odd(5))  # Output: 5


numbers = [1, 2, 3, 4]
double = list(map(lambda x: x * 2, numbers))
print(double)  

def outer_function(x):
    return lambda y: x + y

add_five = outer_function(5)
print(add_five(10))  # Output: 15


decorator = lambda func: lambda: (print(" b4 func"), func(), print(" after func"))

@decorator
def my_func():
    print("Inside a function")

my_func()
