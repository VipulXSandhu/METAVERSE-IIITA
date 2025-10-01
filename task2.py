from vpython import *

scene = canvas(title="Interactive World", width=800, height=600, center=vector(0,1,0), background=color.cyan)

ground = box(pos=vector(0,0,0), size=vector(20,0.5,20), color=color.green)
player = box(pos=vector(0,1,0), size=vector(1,2,1), color=color.blue)
door = box(pos=vector(5,2,0), size=vector(2,4,0.2), color=color.red)

door_open = False
speed = 0.2
keys = {"w":False, "a":False, "s":False, "d":False}

def keydown(evt):
    global door_open
    if evt.key in keys:
        keys[evt.key] = True
    if evt.key == "e":
        if mag(player.pos - door.pos) < 3:
            if not door_open:
                door.pos.z += 2
                door.color = color.green
                door_open = True
            else:
                door.pos.z -= 2
                door.color = color.red
                door_open = False

def keyup(evt):
    if evt.key in keys:
        keys[evt.key] = False

scene.bind("keydown", keydown)
scene.bind("keyup", keyup)

while True:
    rate(60)
    if keys["w"]:
        player.pos.z -= speed
    if keys["s"]:
        player.pos.z += speed
    if keys["a"]:
        player.pos.x -= speed
    if keys["d"]:
        player.pos.x += speed