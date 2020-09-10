#! /usr/bin/env python


def dump_class_keys(some_class, skip_none=True):
    from types import ModuleType, FunctionType, MethodType

    for key in dir(some_class):
        if "__" in key:
            continue

        attr = getattr(some_class, key)
        if attr is None:
            if not skip_none:
                print("#", key, " - None #")
        elif isinstance(attr, ModuleType):
            print("#", key, " - ", str(type(attr)), "#")
        elif isinstance(attr, FunctionType):
            print("#", key, " - ", str(type(attr)), "#")
        elif isinstance(attr, MethodType):
            print("#", key, " - ", str(type(attr)), "#")
        else:
            print("#", key, " - ", str(type(attr)), ": ", attr, "#")


def get_joystick_input(dev_dir = '/dev/input/by-id/'):
    import os

    for tree_id, tree in enumerate(os.walk(dev_dir)):
        for branch_id, branch in enumerate(tree):
            if branch_id == 0:
                continue
            for leaf_id, leaf in enumerate(branch):
                if 'event' in leaf and 'joystick' in leaf:
                    return f'{dev_dir}{leaf}'

    raise Exception('No joystick found')


def blank_screen():
    from PIL import Image
    img = Image.new("RGB", (1280, 720))
    pixels = img.load()
    for i in range(0, 1280):
        for j in range(0, 720):
            pixels[i, j] = (0, 0, 0)
    img.show('title')


def pygame_check_screens():
    import pygame
    d_num = pygame.display.get_num_displays()

    print(d_num)


def main(device_path):
    from evdev import InputDevice, categorize, ecodes
    
    gamepad = InputDevice(device_path)

    print(gamepad)

    for event in gamepad.read_loop():
        if event.code == 0:
            continue
        input_event = categorize(event)

        keycode = None
        if hasattr(input_event, 'keycode'):
            keycode = input_event.keycode
            print(f'Keycode: {keycode}')

        print(f'{event.code} {event.type}: {event.value}')
        # dump_class_keys(event)
        # print('')
        # print('############')
        # print('')

        # dump_class_keys(input_event)
        # print('')
        # print('############')
        # print('')
    
    return 0


if __name__ == '__main__':
    device_path = get_joystick_input()
    main(device_path)
