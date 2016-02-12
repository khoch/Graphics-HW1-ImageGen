import math
##Generates a PPM image

f = open("output.ppm", "w")
f.write("P3\n500 500\n255\n")

p = []

#Generate solid-color 2D list for image
for x in range(500):
    l = []
    for y in range(500):
        l.append("8 8 8 ")
    p.append(l)

#define a circle in the format of [centerY, centerX, radius]
currCircle = [250, 250, 280]
isCurrBlack = False #if current circle is to be black
#radchangefactor = 40
#poschangefactor = 40
changefactor = 15
whiteness = 61
darkness = 0

#Modify image
for i in range(17):
    for x in range(500):
        for y in range(500):
            if math.sqrt((x-currCircle[0])**2 + (y-currCircle[1])**2) < currCircle[2]:
                if isCurrBlack:
                    p[x][y] = "%s %s %s " % (darkness, darkness, darkness)
                else:
                    p[x][y] = "%s %s %s " % (whiteness, whiteness, whiteness)
    isCurrBlack = not isCurrBlack #flip black and white
    currCircle[0] += changefactor
    currCircle[1] += changefactor
    currCircle[2] *= 0.81
    #radchangefactor -=8
    #poschangefactor -=8
    changefactor *= 0.8
    if whiteness < 239:
        whiteness += 17
    darkness += 8


#Write to file
for x in range(500):
    for y in range(500):
        f.write(p[x][y])
f.close()