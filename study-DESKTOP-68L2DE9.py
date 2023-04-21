def game(terra, power):
    
    for lists in terra:
        for it in lists:
            if it <= power:
                power += it
            else:
                break
    return power


print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))