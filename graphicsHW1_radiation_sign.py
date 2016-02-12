##Generates a PPM image

import math

f = open("output.ppm", "w")
f.write("P3\n500 500\n255\n")

p = []

#Generate solid-color 2D list for image
for x in range(500):
    l = []
    for y in range(500):
        l.append("255 255 0 ")
    p.append(l)

#define a circle in the format of [centerY, centerX, radius]
currCircle = [270, 290, 35]
isCurrBlack = False #if current circle is to be black

#Modify image
for i in range(9):
    for x in range(500):
        for y in range(500):
            if math.sqrt((x-currCircle[0])**2 + (y-currCircle[1])**2) < currCircle[2]:
                if isCurrBlack:
                    p[x][y] = "0 0 0 "
                else:
                    p[x][y] = "255 255 0 "
    isCurrBlack = not isCurrBlack #flip black and white
    currCircle[0] += 20
    currCircle[1] += 20
    currCircle[2] += 15

currCircle = [270, 210, 35]
isCurrBlack = False #if current circle is to be black

#Modify image
for i in range(9):
    for x in range(500):
        for y in range(500):
            if math.sqrt((x-currCircle[0])**2 + (y-currCircle[1])**2) < currCircle[2]:
                if isCurrBlack:
                    p[x][y] = "0 0 0 "
                else:
                    p[x][y] = "255 255 0 "
    isCurrBlack = not isCurrBlack #flip black and white
    currCircle[0] += 20
    currCircle[1] -= 20
    currCircle[2] += 15

currCircle = [212, 250, 35]
isCurrBlack = False #if current circle is to be black

#Modify image
for i in range(9):
    for x in range(500):
        for y in range(500):
            if math.sqrt((x-currCircle[0])**2 + (y-currCircle[1])**2) < currCircle[2]:
                if isCurrBlack:
                    p[x][y] = "0 0 0 "
                else:
                    p[x][y] = "255 255 0 "
    isCurrBlack = not isCurrBlack #flip black and white
    currCircle[0] -= 28
    currCircle[2] += 15

#Write to file
for x in range(500):
    for y in range(500):
        f.write(p[x][y])
f.close()