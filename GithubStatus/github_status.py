from urllib.request import Request, urlopen
import requests


url = 'https://www.githubstatus.com/'

class GithubStatus:

    def __init__(self, url:str):
        self.url = url
        self.headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'content-type': 'text/html','content-encoding': 'gzip' }


    def get(self):
        try:
            req = requests.get(url)
            print(req.text)
        except Exception as e:
            print(e)


if __name__ == '__main__':

    github = GithubStatus(url)
    github.get()