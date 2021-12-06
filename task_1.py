import numpy as np

for i in range(0, 5):
    a = input()
    num = np.random.randint(0, 37)
    if num == 0:
        print("green")
    elif num % 2 == 0:
        print("red")
    else:
        print("black")