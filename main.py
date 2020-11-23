from network import LoRa
import socket,time,ubinascii,pycom
import add_payload


pycom.heartbeat(False)

lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters, change them to the provided credentials
app_eui = ubinascii.unhexlify('70B3D57ED00381E0')
app_key = ubinascii.unhexlify('D7B6DCFF4ADC8729299BCAE1C78895D7')
#uncomment to use LoRaWAN application provided dev_eui
#dev_eui = ubinascii.unhexlify('70B3D549938EA1EE')

# join a network using OTAA (Over the Air Activation)
#uncomment below to use LoRaWAN application provided dev_eui
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(3)
    print('Not yet joined...')

print('Joined')
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)



# send some data
while True:
    # make the socket blocking
    # (waits for the data to be sent and for the 2 receive windows to expire)
    s.setblocking(True)
    s.send(add_payload.add_cayenne_payload())
    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)
    # get any data received (if any...)
    time.sleep(60)
    data = s.recv(64)
    print(data)
