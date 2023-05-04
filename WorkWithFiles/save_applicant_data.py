def save_applicant_data(source, output):
    textwithoutnum = ''

    for el in source:
        textwithoutnum += el.get('name')+',' + str(el.get('specialty'))+',' + str(
            el.get('math'))+',' + str(el.get('lang'))+',' + str(el.get('eng')) + '\n'

    with open(output, 'w') as fhoutput:
        fhoutput.write(textwithoutnum)


print(save_applicant_data([
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
], 'WorkWithFiles/output.txt'))
