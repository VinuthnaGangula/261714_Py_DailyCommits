# Python code that asks a user how many pizza slices they want.The pizzeria charges Rs 123.00 a slice.
# If user order even number of slices, price per slice is Rs 120.00.
# Print the total price depending on how many slices user orders.

n = int(input("Enter no. of pizza slices: "))
price = 0.0
if n % 2 == 0:
    price = n * 120.0
else:
    price = n * 123.0

print("Total price: " + str(price))


# Sample Input
# Enter no. of pizza slices: 2

# Output
# Total price: 240.0
