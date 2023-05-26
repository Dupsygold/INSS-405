def calculate_mean(numbers):
    return sum(numbers)/len(numbers)

def calculate_sum(numbers):
    return sum(numbers)

def calculate_median(numbers):
    sorted_numbers= sorted(numbers)
    n= len(sorted_numbers)
    if n % 2== 0:
        median= (sorted_numbers[n//2-1]+sorted_numbers[n//2])/2
    else:
        median= sorted_numbers[n//2]
    return median

# Collecting user input numbers
numbers = []
for _ in range(10):
    number= int(input("Enter a number:"))
    numbers.append(number)

# Calculating mean, sum, and median
mean = calculate_mean(numbers)
sum_of_numbers= calculate_sum(numbers)
median = calculate_median(numbers)

# Printing the results
print("Mean:", mean)
print("Sum:", sum_of_numbers)
print("Medium:", median)


