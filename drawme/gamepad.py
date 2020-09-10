#! /usr/bin/env python


class Gamepad:
    def __init__(self):

        from tools import get_joystick_input
        from evdev import InputDevice

        jpad = get_joystick_input()
        self.gamepad = InputDevice(jpad)
        # print(self.gamepad)

        self.on_a_btn = None
        self.on_b_btn = None
        self.on_y_btn = None
        self.on_x_btn = None
        self.left_analog = None

    def bind_left_analog(self, callback):
        pass

    def bind_a_button(self, callback):
        self.on_a_btn = callback

    def bind_b_button(self, callback):
        self.on_b_btn = callback

    def bind_y_button(self, callback):
        self.on_y_btn = callback

    def bind_x_button(self, callback):
        self.on_x_btn = callback

    def handle_event(self, event, debug=False):
        from evdev import categorize, ecodes

        if event.code == 0:
            return
        input_event = categorize(event)

        keycode = None
        if hasattr(input_event, "keycode"):
            keycode = input_event.keycode
            debug and print(f"Keycode: {keycode}")

        # Run A button if hooked up
        if event.code == 304 and event.type == 1:
            if self.on_a_btn is not None:
                debug and print(" # Running A btn callback #")
                self.on_a_btn(event.value)

        # Run B button if hooked up
        if event.code == 305 and event.type == 1:
            if self.on_b_btn is not None:
                debug and print(" # Running B btn callback #")
                self.on_b_btn(event.value)
        
        # Run X button if hooked up
        if event.code == 307 and event.type == 1:
            if self.on_x_btn is not None:
                debug and print(" # Running X btn callback #")
                self.on_x_btn(event.value)
        
        # Run Y button if hooked up
        if event.code == 308 and event.type == 1:
            if self.on_y_btn is not None:
                debug and print(" # Running Y btn callback #")
                self.on_y_btn(event.value)
        
        debug and print(f"{event.code} {event.type}: {event.value}")

    def process(self, debug=False):
        gen = self.gamepad.read()
        try:
            for event in gen:
                self.handle_event(event, debug)
        except IOError:
            pass

    def process_loop(self, debug=False):
        for event in self.gamepad.read_loop():
            self.handle_event(event, debug)


def test_print_callback(value):
    value_str = "Enabled" if value else "Disabled"
    print(f"# callback ran succesfully - Value: {value_str}! #")
    return 0


if __name__ == "__main__":
    # Quick test of gamepad
    xbone = Gamepad()
    xbone.bind_a_button(test_print_callback)
    xbone.process_loop()
