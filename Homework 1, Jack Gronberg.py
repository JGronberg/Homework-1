def hawkID():
    return("JGronberg")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    tripHours = distanceK/((vehSpeedMPS*18)/5)
    tripHoursTemp = tripHours
    dinners,lunches,breakfast = 0,0,0
    additionalReqs = 0
    gasCost = gasCostPerLiter*(distanceK/vehKPL)
    if(tripHours<4):
        lunches = 0
        hotelNights = 0
        totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
        return tripHours, gasCost, totalCost, breakfast, lunches, dinners, hotelNights
    if(tripHours==8):
        hotelNights = 0
        dinners = 0
        breakfast = 0
        lunches = 1
        totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
        return tripHours, gasCost, totalCost, breakfast, lunches, dinners, hotelNights
    hotelNights = (int)(tripHours/8)
    if(tripHours%8==0):
        hotelNights=hotelNights-1
    while(tripHoursTemp>40):
        breakfast = (int)(tripHours/8)+1
        lunches = (int)(tripHours/8)+1
        dinners = (int)(tripHours/8)+1
        additionalReqs+=1
        breakfast = breakfast + additionalReqs+1
        lunches+=additionalReqs+1
        dinners+=additionalReqs+1
        tripHoursTemp = tripHoursTemp-40
    breakfast = (int)(tripHours/8)
    lunches = (int)(tripHours/8)
    dinners = (int)(tripHours/8)
    totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
    return tripHours, gasCost, totalCost, breakfast, lunches, dinners, hotelNights

def printTripSummary(vehName, distanceM, vehSpeedMPH, vehMPG, gasCostPerGallon, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    tripHours, gasCost, totalCost, breakfast, lunches, dinners, hotelNights = computeTripData(distanceM*1.609, vehSpeedMPH*1.609,vehMPG/2.352, gasCostPerGallon/3.78541, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight)
    outputString = f"{vehName} trip of {distanceM}  miles. Hotel nights: {hotelNights}, Total Cost: ${totalCost:.2f}"
    print(outputString)

#i know that it's not finished, just didn't allocate enough time going to change that for the next assignment though.
#the formatting is all finished just the math isn't all the way there yet. I just don't want to be handing in any late assignments

