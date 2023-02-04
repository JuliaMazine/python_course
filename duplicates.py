x = input("Enter something")
def duplicates(x):
    if len(set(x)) == len(x):
        return("There are no duplicates!")
    else:
        return("There are duplicates!")
print(duplicates(x))