import csv
import json
from search_class import search_with_user_data

def google_search_word_input(path):
    search_word_list = []

    with open(path,newline='', encoding='UTF-8') as swinput:
        reader = csv.reader(swinput)
        for row in reader:
            search_word_list.append(row[0])
    return search_word_list

def word_set_input(path):
    word_set_list = []

    with open(path,newline='', encoding='UTF-8') as swinput:
        reader = csv.reader(swinput)
        for row in reader:
            word_set_list.append(row[0])
    return word_set_list



if __name__=='__main__':
    # Datapaths
    userData_path = './userData.json'

    # read userData(JSON File format)
    user = None
    with open(userData_path, "r", encoding = "UTF-8") as clientJson :
        userData_loaded = json.load(clientJson)

    temp = search_with_user_data(path = './chromedriver',
        user = userData_loaded,
        company = "TTM")

    temp.go_crawl("Annual")

    #input_path = './crawler_input.xlsx'
    #get_input_excel(input_path)
    #pool = Pool(processes=1)
    #temp_keyword = [("'india' PPP ADB",-1)]#,('beta',1),('caesar',2),('double',3)]
    #pool.map(go_crawl,temp_keyword)
