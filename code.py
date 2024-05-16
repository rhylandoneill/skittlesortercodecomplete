import time
import board
import pwmio
import busio
import adafruit_tcs34725
from adafruit_motor import servo
from adafruit_motor import motor

pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)
my_servo_1 = servo.Servo(pwm1)

sensor_integration_time = 150

sensor_gain = 4

num_samples = 5

i2c = busio.I2C(board.GP5, board.GP4)
sensor = adafruit_tcs34725.TCS34725(i2c)

sensor.gain = sensor_gain

sensor.integration_time = sensor_integration_time

while True:

    my_servo.angle = 0
    my_servo_1.angle = 90
    time.sleep(2)
    my_servo.angle = 90

    time.sleep(1)

    print(sensor.color_rgb_bytes)
    red = sensor.color_rgb_bytes[0]
    green = sensor.color_rgb_bytes[1]
    blue = sensor.color_rgb_bytes[2]
    lux = sensor.lux
    temp = sensor.color_temperature
    print(red,green,blue,lux,temp)
    print("Temperature: %d" % sensor.color_temperature)
    print(
        "r: %d, g: %d, b: %d"
        % (
            sensor.color_rgb_bytes[0],
            sensor.color_rgb_bytes[1],
            sensor.color_rgb_bytes[2],
        )
    )

    print("Lux: %d" % sensor.lux)
    if red < 90 and red > 65 and green < 9 and green > 3 and lux < 220 and lux > 160 and temp > 2200 and temp < 2650:
        print ("red detected")
        my_servo_1.angle = 30
    if red > 75 and red < 87 and green < 8 and green > 3 and lux > 220 and lux < 340 and temp > 2100 and temp < 2400:
        print ("orange detected")
        my_servo_1.angle = 60
    if red > 58 and red < 70 and green < 13 and green > 8 and lux > 370 and lux < 550 and temp > 2200 and temp < 2450:
        print ("yellow detected")
        my_servo_1.angle = 90
    if red > 27 and red < 36 and green < 25 and green > 17 and lux > 250 and lux < 350 and temp > 2850 and temp < 3150:
        print ("green detected")
        my_servo_1.angle = 120
    if red > 38 and red < 46 and green < 16 and green > 11 and lux > 135 and lux < 200 and temp > 2800 and temp < 3120:
        print ("purple detected")
        my_servo_1.angle = 150
    else:
        print("nothing detected")
    time.sleep(2)

    my_servo.angle = 180
    time.sleep(2)

'''
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        my_servo.angle = angle
        time.sleep(0.05)
'''
