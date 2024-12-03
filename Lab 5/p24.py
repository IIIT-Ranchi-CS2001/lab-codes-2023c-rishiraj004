def count_characters(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count
test_string = input("Enter a string: ")
char_count_result = count_characters(test_string)
for char, count in char_count_result.items():
    print(f"'{char}': {count}")