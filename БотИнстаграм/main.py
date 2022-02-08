from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from auth_name import username, password
from selenium.webdriver.chrome.service import Service
import time
import random



def hashtag_search(username, password, hash_tag):
    ''' It accepts login, password, and hashtag.
        A virtual Chrome browser is used.
        Log in to the site and search by hashtag.
        Get links to hashtag uploaded posts and like them. '''
    
    service = Service(executable_path='chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    try:
        browser.get('https://www.instagram.com/')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.clear()
        username_input.send_keys(username)
        time.sleep(random.randrange(3, 5))

        password_input = browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(random.randrange(3, 5))

        password_input.send_keys(Keys.ENTER)
        time.sleep(random.randrange(12))
        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hash_tag}/')
            time.sleep(14)

            for i in range(0, 8):
                # "i" is number of page scrolls.
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(15))
            time.sleep(1000)
            href = browser.find_elements(By.TAG_NAME, 'a')
            posts_urls = [item.get_attribute("href") for item in href if '/p/' in item.get_attribute("href")]
            print(posts_urls)
            # posts_urls = []
            # for item in href:
            #     href = item.get_attribute('href')
            #     if '/p/' in href:
            #         posts_urls.append(href)
            #         print(href)

            for url in posts_urls:
                try:
                    browser.get(url)
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button").click()
                    time.sleep(random.randrange(100, 120))
                except Exception as ex:
                    print(ex)

            browser.close()
            browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

hashtag_search(username, password, 'art')
