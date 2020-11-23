from SI7006A20 import SI7006A20
from pysense import Pysense
def temperature():
    py = Pysense()
    si = SI7006A20(py)
    temp=si.temperature()
    print(temp)
    return temp
