import shapes
print("1.Circle")
print("2.Rectabgle")
print("3.Triangle")
choice = int(input("Enter your choice:"))
if choice ==1:
    radius = float(input("Enter radius"))
    print("Areanof circle",shapes.circle_area(radius))
if choice ==2:
    length = float(input("Enter a number"))
    width = float(input("Enter a number"))
    print("Area of rectangle",shapes.rectangle_area(length,width))
if choice ==3:
    base = float(input("Enter a number"))
    height = float(input("Enter a number"))
print("Area of triangle",shapes.triangle_area(base,height))