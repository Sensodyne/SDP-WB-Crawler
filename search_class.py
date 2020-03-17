from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from multiprocessing import Pool
import csv
#from bert_serving.client import BertClient
#from sklearn.metrics.pairwise import cosine_similarity
#from nltk.corpus import stopwords
#import nltk

class newsSearch:
    # enter the news sites and search the keyword
    def __init__(self, path, user):  # (self, path, user, webSite, loginTags)
        self.path = path
        self.user = user

    def login(self, driver):
        # gain access to the website with userInfo
        email = self.user["email"]
        password = self.user["password"]

        signInLink = driver.find_element_by_xpath('//*[@id="netspidersosh"]/header/div[1]/div[7]/a')
        signInLink.click()

        driver.implicitly_wait(3)

        # find log in link
        loginLink = driver.find_element_by_xpath('//*[@id="lg_login_option"]/form/div/div[3]/span')
        loginLink.click()
        driver.implicitly_wait(3)

        # enter email
        emailLink = driver.find_element_by_xpath('//*[@id="lg_login"]/form/div[1]/input') #emailTag
        emailLink.send_keys(email)

        continueLink = driver.find_element_by_name('lg_login')
        continueLink.click()
        time.sleep(0.5)

        # enter password
        passwordLink = driver.find_element_by_xpath('//*[@id="lg_password"]/form/div[1]/input') #passwordTag
        passwordLink.send_keys(password)

        continueLink2 = driver.find_element_by_xpath('//*[@id="lg_password"]/form/div[5]/input')
        continueLink2.click()
        time.sleep(0.5)

        # go to the front page
        driver.back()
        driver.implicitly_wait(3)


    def go_crawl(self):
        #loading chrome driver
        driver = webdriver.Chrome(self.path)
        driver.implicitly_wait(3)

        # enter the website
        driver.get("https://renewablesnow.com/news/albania-calls-tender-for-privatisation-of-hydro-power-co-ulez-shkopet-315184/")
        driver.implicitly_wait(3)
        ext = self.textExtractor(driver)
        print(ext)

        # # log in
        # self.login(driver)

        # # search keywords
        # search = driver.find_element_by_name('ticker')
        # search.send_keys('india ppp')
        # showresult = driver.find_element_by_class_name("searchIcon")
        # showresult.click()

        # driver.implicitly_wait(1)

        # searchresult = driver.find_element_by_xpath('//*[@id="leftContainer"]/div[2]/a')
        # searchresult.click()
        # driver.implicitly_wait(3)

        # get articles based on html tag


    def textExtractor(self, driver):
        element = driver.find_element_by_class_name('Normal')
        text = element.text
        if text == None:
            text = element.get_attribute("value")
            if text == None:
                text = element.get_attribute("innerHTML")
        return text



"""
        # 1,2페이지 검색
        for search_count in range(1,self.page_limit+1):

            # press next page button
            if search_count != 1:
                continue_link = driver.find_element_by_link_text(str(search_count))
                continue_link.click()

            google_page = driver.window_handles[0]

            # get titles of the documents and click it
            titles = driver.find_elements_by_xpath("//div[@class='r']/a")
            article_count = 0 

            # for all articles in the search result
            for article_count in range(len(titles)):
                word_count = [0,0,0]
                try:
                    title_string = titles[article_count].text.splitlines()[-1]
                except:
                    title_string = "unknown title"
                    print('title out of range error occurred')
                print(title_string)

                try:
                # handling exception, the crawler must go on
                    ActionChains(driver).key_down(Keys.CONTROL).click(titles[article_count]).key_up(Keys.CONTROL).perform()
                    driver.switch_to.window(driver.window_handles[-1])

                    element = driver.find_element_by_tag_name('body').text
                    link_url = driver.current_url
                    #print(element) ####### for demo
                    driver.implicitly_wait(5) ####### for demo
                    print("no error until word_searcher")
                    word_count = self.word_searcher(element)
                    print(word_count)
                    print('search:',search_count)
                    print('article:',article_count)
                except:
                    print('error occurred')
                    driver.switch_to.window(driver.window_handles[0])
                    continue
                
                for i in range(len(word_count)):
                    if word_count[i] != 0:
                        word_count[i] = 1

                print(word_count)
                if sum(word_count)>1:
                    link_list.append(link_url)
                    count_list.append(word_count)
                    ############################################
                    #link saving function required
                    self.csv_out(search_keyword[1],title_string,link_url,word_count)
                    ############################################
                    driver.switch_to.window(google_page)
                else:
                    driver.close()
                    driver.switch_to.window(google_page)
        print("crawling ended")
        #time.sleep(10)
        #driver.quit()
"""