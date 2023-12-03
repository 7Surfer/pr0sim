import code

#performance
import time

import json
import copy

# Kampf
# Angreifer:
# LJ: 100000
# XER: 5000
# SS: 1000
# SXER: 1000
# z: 500
# RIP: 10
#Verteidiger
# LJ: 100000
# XER: 5000
# SS: 1000
# SXER: 1000
# z: 500
# RIP: 10

testset = {
    "attackers": [
        (
            0,{
                "player": {
                    "id": 1,
                    "military_tech": 15,
                    "defence_tech": 15,
                    "shield_tech": 15
                },
                "fleetDetail": {
                    "fleet_id": 0
                },
                "unit": {
                    204: 100000,
                    206: 5000,
                    207: 1000,
                    213: 500,
                    214: 10,
                    215: 1000
                }
            }
        )
    ],
    "defenders": [
        (
            1, {
                "player": {
                    "id": 7,
                    "military_tech": 10,
                    "defence_tech": 10,
                    "shield_tech": 10
                },
                "fleetDetail": {
                    "fleet_start_galaxy": 1
                },
                "unit": {
                    204: 100000,
                    206: 5000,
                    207: 1000,
                    213: 500,
                    214: 10,
                    215: 1000
                }
            }
        )
    ]
}

for test in range(1,11):
    fleetTF = 0
    defTF = 0
    
    testData = copy.deepcopy(testset)

    start_time = time.time()
    result = code.calculateAttack(testData["attackers"], testData["defenders"], fleetTF, defTF)
    print(f'--- Run {test}: {time.time() - start_time} seconds ---')
    