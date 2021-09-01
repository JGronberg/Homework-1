def hawkID():
    return("01466779")

def computeTripData(distanceK, vehSpeedMPS, vehKPL, gasCostPerLiter, breakfastCostPerDay, lunchCostPerDay, dinnerCostPerDay, hotelCostPerNight):
    tripHours = distanceK/vehSpeedMPS
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
   # if(tripHours%40==0):
    #  breakfast = (int)(tripHours/8)*
    #    lunches = (int)(tripHours/8)
    #  dinners = (int)(tripHours/8)
    #    if(tripHours>40):
    #       hotelNights += (int)(tripHours/40)
    #    additionalReqs = (int)(tripHours/40)
    #    breakfast+=additionalReqs
    #    lunches+=additionalReqs
    #    dinners+=additionalReqs
    breakfast = (int)(tripHours/8)
    lunches = (int)(tripHours/8)
    dinners = (int)(tripHours/8)
    totalCost = (breakfast*breakfastCostPerDay)+(lunches*lunchCostPerDay)+(dinners*dinnerCostPerDay)+(gasCost)
    return tripHours, gasCost, totalCost, breakfast, lunches, dinners, hotelNights
print("chicken")