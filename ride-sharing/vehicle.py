class Vehicle:
    id = 0
    def __init__(self, v_type, number, capacity):
        Vehicle.id += 1
        self.id = Vehicle.id
        self.__type = v_type
        self.__number = number
        self.__capacity = capacity

    def get_vehicle_number(self):
        return self.__number

    def get_vehicle_type(self):
        return self.__type

    def get_vehicle_capacity(self):
        return self.__capacity