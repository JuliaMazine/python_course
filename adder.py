x = input("Enter a whole number")
def adder(x):
     xs = list(str(x))
     xls = [int(num) for num in xs]
     return sum(xls)
print(adder(x))