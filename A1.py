
import pyautogui 
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')


im = pyautogui.screenshot(region=(279,508, 572, 51))
im2 = pyautogui.screenshot('my_screenshot.png')
