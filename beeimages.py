import os, requests, bs4

res = requests.get('http://beewhimzy.com')
soup = bs4.BeautifulSoup(res.text, 'html.parser')
images = soup.select('img')

for img in images:
	imgurl = 'http://beewhimzy.com' + img.get('src')
	try:
		result = requests.get(imgurl)
		imageFile = open(os.path.join('beewhimzy', os.path.basename(imgurl)), 'wb')
		
		for chunk in result.iter_content(100000):
			imageFile.write(chunk)

		imageFile.close()
	except Exception as exc:
		print(f'There was a problem: {exc}')

