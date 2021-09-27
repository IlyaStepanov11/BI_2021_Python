number = float(input("Enter the value: "))
unit_1 = input("Which unit do you want it converted from (h, min, sec):  ")
unit_2 = input("Which unit do you want it converted to (h, min, sec): ")

if unit_1 == "h" and unit_2 == "min":
    result = float(number)*60
    
elif unit_1 == "h" and unit_2 == "sec":
    result = float(number)*3600
    
elif unit_1 == "min" and unit_2 == "h": 
    result = float(number)/60
    
elif unit_1 == "min" and unit_2 == "sec":
    result = float(number)*60
    
elif unit_1 == "sec" and unit_2 == "h":
    result = float(number)/3600
    
elif unit_1 == "sec" and unit_2 == "min":
    result = float(number)/60

print (result)

