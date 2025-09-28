from src.data.utils.validators import *

def test_validation():
    print("Testing validators")
    #runs simple examples of inputs that could be possible to check if the functions work properly

    assert validate_symbol("LST") == True
    assert validate_symbol("lst") == False
    assert validate_symbol(int("5")) == False

    #validate_candle(open_price, high, low, close, volume)
    assert validate_candle(150, 170, 120, 125, 14442) == True
    assert validate_candle(150, 120, 170, 120, 15564) == False #checks for low < high flag
    assert validate_candle(170, 150, 120, 125, 6152) == False #checks open_price > high flag
    assert validate_candle(150, 170, 120, 125, -5) == False #checks negative flag

    #validate_timestamp(ts)
    assert validate_timestamp("2019-01-02T00:00:00.000+04:00") == True
    assert validate_timestamp("1880-01-02T00:00:00.000Z") == False
    assert validate_timestamp("2030-01-02T00:00:00.000Z") == False
    assert validate_timestamp("2019-13-15T00:00:00.000Z") == False
    assert validate_timestamp("2019-02-31T00:00:00.000Z") == False
    assert validate_timestamp(" ") == False
    assert validate_timestamp(1) == False
    assert validate_timestamp(None) == False
    assert validate_timestamp("2019-02-10T21") == False