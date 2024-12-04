def my_max(*args):
    if not args:
        raise ValueError("No arguments provided.")
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    
    return max_value
# List
numbers_list = [1, 4, 9, 3]
print("Max in list:", my_max(*numbers_list))  

# Set
numbers_set = {5, 8, 12, 7}
print("Max in set:", my_max(*numbers_set)) 

# Tuple
numbers_tuple = (10, 20, 15, 25)
print("Max in tuple:", my_max(*numbers_tuple)) 
