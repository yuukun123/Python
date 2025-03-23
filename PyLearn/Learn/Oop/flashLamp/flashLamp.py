from battery import battery

class flashLamp:
    def __init__(self, status = False, __battery = 0):
        self.__status = status
        self.__battery = battery()

    def setBattery(self, battery):
        self.__battery = battery

    def getBattery(self):
        return self.__battery

    def isOn(self):
        return self.__status

    def isBattery(self):
        return self.__battery.getEnergy() > 0

    def turnOn(self):
        if self.isBattery():
            self.__status = True
            print("Turn on")
            self.__battery.decreaseEnergy()

    def turnOff(self):
        self.__status = False
        print("Turn off")


