import time
import serial      
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

          
file = open("/home/pi/test/data.csv","w").close()      
file = open("/home/pi/test/data.csv","a")


while(1):
	a=ser.readline()
	print a	
	file.write(a)


ser.write('30')
time.sleep(0.1)
ser.write('30')

time.sleep(10)
ser.write('0')
time.sleep(0.1)
ser.write('0')



