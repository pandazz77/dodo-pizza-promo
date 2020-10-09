from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from captcha_solver import CaptchaSolver
from urllib.request import urlopen
from PIL import Image
import pyautogui

def checkpromo():
    driver.get('https://dodopizza.ru/peterburg')
    input('Enter?')
    driver.get('https://dodopizza.ru/peterburg/cart')
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-app"]/main/section[3]/div/div/div/input').send_keys('7024C7EA4\n')
    url = input('Введите url captha: ')
    image = urlopen(url).read()
    with open("image.png", "wb") as f:
        f.write(image)
    im = Image.open("image.png")
    x = (im.size[0])
    print('Size: '+str(x))
    solver = CaptchaSolver('rucaptcha', api_key='#########')
    raw_data = open('image.png', 'rb').read()
    solve = (solver.solve_captcha(raw_data))
    print(solve)
    array = []
    for i in range(len(solve)):
        array.append(int(solve[i]))
    if x == 300:
        for i in array:
            if i==1:
                pyautogui.moveTo(550, 330)
                pyautogui.click()
            elif i==2:
                pyautogui.moveTo(680, 330)
                pyautogui.click()
            elif i==3:
                pyautogui.moveTo(800, 330)
                pyautogui.click()
            elif i==4:
                pyautogui.moveTo(550, 450)
                pyautogui.click()
            elif i==5:
                pyautogui.moveTo(680, 450)
                pyautogui.click()
            elif i==6:
                pyautogui.moveTo(800, 450)
                pyautogui.click()
            elif i==7:
                pyautogui.moveTo(550, 590)
                pyautogui.click()
            elif i==8:
                pyautogui.moveTo(680, 590)
                pyautogui.click()
            elif i==9:
                pyautogui.moveTo(800, 590)
                pyautogui.click()
            time.sleep(1)
    if x==450:
        for i in array:
            if i==1:
                pyautogui.moveTo(530, 310)
                pyautogui.click()
            elif i==2:
                pyautogui.moveTo(630, 310)
                pyautogui.click()
            elif i==3:
                pyautogui.moveTo(730, 310)
                pyautogui.click()
            elif i==4:
                pyautogui.moveTo(830, 310)
                pyautogui.click()
            elif i==5:
                pyautogui.moveTo(530, 405)
                pyautogui.click()
            elif i==6:
                pyautogui.moveTo(630, 405)
                pyautogui.click()
            elif i==7:
                pyautogui.moveTo(730, 405)
                pyautogui.click()
            elif i==8:
                pyautogui.moveTo(830, 405)
                pyautogui.click()
            elif i==9:
                pyautogui.moveTo(530, 500)
                pyautogui.click()
            elif i==10:
                pyautogui.moveTo(630, 500)
                pyautogui.click()
            elif i==11:
                pyautogui.moveTo(730, 500)
                pyautogui.click()
            elif i==12:
                pyautogui.moveTo(830, 500)
                pyautogui.click()
            elif i==13:
                pyautogui.moveTo(530, 600)
                pyautogui.click()
            elif i==14:
                pyautogui.moveTo(630, 600)
                pyautogui.click()
            elif i==15:
                pyautogui.moveTo(730, 600)
                pyautogui.click()
            elif i==16:
                pyautogui.moveTo(830, 600)
                pyautogui.click()
    input('end')
    html = driver.page_source
    soup = BeautifulSoup(html,  "html.parser")
    with open("soup.txt","w",encoding="UTF-8") as file:
        file.write(str(soup))


options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
driver = webdriver.Chrome(executable_path = "chromedriver.exe",chrome_options=options,)
checkpromo()

cookies = driver.get_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)