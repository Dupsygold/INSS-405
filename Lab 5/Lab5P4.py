def collect():

    temperature = int(input("Enter temperature:"))
    print(detector(temperature))

def detector (temperature):
        if temperature <30:
            print("temperatuer is cold")
        elif temperature <40:
            print("temperature is warm")
        elif temperature >40:
            print("temperature is hot")
collect()