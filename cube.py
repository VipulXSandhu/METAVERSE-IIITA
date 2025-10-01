from vpython import *

scene.background = color.black

cube = box(size=vector(2,2,2), color=color.red)

angle = 0
rotate_y = True

while True:
    rate(60)
    
    if rotate_y:
        cube.rotate(angle=0.02, axis=vector(0,1,0))
    else:
        cube.rotate(angle=0.02, axis=vector(1,0,0))
    
    if angle == 100:
        cube.color = vector(0.2,0.8,1)  # cyan
        scene.background = vector(0.96, 0.96, 0.86)

        rotate_y = False

    angle += 1