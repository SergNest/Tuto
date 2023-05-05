# width = 5
# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num ** 2, num ** 3))


# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    list = []
    count = 1
    for key, values in students.items():
      list.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(str(count), key, values, grades.get(values)))
      count += 1
    return list

print(formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}))

[' 1|Nick | A | 5 ', ' 2|Olga | B | 5 ', ' 3|Boris | FX | 2 ', ' 4|Anna | C | 4 ']
[' 1|Nick | A | 5 ', ' 2|Olga | B | 5 ', ' 3|Boris | FX | 2 ', ' 4|Anna | C | 4 ']