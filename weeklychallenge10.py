from bs4 import BeautifulSoup

#we also want to have a way to talk to the internet so we need the request module too
import requests, json


all_matches = []

#here is the URL to the browse painting pages



total_pages = 0
while total_pages <= 10:
#lets ask requests to get that page

	url = "http://www.cagematch.net/?id=112&view=search&sEventName=WCW%20Monday%20Nitro&sEventType=TV-Show&sDateFromDay=04&sDateFromMonth=09&sDateFromYear=1995&sDateTillDay=26&sDateTillMonth=03&sDateTillYear=2001&sPromotion=2&sRegion=Amerika&sWorkerRelationship=Any&s=0" #+ str(total_pages)
	print(url)

	data_page = requests.get(url)


				#just let us know if that failed
	if data_page.status_code != 200:
		print ("There was an error with", url)

					#we are storing the HTML of the page into the variable page_html using the .text attribute of the request result
	page_html = data_page.text

					#now we are going to ask BS to parse the page
	soup = BeautifulSoup(page_html, "html.parser")


	bigtable = soup.find("div", attrs = {"class":"TableContents"})


	all_trs = soup.find_all("tr", attrs = {"class":"Trow"})
	print(all_trs)	
	#this is where the problem is happening

	for a_tr in all_trs:

		date_field = a_tr.find("td", attrs={"class":"TCol TColSeparator"})
		if date_field != None:
			print(date_field)

			match_span = a_tr.find("span", attrs={"class":"MatchCard"})
			if match_span != None:

				event_span = a_tr.find("div", attrs={"class":"MatchEventLine"})
				if event_span != None:
				
					all_matches.append({"date": date_field.text, "match card" : match_span.text, "event" : event_span})
	print(all_matches)

	total_pages = total_pages + 1

		

with open('scraped_matches.json', 'w') as f:
	f.write(json.dumps(all_opendata,indent=4))