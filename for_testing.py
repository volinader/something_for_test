from pyclick import HumanClicker
import pyautogui as peg
import time

""" time.sleep(10)
positiopn = peg.position()
print(positiopn) """
""" time.sleep(10)
hc = HumanClicker()
hc.move((2398, 325), 1)
hc.click() """

def count(numbers_of_holes, x):
    #numbers = 0
    i=0
    while i < numbers_of_holes:
        while x > 20:
            break
        else:
            #numbers +=1
            x+=1
            return x
        i+=1

count(50, 4)
