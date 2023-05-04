def sanitize_file(source, output):
    textwithoutnum = ''
    with open(source, 'r') as fh:
        all_file = fh.read()
        for el in all_file:
            try:
                num = int(el)        
            except:
                textwithoutnum += el

        with open(output, 'w') as fhoutput:
           fhoutput.write(textwithoutnum)

print(sanitize_file('WorkWithFiles/test.txt', 'WorkWithFiles/output.txt'))