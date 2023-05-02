def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for emp in employee_list:
        if  isinstance(emp, str):
          fh.write(emp + '\n') 
        else:
           for el in emp:
             fh.write(el + '\n')    
    fh.close()
    
print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],'WorkWithFiles/test.txt'))