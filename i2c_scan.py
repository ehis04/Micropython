#https://github.com/robert-hh/BME280
import machine
import time
from bme280 import BME280

i2c = machine.I2C(0, scl=machine.Pin(17), sda=machine.Pin(16))

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:  
    print("Decimal address: ",device," | Hexa address: ",hex(device))
    
bme280 = BME280(i2c=i2c)
while True:
    print(bme280.values)
    time.sleep(1)