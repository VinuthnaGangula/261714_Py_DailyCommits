# To check if a string is palindrome or not

s = input("Enter the string: ")

s = s.lower().replace(" ", "")
n = len(s)
first_half = s[:(n // 2)]
sec_half = s[:(n // 2 - 1):-1]
if first_half == sec_half:
    print("It's a palindrome")
else:
    print("It's not a palindrome")


# Sample Input
# Enter the string: palindrome
# Output
# It's not a palindrome
