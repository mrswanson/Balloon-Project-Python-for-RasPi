# there are 11 variables
import serial

data_file = open('home/pi/weatherData.txt', 'w')


ser = serial.Serial('/dev/ttyUSB0', 9600)

while 1 :
    serInput = ser.readline()
    # print serInput
    x  = len(serInput)
    print "/n" 
    #print x
    y=  serInput.split()
    data_file.write(x)
    print y 
    for z in range(0, 12):
        print [z]
        
        
        
