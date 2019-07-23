import time
from djitellopy import Tello

drone = Tello()

# plot lawn with 1, house with 2. Each element represents a 40 by 40 cm area.
plot = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 2, 0, 0]]


def findHouse():
    for r in plot:
        for c in r:
            if c == 2:
                return[plot.index(r), r.index(c)]


prevPos = findHouse()

drone.connect()
time.sleep(5)
drone.takeoff()
time.sleep(5)
drone.move_up(40)
time.sleep(5)

for r in plot:
    for c in r:
        if c == 1:
            x = (plot.index(r) - prevPos[0]) * 40
            y = (r.index(c) - prevPos[1]) * 40
            drone.go_xyz_speed(x, y, 0, 20)
            time.sleep(5)
            prevPos = [plot.index(r), r.index(c)]
            r[r.index(c)] = 0

time.sleep(3)
x = (findHouse()[0] - prevPos[0]) * 40
y = (findHouse()[1] - prevPos[1]) * 40
drone.go_xyz_speed(x, y, 0, 20)
time.sleep(3)
drone.land()

