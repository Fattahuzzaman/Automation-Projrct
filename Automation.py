from pydoc import cli
from tkinter import Button
import click
from matplotlib.pyplot import title
import pywinauto,time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import mouse
import pyautogui as pag
import sys




app=Application().start(r"C:\Users\FHZ\AppData\Local\Programs\ITDe-Filing_6\ITDe-Filing_6.exe")
time.sleep(4)

pag.press(['enter', 'tab', 'enter'])
time.sleep(3)

pywinauto.mouse.double_click(button='left', coords=(400, 550))
time.sleep(3)

pywinauto.mouse.click(button='left', coords=(1500,550))
time.sleep(3)

pywinauto.mouse.click(button='left', coords=(550,750))
time.sleep(3)

pywinauto.mouse.click(button='left', coords=(1086,928))
time.sleep(3)

pag.moveTo(349, 547, 2)
pag.click()
time.sleep(2)

pywinauto.mouse.click(button='left', coords=(317,169))
time.sleep(2)
pag.press('enter')
time.sleep(7)

img=pag.screenshot()
img.save("stage1.png")

pywinauto.mouse.click(button='left', coords=(1100,721))
time.sleep(2)

pywinauto.mouse.click(button='left', coords=(1574,907))
time.sleep(3)
pag.press(['enter', 'tab', 'enter'])
time.sleep(1)

pag.press('end')
time.sleep(1)
pywinauto.mouse.click(button='left', coords=(402,326))
time.sleep(3)

pag.press('end')
time.sleep(1)
pywinauto.mouse.click(button='left', coords=(1544,812))
time.sleep(2)

pag.press('end')
time.sleep(1)
pywinauto.mouse.click(button='left', coords=(1608,653))
time.sleep(3)

pywinauto.mouse.click(button='left', coords=(313,667))
time.sleep(2)
pag.typewrite('Gurgaon')
time.sleep(2)

pywinauto.mouse.click(button='left', coords=(285,810))
time.sleep(1)
pag.press('end')
pywinauto.mouse.click(button='left', coords=(1514,767))
time.sleep(3)

img=pag.screenshot()
img.save("stage2.png")


