import math

#starter variables with user imput
def conversion_calculator():
    initial_temp = input("What is the temperature: ")
    temp = input("Is it celcius or farenheit. input C for celcius, F for farenheit, or K for kelvin: ")
    new_temp = input("What would you like to change it to. F for farenheit, C for celcius, or K for kelvin: ")
    initial_temp = int(initial_temp)
    #functions for the exchange formulas

    def C_to_F(initial_temp):
        converted_temp = initial_temp * (9/5) +32
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    def C_to_K(initial_temp):
        converted_temp = initial_temp +273.15
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    def F_to_C(initial_temp):
        converted_temp = (initial_temp - 32) * (5/9)
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    def F_to_K(initial_temp):
        converted_temp =  (initial_temp - 32) * (5/9) + 273.15 
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    def K_to_C(initial_temp):
        converted_temp = initial_temp -273.15
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    def K_to_F(initial_temp):
        converted_temp = (initial_temp - 273.15) * 1.8 + 3278
        print(math.ceil(converted_temp*pow(10,2))/pow(10,2))
    #the if else statements to use the functions
    if temp == "F".lower() and new_temp == "C".lower():
        F_to_C(initial_temp)
    elif temp == "F".lower() and new_temp == "K".lower():
        F_to_K(initial_temp)
    elif temp == "C".lower() and new_temp == "F".lower():
        C_to_F(initial_temp)
    elif temp == "C".lower() and new_temp == "K".lower():
        C_to_K(initial_temp)
    elif temp == "K".lower() and new_temp == "F".lower():
        K_to_F(initial_temp)
    elif temp == "K".lower() and new_temp == "C".lower():
        K_to_C(initial_temp)
    else :
        print("you have something wrong please read through the prompt for each step and try again")
    #a rerun command to ask if you want to convert more things
    rerun = input("Would you like to put in a new temperature? Y for yes or N for no: ")
    if rerun == "Y".lower():
        conversion_calculator()
    else:
        print("thanks for using the Conversion calculator")
start = conversion_calculator()
