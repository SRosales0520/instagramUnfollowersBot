from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import datetime

start = datetime.datetime.now()
class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.url = self.driver.current_url
        if self.url == "https://www.instagram.com/accounts/onetap/?next=%2F":
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(4)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        else:
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
            sleep(1)

    

    def get_unfollowers(self):
        clientUsername = 'kyleschultzhere'
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(clientUsername)
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a").click()
        sleep(4)
        self.driver.find_element_by_xpath("//a[contains(@href, '/following')]").click()
        following = self._get_names()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]").click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        file = open('{}.txt'.format(clientUsername), 'w')
        file.writelines("\n".join(not_following_back))
        file.close()
        end = datetime.datetime.now()
        print(end-start)


    def _get_names(self):
        sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]") 
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)
        followersNoSuggestions = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        links = followersNoSuggestions.find_elements_by_xpath("//a[not(../span[text()='Verified'])]")
        names = [names.text for names in links if names.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
        return names

#replace the placeholder username and password below with the credentials of the instagram account you want to use
my_bot = InstaBot('placeholderusername', 'placeholderpassword')
my_bot.get_unfollowers()

