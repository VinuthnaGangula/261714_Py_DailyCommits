# To print all permutations of the coordinates of a cuboid [i, j, k] where (i + j + k) != n
# Where i <= x, j <= y, k <= z

if __name__ == "__main__":
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    n = int(input("Enter n: "))

    final_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(final_list)

# Sample Input
# Enter x: 1
# Enter y: 1
# Enter z: 1
# Enter n: 2
# Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
