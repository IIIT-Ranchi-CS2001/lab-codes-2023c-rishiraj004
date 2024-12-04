singers = {"Drake", "Kylie", "Travis", "Sunidhi"}
dancers = {"Michael Jackson", "Sarah", "David", "Jane"}

# Perform set operations
all_students = singers | dancers  # Union of singers and dancers
only_singers = singers - dancers  # Singers who are not dancers
only_dancers = dancers - singers  # Dancers who are not singers
common_students = singers & dancers  # Students who are both singers and dancers

# Print the results
print("All students:", all_students)
print("Only singers:", only_singers)
print("Only dancers:", only_dancers)
print("Common students:", common_students)