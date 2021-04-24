if __name__ == '__main__':
    s = input("Enter the string: ")

    for i in s:
        if i.isalpha() or i.isdigit():
            print("Alphanumeric : True")
            break
    else:
        print("Alphanumeric : False")

    for i in s:
        if i.isalpha():
            print("Alpha : True")
            break
    else:
        print("Alpha : False")

    for i in s:
        if i.isdigit():
            print("Numeric : True")
            break
    else:
        print("Numeric : False")

    for i in s:
        if i.islower():
            print("Lower case : True")
            break
    else:
        print("Lower case : False")

    for i in s:
        if i.isupper():
            print("Upper case : True")
            break
    else:
        print("Upper case : False")
