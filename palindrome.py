x = input("Enter something")
def palindrome(x):
    if x == x[::-1]:
        return("This is a palindrome!")
    else:
        return("This isn't a palindrome!")
print(palindrome(x))