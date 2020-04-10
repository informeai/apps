import requests




class GithubStatus:

    def status(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/status.json')
            return req.json()
        except Exception as e:
            print(e)

    def sumary(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/summary.json')
            return req.json()
        except Exception as e:
            print(e)

    def components(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/components.json')
            return req.json()
        except Exception as e:
            print(e)

    def insidents_not_resolv(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/incidents/unresolved.json')
            return req.json()
        except Exception as e:
            print(e)

    def insidents_all(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/incidents.json')
            return req.json()
        except Exception as e:
            print(e)

    def manutention_programated(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/scheduled-maintenances/upcoming.json')
            return req.json()
        except Exception as e:
            print(e)

    def manutention_scheded(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/scheduled-maintenances/active.json')
            return req.json()
        except Exception as e:
            print(e)

    def manutention_scheded_all(self):
        try:
            req = requests.get('https://kctbh9vrtdwd.statuspage.io/api/v2/scheduled-maintenances.json')
            return req.json()
        except Exception as e:
            print(e)


if __name__ == '__main__':

    github = GithubStatus()
    sumary = github.sumary()
    print(sumary)