# To change uppercase letter to lowercase and vice-versa in a string.

def swap_case(st):
    return st.swapcase()


if __name__ == "__main__":
    s = input("Enter the string: ")
    res = swap_case(s)
    print(res)
