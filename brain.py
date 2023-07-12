import time

def brain(blood, heart):
    for life in range(-10, 0, 1):
        time.sleep(1.0)
        if life == 0:
            break
        print(life)
    while True:
        blood, heart = heart, blood
        time.sleep(1.0)
        print(blood, end=' ')
        time.sleep(0.1)
        print(heart)
        
brain(1, 0)
