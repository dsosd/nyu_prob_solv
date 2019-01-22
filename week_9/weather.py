import bs4
import csv
import requests

def parse_row(row):
	ret=[]
	data=row.contents

	#date
	ret.append(data[1].div.find_all("span", recursive=False)[0].text)
	#description
	ret.append(data[2].span.text)
	#high
	ret.append(data[3].div.find_all("span", recursive=False)[0].contents[0])
	#low
	ret.append(data[3].div.find_all("span", recursive=False)[2].contents[0])
	#percipitation
	ret.append(data[4].div.find_all("span", recursive=False)[1].span.contents[0])
	#wind
	ret.append(data[5].span.text.strip())

	return ret

def dump_data(filename, data):
	with open(filename, "w") as file_:
		writer=csv.writer(file_)
		for row in data:
			writer.writerow(row)

def main():
	url="https://weather.com/weather/tenday/l/New+York+NY+USNY0996:1:US"
	url_html=requests.get(url=url, timeout=8).content

	bse=object()
	if True:
		bse=bs4.BeautifulSoup(url_html, "lxml")
	else:
		bse=bs4.BeautifulSoup(url_html, "html.parser")#fallback

	out=[]
	out.append(["date", "desc", "high", "low", "percip", "wind"])#csv header

	table=bse.find_all(class_="twc-table")[0]
	for i in range(10):
		out.append(parse_row(table.tbody.contents[i]))

	dump_data("out.csv", out)

if __name__=="__main__":
	main()
