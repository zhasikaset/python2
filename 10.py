birthday = int(input("Input birthday: "))
month = input("Input month of birth (e.g. march, july etc): ")

if month == 'december':
    zodiac = 'Archer' if (birthday < 22) else 'Goat'
elif month == 'january':
    zodiac = 'Goat' if (birthday < 20) else 'Water Bearer'
elif month == 'february':
    zodiac = 'Water Bearer' if (birthday < 19) else 'Fish'
elif month == 'march':
    zodiac = 'Fish' if (birthday < 21) else 'Ram'
elif month == 'april':
    zodiac = 'Ram' if (birthday < 20) else 'Bull'
elif month == 'may':
    zodiac = 'Bull' if (birthday < 21) else 'Twins'
elif month == 'june':
    zodiac = 'Twins' if (birthday < 21) else 'Crab'
elif month == 'july':
    zodiac = 'Crab' if (birthday < 23) else 'Lion'
elif month == 'august':
    zodiac = 'Lion' if (birthday < 23) else 'Virgin'
elif month == 'september':
    zodiac = 'Virgin' if (birthday < 23) else 'Scales'
elif month == 'october': 
    zodiac = 'Scales' if (birthday < 23) else 'Scorpion'
elif month == 'november':
    zodiac = 'Scorpion' if (birthday < 22) else 'Archer'
   
print("Your Astrological sign is: {}".format(zodiac))




