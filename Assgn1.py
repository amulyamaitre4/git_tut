x = int(input("Enter the number: "))

l = []
for i in range(1, x+1):
    if i % 3 == 0 and i % 5 == 0:
        l.insert(i,"FizzBuzz")
    elif i % 3 == 0:
        l.insert(i, "Fizz")
    elif i % 5 == 0:
        l.insert(i,"Buzz")
    else:
        l.insert(i, i)
print(l)