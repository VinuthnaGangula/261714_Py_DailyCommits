# To print hash value of tuple.

if __name__ == "__main__":
    n = int(input())
    list_ = map(int, input().split())
    t = tuple(list_)
    print(hash(t))
