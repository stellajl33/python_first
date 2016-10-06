#Fibonacci

array = [0,0,1]

for i in range(3,102,1):
    array.append(array[i-1]+array[i-2])

print array
