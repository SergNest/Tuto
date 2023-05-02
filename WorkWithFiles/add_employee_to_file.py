def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(record + '\n')    
    fh.close()
    
print(add_employee_to_file("Drake Mikelsson,19",'WorkWithFiles/test.txt'))