x = input("Enter season number:")
def season(x):
    if 3 <= int(x) <=5:
        return("Spring")
    if 6 <= int(x) <= 8:
        return("Summer")
    if 9 <= int(x) <= 11:
        return("Autumn")
    if 1 <= int(x) <= 2:
        return("Winter")
    if int(x)== 12:
        return("Winter")
print(season(x))