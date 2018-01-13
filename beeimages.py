'''download images found at site provided as command line argument'''

import os, sys, requests, bs4

sitename = sys.argv[1]
print(f'Retrieving site: {sitename}')
res = requests.get(sitename)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
images = soup.select('img')

for img in images:
    imgurl = 'http://beewhimzy.com' + img.get('src')
    print(f'Found image: {imgurl}')
    try:
        result = requests.get(imgurl)
        with open(os.path.join('images', os.path.basename(imgurl)), 'wb') \
        as imageFile:
            print(f'Saving image')
            for chunk in result.iter_content(100000):
                imageFile.write(chunk)

    except Exception as exc:
        print(f'There was a problem: {exc}')

