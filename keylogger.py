from pynput.keyboard import Key, Listener
import sys

def on_press(key):
    if key == Key.esc:
        return False
    if key == Key.space:
        print(' ', end='', flush=True)
    elif key == Key.enter:
        print('')
    elif key == Key.tab:
        print('\n[tab] ',end='',flush=True)
    elif key == Key.backspace:
        print('[<--]',end='',flush=True)
    elif key == Key.alt:
        print('[alt]',end='',flush=True)
    else:
        print(str(key)[1],end='',flush=True)

with Listener(on_press=on_press) as listener:
    if listener.join() == False:
        sys.exit(0)
