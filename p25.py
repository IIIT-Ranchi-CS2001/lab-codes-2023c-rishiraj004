customer_names = [f"Customer{i}" for i in range(1, 6)] 
customer_ids = [f"ID{i:03}" for i in range(1, 6)]
shopping_points = [100, 150, 200, 250, 300] 
customers_zip = list(zip(customer_names, customer_ids, shopping_points))
customers_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
print("With zip():", customers_zip)
print("Without zip():", customers_manual)