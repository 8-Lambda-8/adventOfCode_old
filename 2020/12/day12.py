import time
import math


def run(part, path):
    with open(path, 'r') as file:
        inputFile = file.read()
        inputFile = inputFile[:-1]
        inputArray = inputFile.split('\n')
        # inputArray.remove("")
    startTime = time.time()

    angle = 0
    position = [0, 0]

    if part == 1:
        for line in inputArray:
            if line[0] == "N":
                position[1] += int(line[1:])
            elif line[0] == "S":
                position[1] -= int(line[1:])
            elif line[0] == "E":
                position[0] += int(line[1:])
            elif line[0] == "W":
                position[0] -= int(line[1:])
            elif line[0] == "L":
                angle += int(line[1:])
            elif line[0] == "R":
                angle -= int(line[1:])
            elif line[0] == "F":
                position[0] += int(math.cos(math.radians(angle)) * int(line[1:]))
                position[1] += int(math.sin(math.radians(angle)) * int(line[1:]))
            print(position)
        solution = abs(position[0]) + abs(position[1])
        print("Solution:", solution)

    waypoint = [10, 1]

    if part == 2:
        for line in inputArray:
            if line[0] == "N":
                waypoint[1] += int(line[1:])
            elif line[0] == "S":
                waypoint[1] -= int(line[1:])
            elif line[0] == "E":
                waypoint[0] += int(line[1:])
            elif line[0] == "W":
                waypoint[0] -= int(line[1:])
            elif line[0] == "L":
                waypoint = rotateWaypoint(waypoint, int(line[1:]))
            elif line[0] == "R":
                waypoint = rotateWaypoint(waypoint, -int(line[1:]))
            elif line[0] == "F":
                position[0] += int(int(line[1:]) * waypoint[0])
                position[1] += int(int(line[1:]) * waypoint[1])

            print(position, waypoint)
        solution = abs(position[0]) + abs(position[1])
        print("Solution:", solution)

    print("calculating Time: ", (time.time() - startTime))


# def rotateWaypoint(wp, angle):
#
#     if not wp[0] == 0:
#         waypointAngle = math.degrees(math.atan(wp[1] / (wp[0])))
#         print(waypointAngle)
#     else:
#         if wp[1] > 0:
#             waypointAngle = 90
#         else:
#             waypointAngle = -90
#
#     waypointAngle += angle
#
#     H = math.sqrt(wp[0] * wp[0] + wp[1] * wp[1])
#     print(waypointAngle, H)
#     wp[0] = round(math.cos(math.radians(waypointAngle)) * H)
#     wp[1] = round(math.sin(math.radians(waypointAngle)) * H)
#     return wp

def rotateWaypoint(waypoint, angle):
    print(waypoint, angle)
    if angle < 0:
        angle = 360+angle

    if angle > 360:
        angle - int(angle/360)*360

    if angle == 90:
        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif angle == 180:
        waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
    elif angle == 270:
        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    print(waypoint)
    return waypoint
