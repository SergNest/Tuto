def total_salary(path):
    total = 0.0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if not line:
          break
        ind = line.find(',')
        total += float(line[ind+1:].replace("/n",""))
    fh.close()
    return total

print(total_salary('WorkWithFiles/test.txt'))