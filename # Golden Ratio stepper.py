# Golden Ratio stepper

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def ratio_calc(num):
    num = float(num)
    counter = 1
    while counter < 6:
        print(f"{counter} step(s) up is {num*1.618*counter}.")
        counter += 1
    counter = 1
    while counter < 6:
        print(f"{counter} step(s) down is {num/(1.618*counter)}.")
        counter += 1
        

while True:

    number = input("Enter the base number, or 'q' to quit. ")
    
    if number.lower() == "q":
        print("Goodbye pal!")
        exit()
    
    while not is_number(number):
        number = input("That was not a valid number. Enter the base number, or 'q' to quit. ")
        if number.lower() == "q":
            print("Goodbye pal!")
            exit()
    
    ratio_calc(number)