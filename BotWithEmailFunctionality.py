from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys

start = datetime.datetime.now()

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        global clientUsername
        global clientaddr
        clientUsername = input('Enter The Client\'s Username : ')
        clientaddr = input('Enter The Client\'s Email Address that should receive the list : ')
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
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(clientUsername)
        sleep(3)
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

    def _send_email(self):
        #replace the bellow email address with the gmail account you want to sent the email from
        fromaddr = 'placeholderemail@gmail.com'
        #replace  the below password placeholder with the password of the gmail account you want the email sent from
        gmailpass = 'placeholderpassword'
        #creates an instance of MIMEMultipart
        msg = MIMEMultipart()
        #stores the fromaddress, clientaddress,subject, and body
        msg['From'] = fromaddr
        msg['To'] = clientaddr
        msg['Subject'] = 'Instagram Unfollowers List'
        body = 'Here is your list of the people that you follow but dont follow you back (unfollwers).'
        #attach the body to the msg instance
        msg.attach(MIMEText(body, 'plain'))
        #open the file to be sent
        filename = '{}.txt'.format(clientUsername)
        attachment = open('{}.txt'.format(clientUsername), 'rb')
        #creating an instance of MIMEBase and naming it as p
        p = MIMEBase('application', 'octet-stream')
        #changing the payload into encoded form
        p.set_payload((attachment).read())
        #encoding it into base 64
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        #attaching the instance 'p' to the 'msg' instance
        msg.attach(p)
        #creates an SMTP session with gmail over port 587
        s = smtplib.SMTP('smtp.gmail.com', 587)
        #starts Transport Layer Security
        s.starttls()
        #authenticates login
        s.login(fromaddr, gmailpass)
        #converts the multipart msg into a string
        text = msg.as_string()
        #sends the email with the from address, to address, and the content of the email
        s.sendmail(fromaddr, clientaddr, text)
        #terminates the session
        s.quit()

    def ask_before_email(self):
        yes = {'yes','y', 'ye', ''}
        no = {'no','n'}

        choice = input('Would you like to send an email to the client with the the generated list attached to the email? Please check over the clients unfollowers file before sending! [Y/n]').lower()
        if choice in yes:
            self._send_email()
            print("The email HAS been sent ")
        elif choice in no:
            print("The email has NOT been sent")
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'")




#replace the placeholder username and password below with the login info of your instagram bot account you created 
my_bot = InstaBot('placeholderusername', 'placeholderpassword')
my_bot.get_unfollowers()
my_bot.ask_before_email()


