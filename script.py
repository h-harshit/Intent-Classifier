# This script automates the task of translating the dataset into Hindi and
# extracting the Hindi-English coded ("the usual SMS Lingo") of the Hindi
# translation from the google translate website.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import csv
import re
import pandas as pd
import time



driver_path=r"D:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

# wait for 15 seconds so as to allow html page to render 
driver.implicitly_wait(15)
# maximize window
driver.maximize_window()

url = "https://www.google.co.in/search?q=english+to+hindi+google+translate&rlz=1C1CHBF_enIN811IN811&oq=en&aqs=chrome.0.69i59j69i60j69i65l3j0.1686j0j4&sourceid=chrome&ie=UTF-8"
driver.get(url)

# path to dataset
path = r"D:\ML Projects\intent\classified_data.csv"

with open(path,'r') as file:
	reader = csv.reader(file)
	textArr = []
	df = pd.read_csv(r'D:\ML Projects\intent\classified_data.csv', encoding='ISO-8859-1', names = ['statement','intent'])
	count = 0

	for row in reader:
		# get the search textbox
		search_field = driver.find_element_by_id("tw-source-text-ta")
		search_field.clear()

		# enter the search keyword and submit
		search_field.send_keys(row[0])
		time.sleep(1) # sleep for 1 second so as to allow search values to render properly on webpage
		text = driver.find_element_by_id('tw-target-rmn')

		# match the regular expression to extract the translated text
		matchObj = re.findall(r'<span>(.*?)</span>',text.get_attribute("innerHTML"))
		textArr.append(matchObj[0])
		print(matchObj[0])
		count+=1
		print(count)

	df['Hinglish'] = textArr
	# save the dataframe as csv file
	df.to_csv(r'D:\ML Projects\intent\modified_data.csv')