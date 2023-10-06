import os
import urllib.request

data_dir = r"D:/Pages/"

pages = [
    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},
    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

for page in pages:
    path = data_dir + page['name'] + '.html'
    try:
        print(f"Processing: {page['url']}...")
        urllib.request.urlretrieve(page['url'], path)
        print('...done')
    except:
        print(f"Error occured while openning {page['url']}")
        print('Stopping the process!')
        break
else:
    print("All pages were downloaded")