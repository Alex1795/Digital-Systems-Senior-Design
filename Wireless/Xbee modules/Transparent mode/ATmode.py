import serial

st = "A"
serialPort = serial.Serial("/dev/ttyUSB0",9600,timeout = 2) #Open communication
                                                            #with the port
print"Opened"
while 1:
    try:
    
        b_sent = serialPort.write(st)                       #send the variable
                                                            # st to the serial port

        loop = serialPort.read()                            #Read from the
                                                            # buffer, in case something was received
        
        print "received:",loop                              #Print what was read
                                                            # from the buffer

    except IOError:
        print "We failed"                                   #In case something
                                                            #goes wrong, prints a line instead of crashing
