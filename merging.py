# Divide the string 's' of length 'n' into 'k' substrings. Convert the substrings obtained
# such that no repetitions occur in that particular substring and print them.

def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        t_str = string[i:(i + k)]
        out = set()
        for j in t_str:
            if j not in out:
                print(j, end='')
                out.add(j)
        print()


if __name__ == '__main__':
    string_in, k_in = input("Enter the string: "), int(input("Enter k: "))
    merge_the_tools(string_in, k_in)


# Sample Input
# Enter the string: AABCAAADA
# Enter k: 3
# Output
# AB
# CA
# AD
