import time
x = input("Enter your birthday like so: 00.00.0000")
print(round((time.time() - time.mktime(time.strptime(x,'%d.%m.%Y')))/86400))
