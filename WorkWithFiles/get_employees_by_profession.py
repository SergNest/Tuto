def get_employees_by_profession(path, profession):
    lnewlist = []
    
    with open(path, 'r') as fh:
      alllines = fh.readlines()
      for el in alllines:
        if el.find(profession) > 0:
            lnewlist.append(el.replace('\n', ''))

    lretstring = ' '.join(lnewlist).replace(profession,'').strip()
        
    return lretstring



print(get_employees_by_profession('WorkWithFiles\output.txt', 'cook'))