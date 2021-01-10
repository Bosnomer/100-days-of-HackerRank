# Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    keys_list = list(student_marks)
    value_list = list(student_marks.values())
    
    index = keys_list.index(query_name)
    add = sum(value_list[index])
    print("{:.2f}".format(add/3))
