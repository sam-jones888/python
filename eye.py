import math

def brain(light, eye, see):
    x = light + eye
    see += x
    s = see * 2
    if s > 0:
        s == light
    else:
        light == False
    return s
    
brain(math.pi, 1, 0)
