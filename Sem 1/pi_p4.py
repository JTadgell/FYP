import time
import serial      
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate = 57600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

          
      


ser.write('0')
time.sleep(0.1)
ser.write('0')

time.sleep(3)
ser.write('0')
time.sleep(0.1)
ser.write('0')



