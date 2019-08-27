import requests, bs4

#res = requests.get('https://blogs.wsj.com/cio/2018/03/21/the-morning-download-salesforces-bets-6-5-billion-on-the-api-economy/')
res = requests.get('https://blogs.wsj.com/cio/2018/03/20/ibm-tool-seeks-to-bridge-ai-skills-gap/')

soup = bs4.BeautifulSoup(res.text, 'lxml')

hi = soup.select('.paywall')

print(hi[0].getText())


