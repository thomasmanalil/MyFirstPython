
from Vehicles.vehicles import Car

def sumOfTwo(a,b):
    return a+b

def sum_array(arr):
    return sum(arr)



def main():
    my_Car = Car("Toyota")
    my_Car.get_brand()
    my_Car.open_door(2)
    my_Car.blinker_control(left_blinker="On")
    my_Car.blinker_control(right_blinker="On")


if __name__ == '__main__':
    main()
