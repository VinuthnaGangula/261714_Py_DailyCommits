# To find average of a given student up to 2 decimal points.
# Input the name and scores into a dictionary.

if __name__ == "__main__":
    n = int(input("Enter n: "))
    student_marks = {}
    for i in range(n):
        name, *line = input("Enter name and scores " + str(i+1) + ": ").split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter name of student: ")
    avg = ((student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2]) / 3.00)
    avg = "{:.2f}".format(avg)
    print(avg)

# Sample Input

# Enter n: 3
# Enter name and scores 1: Krishna 67 68 69
# Enter name and scores 2: Arjun 70 98 63
# Enter name and scores 3: Malika 52 56 60
# Enter name of student: Malika

# Output

# 56.00
