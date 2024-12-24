from machine import Pin, PWM
from time import sleep

# Initialize PWM on GPIO 16
pwm = PWM(Pin(16))
pwm.freq(50)  # Standard frequency for servos is 50Hz

def set_servo_speed(duty):
    """
    Set the servo speed.
    For a continuous rotation servo:
    - duty < 7500: one direction (faster as it decreases)
    - duty > 7500: other direction (faster as it increases)
    - duty ~7500: stop
    """
    pwm.duty_u16(duty)

try:
    while True:
        # Example: gradually increase speed in one direction
        for duty in range(6000, 9000, 100):
            set_servo_speed(duty)
            sleep(0.1)
        
        # Stop the servo
        set_servo_speed(7500)
        sleep(1)
        
        # Gradually increase speed in the other direction
        for duty in range(9000, 6000, -100):
            set_servo_speed(duty)
            sleep(0.1)
        
        # Stop the servo
        set_servo_speed(7500)
        sleep(1)

except KeyboardInterrupt:
    # Stop PWM on exit
    pwm.deinit()
    print("PWM stopped.")