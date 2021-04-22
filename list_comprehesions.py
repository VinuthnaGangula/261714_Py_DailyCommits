# To print all permutations of the coordinates of a cuboid [i, j, k] where (i + j + k) != n
# Where i <= x, j <= y, k <= z

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    final_list = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(final_list)
