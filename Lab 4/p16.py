numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
numbers.sort()
mean = sum(numbers) / len(numbers)
n = len(numbers)
if n % 2 == 1:
    median = numbers[n // 2]  
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2 

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

mode = max(frequency, key=frequency.get)

print(f"List of numbers: {numbers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
