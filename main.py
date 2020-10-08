import webbrowser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import requests
import keyboard
import random
import urllib
import time
from datetime import datetime
from secret import passwords

formUrl = "https://docs.google.com/forms/d/e/1FAIpQLSfkZL0uDGKZRr_7hc81BygkoI_biohM-T83ErQlIhWJMETvRg/viewform"

emails = ["bharat.kathi@warriorlife.net", "kashyap.chaturvedula@warriorlife.net", "robotics@warriorlife.net", "johnny.panos@warriorlife.net", "cyrus.bugwadia@warriorlife.net"]

counter = 0;

while True:
    print("FORM RESPONSE " + str(counter))
    
    now = datetime.now()
    current_time = now.strftime("%H")
    print(str(now) + " - " + current_time)

    if int(current_time) < 2 or int(current_time) > 5:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_window_size(1200, 700)

        driver.get(formUrl)

        elem = driver.find_element_by_id("identifierId")
        elem.send_keys(emails[counter % len(emails)])
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        keyboard.write(passwords[counter % len(emails)])
        keyboard.press_and_release("enter")

        print("Logged in!")
        time.sleep(5)
        print("starting form entry")

        keyboard.press_and_release("tab")
        keyboard.press_and_release("tab")
        # Male- Most optimistic/encouraging
        keyboard.write("Wan, Alex")
        keyboard.press_and_release("tab")
        # Female- Most optimistic/encouraging
        keyboard.write("Tariku, Agape")
        keyboard.press_and_release("tab")
        # Male- Most likely to start their own company
        keyboard.write("Kathi, Bharat")
        keyboard.press_and_release("tab")
        # Female- Most likely to start their own company
        keyboard.write("Mehendale, Rucha")
        keyboard.press_and_release("tab")
        # Male- Most Likely To Own a Coffee House in New York
        keyboard.write("Lopes, Alex")
        keyboard.press_and_release("tab")
        # Female- Most Likely To Own a Coffee House in New York
        keyboard.write("Choi, Melody")
        keyboard.press_and_release("tab")
        # Male- Most Likely to Climb Mt. Everest
        keyboard.write("Fujikawa, Colin")
        keyboard.press_and_release("tab")
        # Female- Most Likely to Climb Mt. Everest
        keyboard.write("Khare, Kavya")
        keyboard.press_and_release("tab")
        # Male- Most likely to get a star on the Hollywood Walk of Fame *
        keyboard.write("Tran, Tommy")
        keyboard.press_and_release("tab")
        # Female- Most likely to get a star on the Hollywood Walk of Fame
        keyboard.write("Guo, Tiffany")
        keyboard.press_and_release("tab")
        # Male- Best person to be stranded with on a desert island *
        keyboard.write("Chan, Myron")
        keyboard.press_and_release("tab")
        # Female- Best person to be stranded with on a desert island
        keyboard.write("Ta, Hannah")
        keyboard.press_and_release("tab")
        # Male- Most likely to notice you’re having a bad day, even on zoom *
        keyboard.write("Tripathi, Neel")
        keyboard.press_and_release("tab")
        # Female- Most likely to notice you’re having a bad day, even on zoom
        keyboard.write("Kammersgard, Morgan")
        keyboard.press_and_release("tab")
        # Male- Most likely to miss their zoom meeting
        keyboard.write("Zhao, Albert")
        keyboard.press_and_release("tab")
        # Female- Most likely to miss their zoom meeting
        keyboard.write("Narasani, Anushka")
        keyboard.press_and_release("tab")
        # Male- Most likely to star in their own reality show
        keyboard.write("Qiu, Kevin")
        keyboard.press_and_release("tab")
        # Female- Most likely to star in their own reality show
        keyboard.write("Vikram, Shreya")
        keyboard.press_and_release("tab")
        # Male- Best Story Teller
        keyboard.write("Zhao, Albert")
        keyboard.press_and_release("tab")
        # Female- Best Story Teller
        keyboard.write("Yu, Caroline")
        keyboard.press_and_release("tab")
        # Male- Most likely to care about the world around them
        keyboard.write("Tang, William")
        keyboard.press_and_release("tab")
        # Female- Most likely to care about the world around them
        keyboard.write("Rheams, Emma")
        keyboard.press_and_release("tab")
        # Male- Most likely to work at Valley
        keyboard.write("Sizelove, Mark")
        keyboard.press_and_release("tab")
        # Female- Most likely to work at Valley
        keyboard.write("Vals, Sierra")
        keyboard.press_and_release("tab")
        # Male- Most contagious laugh
        keyboard.write("Hu, Jonathan")
        keyboard.press_and_release("tab")
        # Female- Most contagious laugh
        keyboard.write("Atienza, Melia")
        keyboard.press_and_release("tab")
        # Male- Most dependable
        keyboard.write("Taylor, Joshua")
        keyboard.press_and_release("tab")
        # Female- Most dependable
        keyboard.write("Chen, Connie")
        keyboard.press_and_release("tab")
        # Male- Most inspirational
        keyboard.write("Chen, Jiashu")
        keyboard.press_and_release("tab")
        # Female- Most inspirational
        keyboard.write("Merza, Cameron")
        keyboard.press_and_release("tab")
        # Male- Most likely to talk their way out of trouble
        keyboard.write("Adimulam, Karthik")
        keyboard.press_and_release("tab")
        # Female- Most likely to talk their way out of trouble
        keyboard.write("Munro, Kareena")
        keyboard.press_and_release("tab")
        # Male- Most likely to be a pro athlete
        keyboard.write("Lumer, Nikhil")
        keyboard.press_and_release("tab")
        # Female- Most likely to be a pro athlete
        keyboard.write("Smith, Skyler")
        keyboard.press_and_release("tab")
        # Male- Most likely to take a road trip and not return
        keyboard.write("Zhao, Albert")
        keyboard.press_and_release("tab")
        # Female- Most likely to take a road trip and not return
        keyboard.write("Salehpour, Alyssa")
        keyboard.press_and_release("tab")
        # Male- Most likely to be a missionary
        keyboard.write("Tharp, Dylan")
        keyboard.press_and_release("tab")
        # Female- Most likely to be a missionary
        keyboard.write("Venneman, Bryne")
        keyboard.press_and_release("tab")
        # Male- Most likely to know the scriptures by heart
        keyboard.write("Tharp, Dylan")
        keyboard.press_and_release("tab")
        # Female- Most likely to know the scriptures by heart
        keyboard.write("Homrich, Makenzie")
        keyboard.press_and_release("tab")
        # ok submit it now or smth
        keyboard.press_and_release("tab")
        keyboard.press_and_release("enter")

        driver.quit()
        counter += 1

    else:
        print("Sleep time...")

    wait = random.randint(500, 1200)
    print("waiting " + str(wait) + "...")
    time.sleep(wait);
    print("")