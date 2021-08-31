def hawkID():
    return("01466779")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    tripHours = distanceK/vehSpeedMPS
    dinners,lunches,breakfast = 0,0,0
    gasCost = gasCostPerLiter*(distanceK/vehKPL)
    if(tripHours<4):
        lunches = 0
        totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
        return tripHours, gasCost, totalCost, breakfast, lunches, dinners
    if(tripHours==8):
        hotelNights = 0
        dinners = 0
        lunches = 1
    hotelNights = (int)(tripHours/8)      
    if(tripHours%40==0):
        hotelNights += (int)(tripHours/40)
        additionalReqs = (int)(tripHours/40)
        breakfast+=additionalReqs
        lunches+=additionalReqs
        dinners+=additionalReqs
    breakfast = (int)(tripHours/8)
    totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
    return tripHours, gasCost, totalCost, breakfast, lunches, dinners 
    print("pog")
    print("last commit")
    print("work on first try?")