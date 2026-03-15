from turtlepoint import *
from mathexclusive import *
from math import *
import json

def export_qgc_plan(cords, altitude=50, filename="mission.plan"):

    items = []
    seq = 1

    for lat, lon in cords:
        items.append({
            "AMSLAltAboveTerrain": None,
            "Altitude": altitude,
            "AltitudeMode": 1,
            "autoContinue": True,
            "command": 16,
            "doJumpId": seq,
            "frame": 3,
            "params": [
                0,
                0,
                0,
                None,
                lat,
                lon,
                altitude
            ],
            "type": "SimpleItem"
        })
        seq += 1

    plan = {
        "fileType": "Plan",
        "groundStation": "QGroundControl",

        "geoFence": {
            "circles": [],
            "polygons": [],
            "version": 2
        },

        "rallyPoints": {
            "points": [],
            "version": 2
        },

        "mission": {
            "cruiseSpeed": 15,
            "firmwareType": 12,
            "hoverSpeed": 5,
            "items": items,
            "plannedHomePosition": [
                cords[0][0],
                cords[0][1],
                altitude
            ],
            "vehicleType": 2,
            "version": 2
        },

        "version": 1
    }

    with open(filename, "w") as f:
        json.dump(plan, f, indent=4)

    print("mission.plan oluşturuldu")


def startmission(p1, p2, radius=60, detail=5):

    setturtle()

    lat1, lon1 = p1
    lat2, lon2 = p2

    latit = 111320

    disty = haversine(lat1, lon1, lat2, lon1) * 1000
    distx = haversine(lat1, lon1, lat1, lon2) * 1000

    x1, y1 = 0, 0
    x2 = distx * (-1 if lat1 > lat2 else 1)
    y2 = disty * (-1 if lon1 > lon2 else 1)

    point(x1, y1)
    point(x2, y2)

    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2

    a = abs(x2 - x1) / 2
    b = radius

    cords = []

    t = 0

    while t < 2 * pi:

        x = cx + a * sin(t)
        y = cy + b * sin(t) * cos(t)

        point(x, y)

        lat = lat1 + x / latit
        lon = lon1 + y / latit

        cords.append((lat, lon))

        t += radians(detail)

    for c in cords:
        print(c)

    export_qgc_plan(cords)

    turtle.exitonclick()


startmission(
    (-35.363261, 149.165230),
    (-35.362800, 149.165900)
)