import pynput
import sys
import os


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


if len(sys.argv) < 2:
    eprint('No source file was specified')

    exit(1)

fileName = sys.argv[1]

f = None

if not os.path.exists(fileName):
    eprint('Source file not found')

    exit(1)

f = open(fileName, 'r');

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

for c, i in enumerate(f.readlines()):
    temp = i.strip().split(' ')

    if temp[0] == '':
        continue

    if len(temp) < 2:
        eprint('Line %d: arguments must be more than 2' % (c + 1))

    command = temp[0]
    arguments = temp[1:]

    if command == 'move':
        if len(arguments) < 3:
            eprint('Line %d: argument is invalid' % (c + 1))

            exit(1)

        if not(any(map(str.isdigit, arguments[1])) and any(map(str.isdigit, arguments[1]))):
            eprint('Line %d: arguments are not numeric', (c + 1))

            exit(1)

        if arguments[0] == 'absolute':
            mouse.position = tuple(map(int, arguments[1:]))

        elif arguments[0] == 'relative':
            mouse.move(int(arguments[1]), int(arguments[2]))

        else:
            eprint('Line %d: command is invalid' % (c + 1))

            exit(1)

    elif command == 'press':
        if arguments[0] == 'left':
            mouse.press(pynput.mouse.Button.left)
        elif arguments[0] == 'right':
            mouse.press(pynput.mouse.Button.right)
        elif arguments[0] == 'middle':
            mouse.press(pynput.mouse.Button.middle)
        else:
            eprint('Line %d: argument must be left, right or middle' % (c + 1))

            exit(1)

    elif command == 'release':
        if arguments[0] == 'left':
            mouse.release(pynput.mouse.Button.left)
        elif arguments[0] == 'right':
            mouse.release(pynput.mouse.Button.right)
        elif arguments[0] == 'middle':
            mouse.release(pynput.mouse.Button.middle)
        else:
            eprint('Line %d: argument must be left, right or middle' % (c + 1))

            exit(1)

    elif command == 'click':
        if len(arguments) < 2:
            eprint('Line %d: arguments must be two' % (c + 1))

            exit(1)
        elif not any(map(str.isdigit, arguments[1])):
            eprint('Line %d: second argument must be numeric' % (c + 1))

            exit(1)

        if arguments[0] == 'left':
            mouse.click(pynput.mouse.Button.left, int(arguments[1]))
        elif arguments[0] == 'right':
            mouse.click(pynput.mouse.Button.right, int(arguments[1]))
        elif arguments[0] == 'middle':
            mouse.click(pynput.mouse.Button.middle, int(arguments[1]))
        else:
            eprint('Line %d: argument must be left, right or middle' % (c + 1))

            exit(1)

    elif command == 'scroll':
        if len(arguments) < 2:
            eprint('Line %d: arguments must be two' % (c + 1))

            exit(1)

        elif not (any(map(str.isdigit, arguments[0])) and any(map(str.isdigit, arguments[1]))):
            eprint('Line %d: x and y must be numeric' % (c + 1))

            exit(1)

        mouse.scroll(int(arguments[0]), int(arguments[1]))

    elif command == 'down':
        if len(arguments[0]) != 1:
            eprint('Line %d: key must be a single number' % (c + 1))

            exit(1)

        elif not str.isalnum(arguments[0][0]):
            eprint('Line %d: key must be alphanumeric' % (c + 1))

            exit(1)

        keyboard.press(arguments[0][0])

    elif command == 'up':
        if len(arguments[0]) != 1:
            eprint('Line %d: key must be a single number' % (c + 1))

            exit(1)

        elif not str.isalnum(arguments[0][0]):
            eprint('Line %d: key must be alphanumeric' % (c + 1))

            exit(1)

        keyboard.release(arguments[0][0])

    elif command == 'type':
        keyboard.type(' '.join(arguments))

    else:
        eprint('Line %d: command is invalid' % (c + 1))

        exit(1)
