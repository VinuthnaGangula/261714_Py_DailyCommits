# Count the number of occurrences of a substring in a given string.

def count_substring(string_in, sub_string_in):
    count_out = 0
    fnd = string_in.find(sub_string_in)
    while fnd != -1:
        count_out += 1
        fnd = string.find(sub_string_in, fnd + 1)
    return count_out


if __name__ == '__main__':
    string = input("Enter the string: ").strip()
    sub_string = input("Enter the substring: ").strip()

    count = count_substring(string, sub_string)
    print(count)

# Sample Input
# Enter the string: ABCDCDC
# Enter the substring: CDC
# Output
# 2
