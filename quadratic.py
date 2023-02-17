a = int(input("Enter 'a' value:"))
b = int(input("Enter 'b' value:"))
c = int(input("Enter 'c' value:"))

root1 = (-b + (b*b - 4*a*c)**0.5) / (2*a)
root2 = (-b - (b*b - 4*a*c)**0.5) / (2*a)


print(root1)
print(root2)