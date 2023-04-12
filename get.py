def get_grade(key):
    lang = {"F": 1,
            "FX": 2,
            "E": 3,
            "D": 3,
            "C": 4,
            "B": 5,
            "A": 5}
    return lang.get(key)  


def get_description(key):
    lang = {"F": "Unsatisfactorily",
            "FX": "Unsatisfactorily", 
            "E": "Unsatisfactorily", 
            "D": "Enough", 
            "C": "Satisfactorily", 
            "B": "Very good", 
            "A": "Perfectly"}
    return lang.get(key) 