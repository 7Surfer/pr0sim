from cleanup import *

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
    "attackers": {
        0: {
            "name": "attacker", #for testing
            "military_tech": 15,
            "defence_tech": 15,
            "shield_tech": 15,
            "unit": {
                204: 100000,
                206: 5000,
                207: 1000,
                213: 500,
                214: 10,
                215: 1000
            }
        }
    },
    "defenders": {
        0: {
            "name": "deffer", #for testing
            "military_tech": 15,
            "defence_tech": 15,
            "shield_tech": 15,
            "unit": {
                204: 100000,
                206: 5000,
                207: 1000,
                213: 500,
                214: 10,
                215: 1000
            }
        }
    }
}


times = []
#for test in range(1,11):
for test in range(1,11):
    fleetTF = 0
    defTF = 0
    
    testData = copy.deepcopy(testset)

    start_time = time.time()
    result = run(testData["attackers"], testData["defenders"])
    currentRuntime = time.time() - start_time
    times.append(currentRuntime)
    print(f'--- Run {test}: {time.time() - start_time} seconds ---')


averrage = sum(times) / len(times)
print(f'--- Averrage over {len(times)} tests: {averrage} seconds ---')