def manage_salaries():
    employees = {}
    for i in range(5):
        name = input(f"Enter the name of employee {i+1}: ")
        salary = float(input(f"Enter the salary of {name}: "))
        employees[name] = salary
    employee_list = [(name, salary) for name, salary in employees.items()]
    for i in range(len(employee_list)):
        for j in range(0, len(employee_list) - i - 1):
            if employee_list[j][1] < employee_list[j + 1][1]:
                employee_list[j], employee_list[j + 1] = employee_list[j + 1], employee_list[j]
    print("\nEmployees sorted by salary (highest first):")
    for rank, (name, salary) in enumerate(employee_list, start=1):
        print(f"Rank {rank}: {name}, Salary: {salary}")
manage_salaries()