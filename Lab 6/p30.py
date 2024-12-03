input_string = input("Enter a comma-separated string: ")
components = [comp.strip() for comp in input_string.split(',')]

# 1. Find all letters and convert them to uppercase
letters_uppercase = list(
    map(lambda x: x.upper(), filter(lambda x: x.isalpha(), components))
)
print("Uppercase letters:", letters_uppercase)

# 2. Find all digits and compute their squares
digits_squared = list(
    map(lambda x: int(x) ** 2, filter(lambda x: x.isdigit(), components))
)
print("Squared digits:", digits_squared)

# 3. Display all alphanumeric characters
alphanumeric = list(filter(lambda x: x.isalnum(), components))
print("Alphanumeric characters:", alphanumeric)
