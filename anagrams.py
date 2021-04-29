# To check if the two strings are anagrams or not.

s1 = input("Enter first sentence: ").lower().replace(" ", "")
s2 = input('Enter second sentence: ').lower().replace(" ", "")

s1 = "".join(sorted(s1))
s2 = "".join(sorted(s2))
if s1 == s2:
    print("Anagrams")
else:
    print('Not anagrams')


# Sample Input
# Enter first sentence: Listen
# Enter second sentence: Silent
# Output
# Anagrams
