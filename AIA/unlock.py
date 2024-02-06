import RPi.GPIO as GPIO
import time

# GPIO pin assignments (adjust these based on your setup)
red_led = 8
green_led = 10
buzzer = 12
relay = 16

# Set GPIO mode 
GPIO.setmode(GPIO.BOARD)

# initialize pins
GPIO.setup(red_led, GPIO.OUT, initial=GPIO.HIGH)  # Red LED on by default
GPIO.setup(green_led, GPIO.OUT, initial=GPIO.LOW)  # Green LED off by default
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)  # Buzzer off by default
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)  # Relay off by default

def change_state():
    """Changes the state of the components for 5 seconds."""
    
    # Switch LED states
    GPIO.output(red_led, GPIO.LOW)
    GPIO.output(green_led, GPIO.HIGH)
    
    # Turn on relay
    GPIO.output(relay, GPIO.HIGH)

    # Turn on buzzer for 2 seconds
    GPIO.output(buzzer, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer, GPIO.LOW)
    

    
    # Wait for 2 seconds
    time.sleep(1)
    
    # Revert to default state
    GPIO.output(red_led, GPIO.HIGH)
    GPIO.output(green_led, GPIO.LOW)
    GPIO.output(relay, GPIO.LOW)

def clean_gpio():
    GPIO.cleanup()