import time

from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions, ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from config import USERNAME, PASSWORD


options = ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('test-type')
options.add_argument('enable-strict-powerful-feature-restrictions')
options.add_argument('disable-geolocation')
browser = webdriver.Chrome(options=options)
browser.get("https://www.gympass.com/")


try:
    action = ActionChains(browser)
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Entrar')))
    action.move_to_element(browser.find_element_by_link_text('Entrar')).perform()
    action.click().perform()

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'username')))
    elem = browser.find_element_by_id('username')
    elem.send_keys(USERNAME, Keys.ENTER)
    time.sleep(2)

    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, 'password')))
    elem = browser.find_element_by_id('password')
    elem.send_keys(PASSWORD, Keys.ENTER)

    print('passo 0')
    browser.get('https://www.gympass.com/checkin')

    # location MUV
    # browser.execute_script("window.navigator.geolocation.getCurrentPosition = function (success, failure) {"+
    #                                     "success({\"coords\" : {\"latitude\": \"-8.050251\",\"longitude\": \"-34.9014556\"}, " +
    #                                     "timestamp: Date.now(),});}")

    # location madalena
    browser.execute_script("window.navigator.geolocation.getCurrentPosition = function (success, failure) {"+
                                        "success({\"coords\" : {\"latitude\": \"-8.0586606\",\"longitude\": \"-34.9069865\"}, " +
                                        "timestamp: Date.now(),});}")
    
    time.sleep(20)
    print('passo 1')
    action.move_to_element(browser.find_element_by_xpath('//span[contains(., "Refresh location")]')).perform()
    print('passo 2')
    action.click().perform()

    # time.sleep(20)
    print('passo 4')
    browser.get_screenshot_as_file("screenshot2.png")
except Exception as e:
    print('[ ocorreu um erro ao executar o script ] - ' + str(e))
finally:
    browser.quit()