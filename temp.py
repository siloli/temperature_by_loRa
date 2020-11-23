from libraries.SI7006A20 import SI7006A20
from libraries.pysense import Pysense
def temperature():
    py = Pysense()
    si = SI7006A20(py)
    temp=si.temperature()
    del si
    del py
    print(temp)
    return temp
