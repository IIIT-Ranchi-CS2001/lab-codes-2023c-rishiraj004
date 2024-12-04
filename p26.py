customer_names = [f"Customer{i}" for i in range(1, 6)]
customer_ids = [f"ID{i:03}" for i in range(1, 6)]
shopping_points = [100, 150, 200, 250, 300]
customers_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
sorted_customers = sorted(customers_manual, key=lambda x: x[2])
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j][2] > lst[j+1][2]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
manually_sorted_customers = bubble_sort(customers_manual.copy())
print("Sorted using sorted():", sorted_customers)
print("Sorted without using sorted (bubble sort):", manually_sorted_customers)