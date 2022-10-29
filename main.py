#!/usr/bin/env pybricks-micropython

import sys
from time import sleep

# `hubs` module: https://pybricks.com/ev3-micropython/hubs.html
try:
    from ev3dev2.display import Display
except Exception as e:
    print(("-" * 30) + " NOPETOWN for pybricks " + ("-" * 30))
    print(e)
    # raise e

from pybricks import ev3brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
)
from pybricks.parameters import (
    Port,
    Stop,
    Direction,
    Button,
    Color,
    SoundFile,
    ImageFile,
    Align,
)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from sensor_and_motor_tests import App

# from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
# from ev3dev2.sensor import INPUT_1
# from ev3dev2.sensor.lego import TouchSensor
# from ev3dev2.led import Leds

ev3brick.sound.beep()
ev3brick.display.clear()
ev3brick.display.text(f"Voltage is: {ev3brick.battery.voltage()}")

# while callable(ev3brick.buttons) and not ev3brick.buttons():
#     sleep(10)


if __name__ == "__main__":
    ev3brick.display.text("Bootin' up . . .")
    sleep(1)
    ev3brick.display.text("BINGO BANGO!")
    test_app = App(name="test_app", brick_device=ev3brick)
    sleep(2)
    test_app.run()
    sleep(10)
