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
def speed(x,y):
	ser.write(str(x))
	time.sleep(0.1)
	ser.write(str(y))
	return 0

def values(x,y,z):
	ser.write(str(x))
	time.sleep(0.1)
	ser.write(str(y))
	time.sleep(0.1)
	ser.write(str(z))
	return 0
def log():
	file.write('test')
	for i in range(2000):
		a=ser.readline()
		print a	
		file.write(a)

for i in range(-3,5):
	
	Kp=10**i
	Kd=0
	Ki=0
	file.write(Kp+'|'+Kd+'|'+Ki)
	time.sleep(0.1)
	ser.write('1')#kp update
	time.sleep(0.1)
	values(Kp,Kd,Ki)
	time.sleep(0.1)
	ser.write('3')#step_response
	time.sleep(0.1)
	ser.write('6400')
	time.sleep(0.1)
	ser.write('6400')
	log()
	ser.write('a')
	time.sleep(0.1)
	ser.write('0')
	time.sleep(4)
	i=i+1



