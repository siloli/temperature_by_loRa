import struct,temp,time
def add_cayenne_payload(channel=1):
    payload=bytes()
    """
    conversion au format Cayenne LPP : https://developers.mydevices.com/cayenne/docs/lora/#lora-cayenne-low-power-payload-overview
    Uplink Payload Structure
    1 Byte 	1 Byte 	N Bytes 	1 Byte 	1 Byte 	M Bytes 	…
    Data1 Ch. 	Data1 Type 	Data1 	Data2 Ch. 	Data2 Type 	Data2 	…
    Temperature Sensor 	3303 	103 	67 	2 	0.1 °C Signed MSB
    """
    # conversion en entier signé
    tempC=temp.temperature()
    time.sleep(1)
    temperature = int(tempC * 10) # precision de 0.1 pour temp
    payload = (payload +bytes([channel]) +bytes([103]) +struct.pack('>l', temperature)[2:4])
    print(payload)
    return(payload)
