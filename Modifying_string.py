# To change a character of a string at a given position.

def modify_string(s, pos, ch):
    list_ = list(s)
    list_[pos] = ch
    return "".join(list_)


if __name__ == "__main__":
    s = input("Enter the string: ")
    pos = int(input("Enter position: "))
    ch = input("Enter the character: ")
    print(modify_string(s, pos, ch))

# Sample Input
# Enter the string: modify
# Enter position: 2
# Enter the character: f
# Output
# mofify
