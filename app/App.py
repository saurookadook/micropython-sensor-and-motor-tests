from time import sleep

from pybricks.hubs import EV3Brick


class App:
    app_hub = None

    def __init__(self, name=""):
        self.name = name
        self.app_hub = EV3Brick()

    def run(self):
        self.app_hub.speaker.beep()
        self._print_and_say(text="BINGO BANGO!", text_to_say="Bingo Bango")
        sleep(2)
        self.app_hub.screen.print("LOOK AT THIS '{}' SHIT".format(self.name))

    def end(self):
        sleep(3)
        self._print_and_say(text="Bye forever!")
        sleep(1)

    def _print_and_say(self, text="", text_to_say="", clear_screen=True):
        if text != "" and text_to_say == "":
            text_to_say = text

        if text_to_say != "" and text == "":
            text = text_to_say

        if clear_screen:
            self.app_hub.screen.clear()

        self.app_hub.screen.print(text)
        self.app_hub.speaker.say(text_to_say)
