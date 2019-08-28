from sense_hat import SenseHat

sense = SenseHat()

r = [255, 0, 0]
g = [0, 255, 0]
b = [0, 0, 255]
w = [255,255,255]
z = [0, 0, 0]

redimage = [
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
r,r,r,r,r,r,r,r,
]

greenimage = [
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
w,w,w,w,w,w,w,w,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
g,g,g,g,g,g,g,g,
]

blueimage = [
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
w,w,w,w,w,w,w,w,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]

whiteimage = [
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
w,w,w,w,w,w,w,w,
]

sense.set_pixels(redimage)

while True:
    pitch, roll, yaw = sense.get_orientation().values()
#   print (pitch, roll, yaw)
    
    if (pitch < 3 or pitch > 355) and (yaw < 3 or yaw > 355):
        sense.set_pixels(whiteimage)
    elif pitch < 0.5 or pitch > 359.5:
        sense.set_pixels(greenimage)
    elif yaw < 5 or yaw > 355:
        sense.set_pixels(blueimage)
    else:
        sense.set_pixels(redimage)
