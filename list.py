# Program using 2 list, where list A will multiply itself and transfer its value to list B.
a = list(map(int, input("Enter list a: ").split()))
print("List a: ", a)

b = []
 
for num1, num2 in zip(a, a):
    b.append(num1*num2)
 
print('b result is: ', b) 
