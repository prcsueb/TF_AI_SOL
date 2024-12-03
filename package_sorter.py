def sort(width, height, length, mass):
    # vol Calc
    volume = width * height * length
    
    # if bulk
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    
    # if heavy
    heavy = mass >= 20
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

print(sort(100, 100, 100, 10))
print(sort(200, 100, 50, 30))
print(sort(200, 200, 200, 30))
print(sort(50, 50, 50, 5))
print(sort(160, 50, 50, 10))
