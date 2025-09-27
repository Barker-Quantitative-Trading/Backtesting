from src.data.utils.validators import *

def main():
    print("Testing validators")
    #runs simple examples of inputs that could be possible to check if the functions work properly

    if validate_symbol("LST") == True:
        print("Validated")
    else:
        print("Incorrect")
    if validate_symbol("lst") == False:
        print("Validated")
    else:
        print("Incorrect")
    if validate_symbol(int("5")) == False:
        print("Validated")
    else:
        print("Incorrect")

    print("validate_candle tests")
    
    #validate_candle(open_price, high, low, close, volume)
    if validate_candle(150, 170, 120, 125, 14442) == True:
        print("Validated")
    else:
        print("Incorrect")
    if validate_candle(150, 120, 170, 120, 15564) == False: #checks for low < high flag
        print("Validated")
    else:
        print("Incorrect")
    if validate_candle(170, 150, 120, 125, 6152) == False: #checks open_price > high flag
        print("Validated")
    else:
        print("Incorrect")
    if validate_candle(150, 170, 120, 125, -5) == False: #checks negative flag
        print("Validated")
    else:
        print("Incorrect")

    if validate_timestamp("2019-01-02T00:00:00.000Z") == True:
        print("Validated")
    else:
        print("Incorrect")
    if validate_timestamp("1880-01-02T00:00:00.000Z") == False:
        print("Validated")
    else:
        print("Incorrect")
    if validate_timestamp("2030-01-02T00:00:00.000Z") == False:
        print("Validated")
    else:
        print("Incorrect")
    if validate_timestamp("2019-13-15T00:00:00.000Z") == False:
        print("Validated")
    else:
        print("Incorrect")
    if validate_timestamp("2019-02-31T00:00:00.000Z") == False:
        print("Validated")
    else:
        print("Incorrect")
    
    print("End of test")

    

if __name__ == "__main__":
    main()