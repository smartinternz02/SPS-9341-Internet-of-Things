#SmartParkingSystem
#There are two types of vehicles - 4 wheeler, 2 wheeler;


import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import json

#Provide your IBM Watson Device Credentials
organization = "on9ox0"
deviceType = "SmartParkingSystem"
deviceId = "D6D9G2H1"
authMethod = "token"
authToken = "123456789"
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

   
class FourWheeler:
    def __init__(self):
        self.ID=" "
        self.Time=" " # in Hours
        self.charge=" "
    def parkinginfo(self):
        self.ID=input("Enter the ID of the parking space:")
        self.Time=int(input("How long are you staying?? (Enter time in hours)"))
    def charges(self):
        self.charge=self.Time*50 #Say per hr charge is 50 rupees for 4 wheeler
    def displayCharges(self):
        print("You stayed for", self.Time, "hrs!")
        print("Please pay:",self.charge)
        print("--------------------------------------------------------------------------------------------------------")
    def displayStatus(self):
        print("Vehicle_ID:",self.ID)
        print("Waiting_Time:",self.Time,"hrs")
        print("--------------------------------------------------------------------------------------------------------------")




class TwoWheeler:
    def __init__(self):
        self.ID=" "
        self.Time=" "# in Hours
        self.charge=" "
    def parkinginfo(self):
        self.ID=input("Enter the ID of the parking space:")
        self.Time=int(input("How long are you staying?? (Enter time in hours)"))
    def charges(self):
        self.charge=self.Time*30 #Say per hr charge is 30 rupees for 2 wheeler
    def displayCharges(self):
        print("You stayed for", self.Time, "hrs!")
        print("Please pay:",self.charge)
        print("--------------------------------------------------------------------------------------------------------")
    def displayStatus(self):
        print("Vehicle_ID:",self.ID)
        print("Waiting_Time:",self.Time,"hrs")
        print("--------------------------------------------------------------------------------------------------------------")

        
Four_wheeler_parking_lot=[]
Two_wheeler_parking_lot=[]
ch='Y'
while(ch=='Y'):
    print("1. Park Four Wheeler..\n2. Park Two Wheeler..\n3. Check Four Wheeler status..\n4. Check Two Wheeler status..\n5. Exit..")
    choice=int(input("What do you want to do???"))
    if(choice==1):
        Fourwheel= FourWheeler()
        Fourwheel.parkinginfo()
        Fourwheel.charges()
        Fourwheel.displayCharges()
        Four_wheeler_parking_lot.append(Fourwheel)
        

    elif(choice==2):
        Twowheel= TwoWheeler()
        Twowheel.parkinginfo()
        Twowheel.charges()
        Twowheel.displayCharges()
        Two_wheeler_parking_lot.append(Twowheel)


    elif(choice==3):
        print("*********VEHICLES IN FOUR WHEELER PARKING LOT*****************")
        print("--------------------------------------------------------------------------------------------------------------")
        for i in Four_wheeler_parking_lot:
            i.displayStatus()

    elif(choice==4):
        print("*********VEHICLES IN TWO WHEELER PARKING LOT*****************")
        print("--------------------------------------------------------------------------------------------------------------")
        for i in Two_wheeler_parking_lot:
            i.displayStatus()

    else:
        print("Exit")

    ID="04_001"
    Time="4hrs"
    charge=4*50
    data = {"d":{ 'Parking Space ID' : ID, 'Waiting Time': Time,'Pay Charge': charge }}
        #print data
    def myOnPublishCallback():
        print ("Parking Space ID = %s C" % ID, "Waiting Time = %s %%" % Time,"Please pay:%d hrs" %charge,"to IBM Watson")

    success = deviceCli.publishEvent("Data", "json", data, qos=0, on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IoTF")
    time.sleep(1)  
        
    
deviceCli.disconnect()    
