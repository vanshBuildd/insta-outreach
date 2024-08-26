from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from googleapiclient.errors import HttpError
import random
from selenium.webdriver.chrome.service import Service
import os

SECRET_P = os.getenv("SECRET_P")


def send_instagram_message(receiver_username):

    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument(
    #     "user-data-dir=/Users/vanshbulani/Library/Application Support/Google/Chrome/Default")
# Manually specify a compatible ChromeDriver version
    # Replace with your Chrome version's corresponding driver version
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    # driver_service = webdriver.chrome.service.Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=driver_service)

    try:
        if driver:
            driver.get('https://www.instagram.com/')
            time.sleep(random.randint(2, 4))
            driver.find_element(
                By.XPATH, "//input[@name='username']").send_keys('bulanivansh')
            driver.find_element(
                By.XPATH, "//input[@name='password']").send_keys(SECRET_P)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

        time.sleep(random.randint(10, 12))
        count = 1
        loop = False

        greeting = ['Hello', 'Sup :)', 'Howdy', 'Hi!',
                    'Hola', 'Greetings', 'Hello sir or madame']
        if not loop:
            driver.get('https://www.instagram.com/direct/new/')
            print("1")
            time.sleep(2)
            try:
                driver.find_element(
                    By.XPATH, "//button[text()='Not Now']").click()
            except Exception as e:
                print(f"An error occurred: {e}")
                # to_field = driver.find_element(By.NAME, 'queryBox')
            print("2")

            try:
                print("3")
                new_message_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "div[role='button'][tabindex='0'] svg[aria-label='New message']"))
                )
                print("New message button found, clicking...")
                new_message_button.click()
            except Exception as e:
                print(f"An error occurred: {e}")
                to_field = driver.find_element(By.NAME, 'queryBox')
        if loop:
            driver.get('https://www.instagram.com/direct/new/')
            print("1.2")
            WebDriverWait(driver=driver, timeout=random.randint(3, 6)).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]')))
            print("2.2")
            to_field = driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')

        time.sleep(1)
        print("4")
        to_field = driver.find_element(By.NAME, 'queryBox')
        to_field.send_keys(receiver_username)
        time.sleep(random.randint(3, 4))
        if not loop:
            actionf = driver.find_element(By.NAME, 'queryBox')
        if loop:
            actionf = driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')

        a = ActionChains(driver)
        a.send_keys(Keys.TAB).send_keys(Keys.ENTER)
        a.perform()
        time.sleep(random.randint(2, 3))

        if not loop:
            try:
                # Wait for the "Chat" button to be clickable and then click it
                print("5")
                chat_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[@role='button' and text()='Chat']"))
                )
                chat_button.click()
                print("Clicked on the Chat button.")

            except Exception as e:
                print(f"An error occurred: {e}")
        if loop:
            actionz = driver.find_element(
                By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input')
        time.sleep(3)

        c = ActionChains(driver)
        c.key_down(Keys.SHIFT).send_keys(Keys.TAB).send_keys(
            Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER)
        c.perform()
        time.sleep(random.randint(4, 6))
        print("6")
        message_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[contenteditable='true'][role='textbox']"))
        )
        message_box.click()
        message_box.send_keys(random.choice(greeting))
        time.sleep(.5)
        message_box.send_keys(Keys.ENTER)
        # smssg = driver.find_element(By.TAG_NAME, 'textarea')
        # b = ActionChains(driver)
        # b.send_keys(Keys.ENTER)
        # b.perform()

        date_sent = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # sheet.update_cell(count, 4, date_sent)  # This line assumes you have a sheet to update, modify as needed
        loop = True

    except HttpError as err:
        print(err)
    finally:
        driver.quit()
