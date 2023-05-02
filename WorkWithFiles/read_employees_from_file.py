def read_employees_from_file(path):
    emp_list = []
    fh = open(path, 'r')
    while True:       
      line = fh.readline()
      if not line:
        break
      emp_list.append(line.replace('\n',''))
    fh.close()
    return emp_list

print(read_employees_from_file('WorkWithFiles/test.txt'))