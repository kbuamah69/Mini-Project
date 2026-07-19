# Smart Home Control Panel

## About this project

This is a Python program I made for practice with Object-Oriented Programming (OOP). It simulates a simple smart home system where you can control three types of devices through a text menu: a temperature sensor, a smart light, and a security camera.

The main goal of this project was to practice:
- **Classes and objects**
- **Inheritance** (creating child classes from a parent class)
- **Encapsulation** (using private attributes with getters and setters)
- **Polymorphism** (overriding a method in a child class)

## How the program is structured

### Parent class: `SmartDevice`
This is the base class that all devices share. It stores information every smart device needs:
- `name` – the device's name
- `device_id` – a private attribute with a getter and setter (the setter checks that the ID is not empty)
- `power_status` – a private attribute with a getter and setter (True/False for on/off)

It also has these methods:
- `turn_on()` – turns the device on
- `turn_off()` – turns the device off
- `display_info()` – shows the device's name, ID, and power status

### Child class: `TemperatureSensor`
Inherits from `SmartDevice` and adds:
- `temperature` – stores the current temperature
- `read_temperature()` – prints the temperature, but only if the device is on

### Child class: `SmartLight`
Inherits from `SmartDevice` and adds:
- `brightness` – stores the brightness level (0–100)
- `increase_brightness(amount)` – raises the brightness, but won't go above 100
- `decrease_brightness(amount)` – lowers the brightness, but won't go below 0
- Both methods only work if the light is turned on, and only accept amounts between 1 and 99

### Child class: `SecurityCamera`
Inherits from `SmartDevice` and adds:
- `recording_status` – True/False for whether it's recording
- `start_recording()` – starts recording, only if the camera is on
- `stop_recording()` – stops recording, only if the camera is on
- `display_info()` – this is an **overridden** method (an example of polymorphism); it calls the parent's `display_info()` using `super()` and then also prints the recording status

## The devices in the program

When the program starts, it automatically creates three devices:

| Device Name | Type | ID | Starting Power | Extra Detail |
|---|---|---|---|---|
| Room Sensor | TemperatureSensor | 101 | ON | 24°C |
| Living Room Light | SmartLight | 102 | ON | 75% brightness |
| Front Door Camera | SecurityCamera | 103 | ON | Recording |

## Menu options

The program runs in a loop and keeps showing this menu until the user chooses to exit:

```
=== MAIN MENU ===
1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit
```

- Option 1 shows info for all three devices
- Options 2 and 3 ask which device you want to turn on/off
- Option 4 reads the temperature from the sensor
- Option 5 lets you increase or decrease the light's brightness
- Option 6 asks for confirmation before starting the camera recording
- Option 7 exits the program

The program also checks for invalid input, like typing a letter instead of a number, using a `try/except` block.

## How to run the program

1. Make sure Python 3 is installed on your computer.
2. Open a terminal in the project folder.
3. Run:
   ```bash
   python smart_home.py
   ```
4. Type a number from 1–7 to choose an option and follow the prompts.

## Example run

```
=== MAIN MENU ===
1. Display Device Information
2. Turn Device On
3. Turn Device Off
4. Read Temperature
5. Adjust Brightness
6. Start Recording
7. Exit
Select an option (1-7): 4
The temperature on Room Sensor is 24°C
```

## What I learned / limitations

While making this, I learned how to use inheritance to avoid repeating code across classes, and how encapsulation with getters/setters can be used to control access to private attributes. One thing I'd improve in the future is adding more input validation, since the program currently only handles invalid input for the main menu and would crash if a letter was typed for some of the other prompts (like choosing a device number).
