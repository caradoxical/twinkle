# twinkle

Python module for playing with an RGW LED hat made for the Jetson Nano and Raspberry Pi.

## How to Use
### NVIDIA Jetson
1. pip install `Jetson.GPIO`
2. Follow the setup instructions on https://github.com/NVIDIA/jetson-gpio
3. Save this script on your Jetson device
4. Test it out by running `sudo python3 twinkle.py`
5. Import it into other Python scripts to access functions
6. When you're done using this module, make sure to run `GPIO.cleanup()` to safely reset GPIO pins to low.

## Functions
* `turn_on(color)` Turns an LED on
* `turn_off(color)` Turns an LED off
* `pulse(color)` Pulses an LED for 0.1s
These functions accept the values: "red", "green", and "white"