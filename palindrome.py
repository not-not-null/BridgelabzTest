

def palindrome():
    value = input("enter a string: ")
    lstRev = value[::-1]
    if value == lstRev:
        print("String is a palindrome")
        print(lstRev)
    else:
        print("String is not a palindrome")


palindrome()
