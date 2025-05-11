import math
import random
from collections import Counter, defaultdict


def calculate_stats(*numbers, operation='avg', **options):
   
    if not numbers:
        return None
    
    #без обработки отрицательных чисел:
    #processed_numbers = numbers
    
    round_digits = options.get('round_digits', None)
    ignore_negative = options.get('ignore_negative', False)
    
    #по разным условиямм фильтрации:
    #processed_numbers = [n for n in numbers if n > 0]  # только положительные
    processed_numbers = [
        n for n in numbers 
        if not ignore_negative or n >= 0
    ]
    
    if not processed_numbers:
        return None
    
    if operation == 'avg':
        result = sum(processed_numbers) / len(processed_numbers)
        #через math.fsum: with math.fsum
        # result = math.fsum(processed_numbers) / len(processed_numbers)
    elif operation == 'sum':
        result = sum(processed_numbers)
    elif operation == 'prod':
        result = math.prod(processed_numbers)
        #вцикле:
        #result = 1
        #for n in processed_numbers:
        #    result *= n
    elif operation == 'median':
        sorted_nums = sorted(processed_numbers)
        n = len(sorted_nums)
        result = (sorted_nums[n//2] + sorted_nums[(n-1)//2]) / 2
        #result = sorted_nums[n//2]
    else:
        raise ValueError(f"Unknown operation: {operation}")
    
    if round_digits is not None:
        result = round(result, round_digits)
        #округлить через format:
        #result = float(f"{result:.{round_digits}f}")
    
    return result


def generate_random_values(*, count=1, **dist_params):
   
    dist_type = dist_params.get('dist', 'uniform')
    
    #без проверки типа распределения:
    # return [random.random() for _ in range(count)]
    
    if dist_type == 'uniform':
        low = dist_params.get('low', 0)
        high = dist_params.get('high', 1)
        #if low == high:
        #return [low] * count
        return [random.uniform(low, high) for _ in range(count)]
    elif dist_type == 'normal':
        mean = dist_params.get('mean', 0)
        stddev = dist_params.get('stddev', 1)
        #while True:
        #    val = random.gauss(mean, stddev)
        #    if mean - 3*stddev <= val <= mean + 3*stddev:
        #        return val
        return [random.gauss(mean, stddev) for _ in range(count)]
    elif dist_type == 'int':
        low = dist_params.get('low', 0)
        high = dist_params.get('high', 100)
        #варианты генерации:

        #return random.choices(range(low, high+1), k=count)
        return [random.randint(low, high) for _ in range(count)]
    else:
        raise ValueError(f"Unknown distribution type: {dist_type}")


def process_items(*items, **processing_options):

    if not items:
        return None
    
    #просто возвращать список:
    #return list(items)
    
    if processing_options.get('count', False):
        #counts = {}
        #for item in items:
        #    counts[item] = counts.get(item, 0) + 1
        #return counts
        return Counter(items)
    
    if processing_options.get('unique', False):
        #сначала list comprehension:
        #return [item for i, item in enumerate(items) if item not in items[:i]]
        return list(set(items))
    
    if processing_options.get('group_by_type', False):
        type_dict = defaultdict(list)
        #без defaultdict:
        #type_dict = {}
        #for item in items:
        #    if type(item) not in type_dict:
        #        type_dict[type(item)] = []
        #    type_dict[type(item)].append(item)
        for item in items:
            type_dict[type(item)].append(item)
        return dict(type_dict)
    
    return list(items)



if __name__ == "__main__":
    print("=== Math Examples ===")
    print("Average:", calculate_stats(1, 2, 3, 4, 5))
    #print("Average (empty):", calculate_stats())
    print("Sum with rounding:", calculate_stats(1.1, 2.2, 3.3, operation='sum', round_digits=1))
    print("Median ignoring negatives:", calculate_stats(-1, 2, 3, -4, 5, operation='median', ignore_negative=True))
    #print("Product:", calculate_stats(2, 3, 4, operation='prod'))
    
    print("\n=== Random Examples ===")
    print("Uniform:", generate_random_values(count=3, dist='uniform', low=5, high=10))
    #print("Default random:", generate_random_values(count=2))
    print("Normal:", generate_random_values(count=3, dist='normal', mean=100, stddev=15))
    print("Integers:", generate_random_values(count=5, dist='int', low=1, high=6))
    #print("Invalid dist:", generate_random_values(dist='invalid'))
    
    print("\n=== Collections Examples ===")
    sample_items = [1, 2, 2, 'a', 'b', 'a', 3.14, True, False, True]
    #по разным наборам данных:
    # sample_items = ['apple', 'banana', 'apple', 'orange']
    print("Count:", process_items(*sample_items, count=True))
    print("Unique:", process_items(*sample_items, unique=True))
    print("Group by type:", process_items(*sample_items, group_by_type=True))
    #print("Default processing:", process_items(*sample_items))
    
    #Дополнительные эксперименты:
    #print("\n=== Extra Experiments ===")
    ## Передача списка как *args
    #nums = [5, 10, 15]
    #print("Unpacked list:", calculate_stats(*nums))
    
    ##передача словаря как **kwargs
    #options = {'operation': 'sum', 'round_digits': 2}
    #print("With dict options:", calculate_stats(1.234, 2.345, **options))