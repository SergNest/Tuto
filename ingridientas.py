def format_ingredients(items):
    new_line = ""
    if len(items) > 1:
        for it in items:          
            if it == items[-1:][0]:
                new_line += " and " + it
            elif it == items[-2:][0]:
                new_line += it
            else:
                new_line += it + ", "
        return new_line
    elif len(items) == 0:
       return ""
    else:
        return items[0]
    
print(format_ingredients(["2 eggs"]))