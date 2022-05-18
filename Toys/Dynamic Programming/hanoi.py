"Hanoi"

import time

to = time.time()

def hanoi(plate_number,x_set,y_set,z_set):
    "Definition of Hanoi"
    if plate_number == 1:
        print(x_set, "=>", z_set)               #   Output the movement from X to Z with Y
    else:
        hanoi(plate_number-1,x_set,z_set,y_set)     #   move the top plates from X to Y with Z
        hanoi(1,x_set,y_set,z_set)                  #   move the last plate from X to Z with Y
        hanoi(plate_number-1,y_set,x_set,z_set)     #   move the top plates from Y to Z with X

n = int(input("Please input the number of oder. \n"))
hanoi(n,"1st Pin","2nd Pin","3rd Pin")

td = time.time() - to
print("The time interval is %f s." %td)
