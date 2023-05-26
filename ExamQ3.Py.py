import random

def generate_random_integers():
    numbers=[]
    for_in: range[(1, 100)]
    numbers.append(random.randint(1, 1000))
    return numbers

def print_odd_numbers(numbers):
    odd_numbers=[num for num in numbers if num % 2 !=0]
    print("Odd Numbers:",",". join(map(str,odd_numbers)))

# Generate random generate
random_integers= generate_random_integers()

#Print odd numbers
print_odd_numbers(random_integers)









