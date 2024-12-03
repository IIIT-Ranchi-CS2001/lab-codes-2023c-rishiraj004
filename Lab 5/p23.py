point1 = (float(input("Enter the x-coordinate of point 1: ")), float(input("Enter the y-coordinate of point 1: ")))
point2 = (float(input("Enter the x-coordinate of point 2: ")), float(input("Enter the y-coordinate of point 2: ")))
x1, y1 = point1
x2, y2 = point2
if (y1 - y2) != 0: 
    m = (x1 - x2) / (y1 - y2)
else:
    m = float('inf') 
line_equation = f"(x - {x1}) = {m} * (y - {y1})"

print(line_equation)