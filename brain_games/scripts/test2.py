def cylinder():
    r = float(input())
    h = float(input())

    side = 2 * 3.14 * r * h
  
    circle = 3.14 * r**2
  
    full = side + 2 * circle
    return full
 
square = cylinder()
print(square)