# To wrap a text into a paragraph of width w.

import textwrap


def wrap(s, w):
    return textwrap.fill(s, w)


if __name__ == '__main__':
    string, max_width = input("Enter text: "), int(input("Enter width: "))
    result = wrap(string, max_width)
    print(result)

# Sample Input
# Enter text: abracadabra
# Enter width: 3
# Output
# abr
# aca
# dab
# ra
