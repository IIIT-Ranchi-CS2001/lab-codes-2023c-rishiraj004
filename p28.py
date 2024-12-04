def my_sort(data, key):
    if not data or not isinstance(data[0], tuple):
        raise ValueError("Input data must be a list of tuples.")
    if key not in (0, 1, 2):
        raise ValueError("Key must be 0, 1, or 2.")
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

customer_data = [
    ('Charlie', 103, 300),
    ('Alice', 101, 500),
    ('Bob', 102, 400)
]

# Sort by customer name (key=0)
print(my_sort(customer_data[:], key=0))

# Sort by customer ID (key=1)
print(my_sort(customer_data[:], key=1))

# Sort by shopping points (key=2)
print(my_sort(customer_data[:], key=2))
