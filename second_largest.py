# To find the runner-up score from the list of given scores as input.

if __name__ == "__main__":
    n = int(input("Enter no. of scores: "))
    arr = list(map(int, input("Enter n scores separated by a space: ").split()))

    top_score = max(arr)
    arr = list(filter(lambda x: x != top_score, arr))
    runner_up_score = max(arr)
    print(runner_up_score)
