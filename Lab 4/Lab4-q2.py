# Hot = >= 50
# warm = 30 - 50
# cold = 0 - 30
# Extreme_cold = <0

Temperature = input("Temperature: ")
if(int(Temperature)) >= 50:
    print("Hot")
elif(int(Temperature) <=50 and int(Temperature) >=30):
    print("warm")
elif(int(Temperature) <=30 and int(Temperature)>= 0):
    print("cold")
else:
    print("Extreme cold")