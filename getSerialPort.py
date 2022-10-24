import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInts = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input("Silahkan Pilih Portnya: COM")

for x in range(0,len(portList)):
    if portList[x].startswith("COM" + str(val)):
        portOzzy = "COM" + str(val)
        print(portList[x])

serialInts.baudrate = 9600
serialInts.port = portOzzy
serialInts.open()

while True:
    if serialInts.in_waiting:
        packet = serialInts.readline()
        print(packet.decode('utf').rstrip('\n'))