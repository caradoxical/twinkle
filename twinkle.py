import Jetson.GPIO as GPIO
import time

# Define GPIO pins used to toggle each LED color
LED_PINS = {"red":149,"green":194,"white":216}

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

def turn_on(color):
    if color not in LED_PINS:
        raise ValueError("LED color must be one of %r." % LED_PINS)
    else:
        GPIO.setup(LED_PINS(color), GPIO.OUT)
        GPIO.output(LED_PINS(color), GPIO.HIGH)

def turn_off(color):
    if color not in LED_PINS:
        raise ValueError("LED color must be one of %r." % LED_PINS)
    else:
        GPIO.setup(LED_PINS(color), GPIO.OUT)
        GPIO.output(LED_PINS(color), GPIO.LOW)

def pulse(color):
    if color not in LED_PINS:
        raise ValueError("LED color must be one of %r." % LED_PINS)
    else:
        GPIO.setup(LED_PINS(color), GPIO.OUT)
        GPIO.output(LED_PINS(color), GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(LED_PINS(color), GPIO.LOW)

# Test the module
if __name__ == '__main__':
    # Set the pin numbers
    led1 = "red"
    led2 = "green"
    led3 = "white"

    # Turn the pins on and off
    turn_on(led1)
    time.sleep(1)
    turn_off(led1)
    time.sleep(1)
    turn_on(led2)
    time.sleep(1)
    turn_off(led2)
    time.sleep(1)
    turn_on(led3)
    time.sleep(1)
    turn_off(led3)
    time.sleep(1)
    pulse(led1)
    time.sleep(1)
    pulse(led2)
    time.sleep(1)
    pulse(led3)
    
    # Clean up the GPIO pins
    GPIO.cleanup()
