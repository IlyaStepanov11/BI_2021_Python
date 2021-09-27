number = float(input("Enter the value: "))
unit1 = input("Which unit do you want it converted from (hour, min, sec):  ")
unit2 = input("Which unit do you want it converted to (hour, min, sec): ")


if unit1 == "sec" and unit2 == "hour":
    result = float(number)/36
    
elif unit1 == "sec" and unit2 == "min":
    result = float(number)/60 
    
elif unit1 == "min" and unit2 == "hour": 
    result = float(number)/60
    
elif unit1 == "min" and unit2 == "sec":
    result = float(number)*60
    
elif unit1 == "hour" and unit2 == "min":
    result = float(number)*60
    
elif unit1 == "hour" and unit2 == "sec":
    result = float(number)*3600

print (result)

