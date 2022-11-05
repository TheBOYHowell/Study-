# quadratic formula 

A=int(input('write A :'))
B=int(input('write B :'))
C=int(input('write C :'))


root1=(-B + ((B ** 2) - 4 * A * C)**0.5)/(2 * A)
root2=(-B - ((B ** 2) - 4 * A * C)**0.5)/(2 * A)

print(root1)
print(root2)