from tkinter import Button
import pyautogui as peg
import time
import random
peg.FAILSAFE= False

def click_delay():
    return random.uniform(0.06, 0.1)
def mouse_movement_delay():
    return random.uniform(0.3, 0.6)
def generateMouseClearViewShift():
    return random.randint(60, 150)
def generateLoopDelay():
    return random.randint(0, 0.05)
def shop_delay():
    return random.uniform(2, 5)
def buy_delay():
    return random.uniform(0.09, 0.15)

#edit lines below before using soft
number_of_holes = 6 #number of holes at one area, prefer use 6 because some lands have 6 holes
summ_num_of_all_holes = 17 #write numbers of all holes opened for plant
number_of_lands = 3 #write numbers of opened lands
vegetable = "sunflower"  #write your vegetable 'sunflower' 'carrot'
seed_picture = "sunflower_seed" #write your vegetable seed name "cauliflower_seed" "carrot_seed"
harvest_timer = 30 #write growing time of your plant (in sec)


def land_choice():
    input('Move your mouse to left up part of area and press ENTER...')
    first_x, first_y = peg.position()
    input('Move your mouse to right down part of area and press ENTER...')
    second_x, second_y = peg.position()
    width = (second_x - first_x)
    hight = (second_y - first_y)
    return first_x, first_y, width, hight



def harvest_plants():
    for item in working_area:
        i = 0
        while i < number_of_holes:

            no_seeds = (peg.locateOnScreen('pictures\/no_seeds.png', confidence = 0.8))
            if no_seeds is not None:
                shop()
            else:
                print('Seeds exist in inventory')

            button_location = (peg.locateOnScreen(f'pictures\harvest\{vegetable}.png', confidence = 0.8, region = (item)))
            if button_location is not None:    
                button_center = peg.center(button_location)
                button_x, button_y = button_center
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(click_delay())
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                print("Plants were harvested")
                peg.moveTo(button_x + generateMouseClearViewShift(), button_y + generateMouseClearViewShift(), mouse_movement_delay())
        
            else:
                print("Nothing to harvest")

            reward_window = (peg.locateOnScreen("pictures\/rewards_window.png", confidence = 0.8))
            if reward_window is not None:
                get_rewards()
            i+=1

def plant_seed():
    for item in working_area:
        i = 0
        while i < number_of_holes:
            hoole_place = (peg.locateOnScreen('pictures\empty_hole.png', confidence = 0.8, region = (item)))
            
            no_seeds = (peg.locateOnScreen('pictures\/no_seeds.png', confidence = 0.8))
            if no_seeds is not None:
                shop()
            else:
                print('Seeds exist in inventory')

            if hoole_place is not None:
                button_center = peg.center(hoole_place)
                button_x, button_y = button_center
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                print("Seed was planted")
                peg.moveTo(button_x + generateMouseClearViewShift(), button_y + generateMouseClearViewShift(), mouse_movement_delay())
            
            else:
                print("No space for plant")
            i += 1

def get_rewards():
    reward_window = (peg.locateOnScreen("pictures\/rewards_window.png", confidence = 0.8))
    #reward_picture = (peg.locateOnScreen("pictures\/reward.png", confidence = 0.8))
    
    if reward_window is not None:
        
        reward_picture = (peg.locateOnScreen("pictures\/reward.png", confidence = 0.7))
        if reward_picture is not None:
            button_center = peg.center(reward_picture)
            button_x, button_y = button_center
            print("reward")
            peg.moveTo(button_x, button_y, mouse_movement_delay())
            peg.click()
        
            time.sleep(click_delay())
        reward_close = (peg.locateOnScreen("pictures\close_reward.png", confidence = 0.8))
        if reward_close is not None:
            button_center2 = peg.center(reward_close)
            button_x, button_y = button_center2
            peg.moveTo(button_x, button_y, mouse_movement_delay())
            peg.click()
            print("You got reward")
            peg.moveTo(button_x + generateMouseClearViewShift(), button_y + generateMouseClearViewShift(), mouse_movement_delay())
           
        else:
            get_rewards()
            print("no close button")
        
        
    else:
        print("no window")

def shop():
    shop = "pictures\shop\shop.png"
    sync = "pictures\shop\sync.png"
    not_robot = "pictures\shop\/not_robot.png"
    metamask = "pictures\shop\scrolling.png"
    confirm = "pictures\shop\confirm.png"
    continuee = "pictures\shop\continue.png"
    buy = "pictures\shop\/buy.png"
    exit = "pictures\shop\exit.png"
    open_metamask = "pictures\shop\open_metamask.png"

    seeds_zero = (peg.locateOnScreen(f"pictures\shop\seed_pictures\{seed_picture}.png", confidence = 0.8))
    if seeds_zero is not None:
        time.sleep(shop_delay())
        shop_button = peg.locateOnScreen(shop, confidence = 0.8)
        button_center3 = peg.center(shop_button)
        button_x, button_y = button_center3
        peg.moveTo(button_x, button_y, mouse_movement_delay())
        peg.click()
        time.sleep(shop_delay())

        
        sync_button = peg.locateOnScreen(sync, confidence = 0.8)
        button_center4 = peg.center(sync_button)
        button_x, button_y = button_center4
        peg.moveTo(button_x, button_y, mouse_movement_delay())
        peg.click()
        time.sleep(shop_delay())

        not_robot_button = peg.locateOnScreen(not_robot, confidence = 0.8)
        button_center5 = peg.center(not_robot_button)
        button_x, button_y = button_center5
        peg.moveTo(button_x, button_y, mouse_movement_delay())
        peg.click()
        time.sleep(5)
        
        #dont_work_button = peg.locateOnScreen(dont_work, confidence = 0.8)
        #while dont_work_button is not None:
            #break
        try:
            metamask_button = peg.locateOnScreen(metamask, confidence = 0.8)
            if metamask_button is not None:
            #metamask_button = peg.locateOnScreen(metamask, confidence = 0.8)
                button_center6 = peg.center(metamask_button)
                button_x, button_y = button_center6
                time.sleep(shop_delay())
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click(clicks = 6, interval=0.25)
                time.sleep(5)


                metamask_button = peg.locateOnScreen(metamask, confidence = 0.8)
                button_center6 = peg.center(metamask_button)
                button_x, button_y = button_center6
                time.sleep(5)
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click(clicks = 6, interval=0.25)
                time.sleep(5)



                confirm_button = peg.locateOnScreen(confirm, confidence = 0.8)
                button_center7 = peg.center(confirm_button)
                button_x, button_y = button_center7
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(80)

                continuee_button = peg.locateOnScreen(continuee, confidence = 0.8)
                button_center8 = peg.center(continuee_button)
                button_x, button_y = button_center8
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())
        
                shop_button = peg.locateOnScreen(shop, confidence = 0.8)
                button_center3 = peg.center(shop_button)
                button_x, button_y = button_center3
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())

                buy_button = peg.locateOnScreen(buy, confidence = 0.8)
                button_center9 = peg.center(buy_button)
                button_x, button_y = button_center9
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click(clicks = 40, interval= buy_delay())
                time.sleep(shop_delay())

                close_button = peg.locateOnScreen(exit, confidence = 0.8)
                button_center10 = peg.center(close_button)
                button_x, button_y = button_center10
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())

        except:
            print('no window')
        try:
            open_metamask_button = peg.locateOnScreen(open_metamask, confidence = 0.8)
            if open_metamask_button is not None:
                button_center11 = peg.center(open_metamask_button)
                button_x, button_y = button_center11
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(5)

                metamask_button = peg.locateOnScreen(metamask, confidence = 0.8)
                button_center6 = peg.center(metamask_button)
                button_x, button_y = button_center6
                time.sleep(5)
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click(clicks = 6, interval=0.25)
                time.sleep(5)



                confirm_button = peg.locateOnScreen(confirm, confidence = 0.8)
                button_center7 = peg.center(confirm_button)
                button_x, button_y = button_center7
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(80)

                continuee_button = peg.locateOnScreen(continuee, confidence = 0.8)
                button_center8 = peg.center(continuee_button)
                button_x, button_y = button_center8
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())
        
                shop_button = peg.locateOnScreen(shop, confidence = 0.8)
                button_center3 = peg.center(shop_button)
                button_x, button_y = button_center3
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())

                buy_button = peg.locateOnScreen(buy, confidence = 0.8)
                button_center9 = peg.center(buy_button)
                button_x, button_y = button_center9
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click(clicks = 40, interval= buy_delay())
                time.sleep(shop_delay())

                close_button = peg.locateOnScreen(exit, confidence = 0.8)
                button_center10 = peg.center(close_button)
                button_x, button_y = button_center10
                peg.moveTo(button_x, button_y, mouse_movement_delay())
                peg.click()
                time.sleep(shop_delay())

        except:
            print('no transaction')

            
#checking on errors
def something_wrong():
    session_expired = peg.locateOnScreen("pictures\session_exp\session_expired.png")
    something_wrong = peg.locateOnScreen("pictures\session_exp\something_wrong.png")
    if something_wrong or session_expired is not None:
        peg.press("f5")
        time.sleep(10)
        start = peg.locateOnScreen("pictures\session_exp\start_farm.png")
        button_center13 = peg.center(start)
        button_x, button_y = button_center13
        peg.moveTo(button_x, button_y, mouse_movement_delay())
        peg.click()
        time.sleep(10)


def steps_of_functions():
    
    harvest_plants()
    plant_seed()
    time.sleep(harvest_timer)
    
    
working_area = []
def main(number_of_slots):  #main function
    if len(working_area) < 1:
        i = 0
        while i < number_of_lands:
    
            first_x, first_y, width, hight = land_choice()
            working_area.append([first_x, first_y, width, hight])
            i+=1
    error_check = 0
    i = 0
    while True:
        while i < number_of_slots:
            steps_of_functions()
            delay = click_delay()
            print(f"Cycle {i} completed")

            print(f'Sleeping {delay} seconds')
            time.sleep(delay)

            i += 1
            error_check += 1
            print("error check", error_check)
        print("loop competed")

        #delay = generateLoopDelay()
        #print(f'Sleeping {delay} seconds')
        #time.sleep(delay)
            
        i = 0
        
        
        while error_check > 104:
            print("testing on errors")
            something_wrong()
            time.sleep(click_delay())
            error_check = 0
        
main(summ_num_of_all_holes)

