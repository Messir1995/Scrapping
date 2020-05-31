import requests
from bs4 import BeautifulSoup
import csv
class Scraping_information:
	path = "output.csv"

	def __init__(self):
		pass

	#get data about object of search
	def data_about_site(self):
		self.page_link ='http://www.rivegauche.ru/content/izmeneniya-v-grafike-raboty-magazinov-riv-gosh'
		self.point = 'collapsed hidden'

	#get code from page
	def get_page(self):
		self.page_response = requests.get(self.page_link, timeout=5)

	#find information about place
	def get_data(self): 
		self.page_content = BeautifulSoup(self.page_response.content, "html.parser")
		#print(self.page_content)
		self.search_data = str(self.page_content.find_all(class_=self.point))
		self.search_data = BeautifulSoup(self.search_data, "html.parser")
		#self.search_data2 = BeautifulSoup(self.search_data3, "html.parser")
		#self.search_data = self.search_data2.find_all('li')
		#print(self.search_data)
	
	#write our data to csv
	def csv_writer(self):
		with open(self.path, "w", newline='') as csv_file:
			writer = csv.writer(csv_file, delimiter=';')
			i=0
			#for depth in len(list(self.point_info[0])):
			for depth in range(len(list(data.point_info[0]))):
			#for rows in self.point_info:
				writer.writerow(self.point_info[0][i])
				writer.writerow(self.point_info[1][i])
				i+=1

	

data = Scraping_information()
data.data_about_site()
data.get_page()
data.get_data()
i=1
#parsing information
data.point_info = [["Date"],["Points"]]
temp = data.search_data.find_all('li')
for point in temp:
	for string in point.strings:
		if i%2==1:
			data.point_info[0].append(repr(string))
		if i%2==0:
			data.point_info[1].append(repr(string))
		i+=1
print(data.point_info)
data.csv_writer()