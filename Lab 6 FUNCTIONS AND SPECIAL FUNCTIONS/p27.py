def my_zip(*args, strct=True):
    if strct:
        # Ensure all lists have the same length
        lengths = [len(lst) for lst in args]
        if len(set(lengths)) != 1:
            raise ValueError("All lists must be of the same length when 'strct' is True.")
        return list(zip(*args))
    else:
        # Zip using the minimum length
        min_length = min(len(lst) for lst in args)
        return [tuple(lst[i] for lst in args) for i in range(min_length)]

customer_name = ['Alice', 'Bob', 'Charlie']
customer_id = [101, 102, 103]
shopping_points = [500, 400, 300]

# Strict zipping
print(my_zip(customer_name, customer_id, shopping_points, strct=True))

# Lenient zipping
customer_name = ['Alice', 'Bob']
print(my_zip(customer_name, customer_id, shopping_points, strct=False))
