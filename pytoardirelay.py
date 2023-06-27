import time

import serial

#The following line is for serial over GPIO
port = '/dev/ttyS0'


ard = serial.Serial(port,9600,timeout=5)

i = 0

while (i < 4):
    # Serial write section

    setTempCar1 = 63
    setTempCar2 = 37
    ard.flush()
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print ("Python value sent: ")
    print (setTemp1)
    ard.write(setTemp1)
    time.sleep(4)

    # Serial read section
    msg = ard.readline()
    print ("Message from arduino: ")
    print (msg)
    i = i + 1
else:
    print("Exiting")
exit()