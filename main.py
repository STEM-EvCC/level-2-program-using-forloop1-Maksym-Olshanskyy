mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# Use a for loop to iterate through the list of missions.
# Count the total number of missions.
# Count the number of successful missions.
# Identify and list all missions launched before the year 2000.


# Prints a list in the form:
# [header]
# [prefix][item 0]
# [prefix][item 1]
# ...
def printList(list, header, prefix):
    print(header)
    for item in list:
        print(prefix + item)

numMissions = len(mission_names)
numSuccessMissions = 0
beforeY2K = []

for i in range(numMissions): # iterates from 0 to the length of mission_names
    if mission_success[i]: # if that particular mission succeded
        numSuccessMissions += 1 # increment successful missions by 1
    if mission_years[i] < 2000: # if that particular mission was before y2k
        beforeY2K.append(mission_names[i]) # add the mission name to beforey2k list

successRate = numSuccessMissions / numMissions * 100 # calculate successful mission %

print("Total number of missions: " + str(numMissions))
print("Number of successful missions: " + str(numSuccessMissions))
print("Success rate: {0:0.2f}".format(successRate) + "%") # format to trunkate decimal to 2 digits
printList(beforeY2K, "Missions launched before the year 2000:", "- ")