#!/usr/bin/env pybricks-micropython

import sys
from time import sleep

# `hubs` module: https://pybricks.com/ev3-micropython/hubs.html
from pybricks.hubs import EV3Brick
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

from app import App

ev3brick = EV3Brick()


def main():
    ev3brick.speaker.beep()
    ev3brick.screen.clear()
    ev3brick.screen.print("Voltage is: {}".format(ev3brick.battery.voltage()))
    ev3brick.speaker.say("Bootin up")
    ev3brick.screen.print("Bootin' up . . .")
    sleep(1)

    test_app = App(name="test_app")

    test_app.run()
    test_app.end()
    # test_motor = Motor(Port.B)
    # test_motor.run_target(500, 90)

    # ev3brick.speaker.beep(frequency=1000, duration=500)


if __name__ == "__main__":
    main()

    # while callable(ev3brick.buttons) and not ev3brick.buttons():
    #     sleep(10)
