from selenium import webdriver
from time import sleep

class instabot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Log in')]")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
        .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)



        
        
    def get_unfollowers(self):
       # driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))\
        

        self.driver.find_element_by_xpath("//a[contains(text(), 'mave.rick1901')]")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()

        sleep(2)
        sugg = self.driver.find_element_by_xpath('//h4[contains(text(), Suggestions)]')
        self.driver.execute_script("arguments[0].scrollIntoView();",sugg)
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0,1
        while last_ht!= ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)                                          #scrolling following list

        
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        self.driver.find_element_by_xpath("//a[contains(@href, '/followers')]")\  #followers list
            .click()
        sleep(3)
        
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        sleep(2)
        
        
        
        sleep(2)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log Out')]")\ #logging out
        .click()
        
        #self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div/button")
        
   # def _get_names(self):
        
        
       # links = scroll_box.find_element_by_tag_name('a')
        #names = [name.text for name in links if name.text != ''] 

        #close button
     #   self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button/svg")\
      #      .click()
        #return names
    
           #/ .click()
   # def unfollowers(self):
    #    followings = self._get_names()
     #   followers = self._get_names()
      #  not_following_back = [user for user in followings if user not in followers]
       # print(not_following_back) 


    
        
#//a[contains(text(), 'Log in')]") where a is link tag, which simply searches a text 'Log in on html page

bot = instabot("mave.rick1901", "Bubble@33")
bot.get_unfollowers()
#bot.unfollowers()

#/html/body/div[4]/div/div/div[3]/button[2]
