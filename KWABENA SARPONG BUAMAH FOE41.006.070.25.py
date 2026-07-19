class SmartDevice:
    def __init__(self,name,device_id,power_status):
        self.name = name
        self.__device_id = device_id
        self.__power_status = power_status

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, actual_id):
        if actual_id == "":
            print("Please enter a valid Device ID")

        else:
            self.__device_id = actual_id

    @property
    def power_status(self):
        return self.__power_status

    @power_status.setter
    def power_status(self, value):
        self.__power_status = value

    def turn_on(self):
        self.__power_status = True
        print(f"Turning on {self.name} \n{self.name} is now on")

    def turn_off(self):
        self.__power_status = False
        print(f"Turning off {self.name} \n{self.name} is now off")

    def display_info(self):
        print(f"Name : {self.name} \nDevice ID : {self.device_id}")
        if self.power_status:
            print(f"Power Status : ON")
        else:
            print(f"Power Status : OFF ")

class TemperatureSensor(SmartDevice):
    def __init__(self,name,device_id,power_status,temperature):
        super().__init__(name,device_id,power_status)
        self.temperature = temperature

    def read_temperature(self):
        if self.power_status:
            print(f"The temperature on {self.name} is {self.temperature}°C")
        else:
            print(f"{self.name} is off ")

class SecurityCamera(SmartDevice):
    def __init__(self,name,device_id,power_status,recording_status):
        super().__init__(name, device_id, power_status)
        self.recording_status = recording_status

    def display_info(self):
        super().display_info()
        print("Recording_status : ","ON" if {self.recording_status} else "OFF")

    def start_recording(self):
        if self.power_status:
            self.recording_status = True
            print(f"{self.name} is now recording video")
        else:
            print(f"Cannot record because {self.name} is powered off")



    def stop_recording(self):
        if self.power_status:
            self.recording_status = False
            print(f"{self.name} has stopped the recording")
        else:
            print(f"The camera is off so it was not recording")



class SmartLight(SmartDevice):
    def __init__(self,name,device_id,power_status,brightness):
        super().__init__(name, device_id, power_status)
        self.brightness = brightness

    def increase_brightness(self,amount):
        if 0< amount <100:
            print(f"{self.name}'s brightness is being increased")
            if self.power_status:
                self.brightness = self.brightness + amount
                if self.brightness > 100:
                    self.brightness = 100
                    print(f"Max brightness reached: {self.brightness}")
                else:
                    print(f"New brightness level: {self.brightness}")
            else:
                print(f"Turn on {self.name}")
        else:
            print(f"Please input a value from 1 to 99")

    def decrease_brightness(self,amount):
        if 0< amount <100:
            print(f"Lowering brightness for {self.name}")
            if self.power_status:
                self.brightness = self.brightness - amount
                if self.brightness < 0:
                    self.brightness = 0
                    print("Brightness is 0, the light is practically off")
                else:
                    print(f"Brightness dropped to {self.brightness}")
            else:
                print(f"Turn on {self.name}")
        else:
            print(f"Enter a number between 1 and 99")



t_sensor = TemperatureSensor("Room Sensor", 101, True, 24)
room_light = SmartLight("Living Room Light", 102, True, 75)
front_camera = SecurityCamera("Front Door Camera", 103, True, True)

print("--- Smart Home Control Panel ---")

is_running = True

while is_running:
    print("=== MAIN MENU ===")
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")

    try:
        option = int(input("Select an option (1-7): "))
    except ValueError:
        print("That is not a valid number")
        print("Please pick a number between 1 and 7")
        continue



    if option == 1:
        t_sensor.display_info()
        room_light.display_info()
        front_camera.display_info()

    elif option == 2:
        print("Select a device to turn ON:")
        print("1. Thermometer 2. Light 3. Camera")
        device_option = int(input("Choose an option(1-3): "))

        if device_option == 1:
            t_sensor.turn_on()
        elif device_option == 2:
            room_light.turn_on()
        elif device_option == 3:
            front_camera.turn_on()
        else:
            print("Invalid option")

    elif option == 3:
        print("Select a device to turn OFF:")
        print("1. Thermostat 2. Light 3. Camera")
        device_option = int(input("Choose an option(1-3): "))

        if device_option == 1:
            t_sensor.turn_off()
        elif device_option == 2:
            room_light.turn_off()
        elif device_option == 3:
            front_camera.turn_off()
        else:
            print("Wrong selection")

    elif option == 4:
        t_sensor.read_temperature()

    elif option == 5:
        print("Would you like to turn brightness up or down?")
        print("1. Increase Brightness 2. Decrease Brightness")

        brightness_option = int(input("Pick 1 or 2: "))
        amount = int(input("By how much? "))
        if brightness_option == 1:
            room_light.increase_brightness(amount)
        elif brightness_option == 2:
            room_light.decrease_brightness(amount)
        else:
            print("Invalid option")

    elif option == 6:
        rec_option = str(input("Begin recording now? (Yes/No): "))
        if rec_option.capitalize() == "Yes":
            front_camera.start_recording()

    elif option == 7:
        is_running = False
        print("Exiting system. Goodbye!")

    else:
        print("Error: Option out of range")
        print("Please enter 1, 2, 3, 4, 5, 6, or 7")
