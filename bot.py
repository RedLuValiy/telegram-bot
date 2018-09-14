import requests
import misc

token = misc.token
URL = 'ssl://api.telegram.org/bot' + token +'/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    print(r.content)


def main():
    get_updates()


if __name__ == '__main__':
    main()
