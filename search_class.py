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

        loginLink = driver.find_Element_by_id("SIGN-IN")
        time.sleep(0.5)

        emailLink = driver.find_element_by_id("lg_id") #emailTag
        emailLink.send_keys(email)

        # click
        time.sleep(0.5)

        passwordLink = driver.find_element_by_id("lg_password") #passwordTag
        passwordLink.send_keys(password)

        # click
        time.sleep(0.5)

        access = driver.find_element_by_id("submitLoginFormBtn")
        access.click()

        time.sleep(0.5)


    def go_crawl(self):
        #loading chrome driver
        driver = webdriver.Chrome(self.path)
        driver.implicitly_wait(3)

        # enter the website
        driver.get("https://economictimes.indiatimes.com/")
        driver.implicitly_wait(3)

        # log in
        self.login(driver)

        # search keywords
        try:
            navigator = driver.find_element_by_link_text("Toggle navigation")
            navigator.click()
        except:
            pass

        search = driver.find_element_by_xpath("/html/body/app-root/user-logged-in-home/app-header-main/header/div/div/div[2]/div/app-search/div/div[1]/input")
        search.send_keys(self.company)
        showresult = driver.find_element_by_id("searchSubmitBtn")
        showresult.click()

        time.sleep(0.5)

        searchresult = driver.find_elements_by_partial_link_text("NYSE")

        # get articles based on html tag


class text_parser:
    def __init__(self, driver):
        self.driver = driver
    
    def TextExtractor(driver):
    element = self.driver.find_element_by_class_name('Normal')
    text = element.txt
    if text = None:
        text = element.get_attribute("value")
        if text = None:
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