class Car:
    def __init__(self,brand):
        self.brand=brand

    def get_brand(self):
        print(self.brand)

    def open_door(self, door_number):
        print ("Openeing door: ", str(door_number))

    def blinker_control (self, left_blinker="Off", right_blinker="Off"):
        if left_blinker=="On":
            self.left_blinker=left_blinker
            self.right_blinker= "Off"
        elif right_blinker=="On":
            self.left_blinker="Off"
            self.right_blinker= right_blinker
        print ("left: " +str(self.left_blinker) +" - Right: "+str(self.right_blinker))



class Truck(Car):
    def tow_car(self):
        print ("Towing Car")
