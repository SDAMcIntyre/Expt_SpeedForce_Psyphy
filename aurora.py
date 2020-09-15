import serial

port = 'COM6' # check in "device manager"/"enhetshanteraren" which com port the trigger box is
baudrate = 1200 # according to trigger box documentation

triggerBox = serial.Serial(port, baudrate, timeout = 0.5) # set up the triger box object

# construct a command according to trigger box documentation
# example, send an ongoing 5 Volt signal on analog output number 3
commandNumber = 2 # 1 = digital, 2 = analog
analogOutput = 5 # channel number labelled on box; 4 = single protocol, 5 = protocol within sequence
outputLevel = 50 # voltage is level/10 (min = 0, max = 50)
time1 = 0 # on forever
time2 = 0 # on forever
command = bytearray(['S',commandNumber, analogOutput, outputLevel, time1, time2])

# send the command to the triger box
triggerBox.write(command)
