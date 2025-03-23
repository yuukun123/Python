from flashLamp import flashLamp
from battery import battery

def Test_flashLamp(flashLamp, battery):
    pin = battery()
    print(f"Original power battery: {pin.getEnergy()}")
    pin.decreaseEnergy()
    print(f"Power battery after confining 2 units: {pin.getEnergy()}")
    pin.setEnergy(5)
    print(f"Power battery after set it to {pin.getEnergy()}: {pin.getEnergy()}")
    print()

    flashLamp = flashLamp()
    print(f"FlashLamp is on: {flashLamp.isOn()}")
    print(f"FlashLamp is battery: {flashLamp.getBattery().getEnergy()}")
    flashLamp.turnOn()
    print(f"FlashLamp is on: {flashLamp.isOn()}")
    print(f"FlashLamp is battery: {flashLamp.getBattery().getEnergy()}")
    flashLamp.turnOff()
    print(f"FlashLamp is on: {flashLamp.isOn()}")
    print()

    empty_battery = battery()
    empty_battery.setEnergy(0)
    flashLamp.setBattery(empty_battery)
    print(f"FlashLamp is battery: {flashLamp.getBattery().getEnergy()}")
    flashLamp.turnOn()
    print(f"FlashLamp is on: {flashLamp.isOn()}")

if __name__ == '__main__':
    Test_flashLamp(flashLamp, battery)