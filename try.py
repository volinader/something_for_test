from pyclick import HumanClicker
import pyautogui as peg
import time

""" time.sleep(10)
positiopn = peg.position()
print(positiopn) """
time.sleep(10)
hc = HumanClicker()
hc.move((2398, 325), 1)
hc.click()


