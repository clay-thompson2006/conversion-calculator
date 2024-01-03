    #functions for the exchange formulas

    def C_to_F(initial_temp):
        converted_temp = initial_temp * (9/5) +32
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    def C_to_K(initial_temp):
        converted_temp = initial_temp +273.15
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    def F_to_C(initial_temp):
        converted_temp = (initial_temp - 32) * (5/9)
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    def F_to_K(initial_temp):
        converted_temp =  (initial_temp - 32) * (5/9) + 273.15 
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    def K_to_C(initial_temp):
        converted_temp = initial_temp -273.15
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    def K_to_F(initial_temp):
        converted_temp = (initial_temp - 273.15) * 1.8 + 3278
        printed_temp = math.ceil(converted_temp*pow(10,2))/pow(10,2)
        print(printed_temp)
        file.write(f"Starter temp: {initial_temp} {temp} Converted to: {printed_temp} {new_temp} \n")
        file.close()
    #the if else statements to use the functions
    if temp == "F" or "f" and new_temp == "C" or "c":
        F_to_C(initial_temp)
    elif temp == "F" or "f" and new_temp == "K" or "k":
        F_to_K(initial_temp)
    elif temp == "C" or "c" and new_temp == "F" or "f":
        C_to_F(initial_temp)
    elif temp == "C" or "c" and new_temp == "K" or "k":
        C_to_K(initial_temp)
    elif temp == "K" or "k" and new_temp == "F" or "f":
        K_to_F(initial_temp)
    elif temp == "K" or "k" and new_temp == "C" or "c":
        K_to_C(initial_temp)
    else :
        print("you have something wrong please read through the prompt for each step and try again")
    #a rerun command to ask if you want to convert more things
    rerun = input("Would you like to put in a new temperature? Y for yes or N for no: ")
    if rerun == "Y":
        conversion_calculator()
    else:
        print("thanks for using the Conversion calculator")
start = conversion_calculator()
file.close()
