from bs4 import BeautifulSoup
import requests
import tweepy
from credentials import creds
import datetime
import time

base_url = "http://www.tvguide.com/tvshows/law-order/tv-listings/100255/"
svu_url = "http://www.tvguide.com/tvshows/law-order/tv-listings/100257/"

def scraper(url):
    all_showings = []
    data = requests.get(url)
    souper = BeautifulSoup(data.text, 'html.parser')
    day = souper.find_all('span', {'class': 'airing-date-day'})
    date = souper.find_all('span', {'class': 'airing-date-date'})
    time = souper.find_all('span', {'class': 'airing-date-time'})
    channel = souper.find_all('span', {'class': 'airing-details-channels'})

    day_list = []
    date_list = []
    time_list = []
    channel_list = []

    for x in day:
        day_list.append(x.text)

    for x in date:
        date_list.append(x.text)

    for x in time:
        time_list.append(x.text)

    for x in channel:
        channel_list.append(x.text)

    for i,show in enumerate(day_list):
        new_show = []
        new_show.append(day_list[i])
        new_show.append("".join(char for char in date_list[i] if char.isdecimal()))
        new_show.append(time_list[i])
        new_show.append(channel_list[i])
        all_showings.append(new_show)

    for show in all_showings:
        if 'pm' in show[2]:
            show[2] = show[2].split(':')
            show[2] = int(show[2][0])
            if show[2] == 12:
                pass
            else:
                show[2] = int(show[2]) + 12
        else:
            show[2] = show[2].split(':')
            show[2] = int(show[2][0])
            if show[2] == 12:
                show[2] = 0
    return all_showings
# day = ['Tue', 'Tue', 'Tue', 'Tue', 'Tue', 'Tue', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed']
# date = ['Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25']
# time = ['6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm', '12:00am', '1:00am', '4:00am', '5:00am', '10:00am', '11:00am', '11:00am', '12:00pm', '12:00pm', '1:00pm', '1:00pm', '2:00pm', '2:00pm', '3:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm']
# channel = ['WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WGNA', 'TNT', 'WE', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'ION', 'ION', 'ION']
#
# svu_day = ['Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Thu', 'Fri', 'Fri', 'Fri', 'Fri']
# svu_date = ['Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 26', 'Jan 27', 'Jan 27', 'Jan 27', 'Jan 27']
# svu_time = ['12:00am', '1:00am', '4:00am', '5:00am', '8:00pm', '9:00pm', '4:01am', '5:00am', '11:00am', '12:00pm', '1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm', '8:00pm', '9:00pm', '11:01pm', '12:01am', '5:00am', '9:00am', '10:00am']
# svu_channel = ['USA', 'USA', 'USA', 'USA', 'NBC', 'NBC', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA', 'USA']

def finder(shows):
    for show in shows:
        # print(show)
        on_soon = []
        x = datetime.datetime(year=2017,month=1,day=int(show[1]),hour=int(show[2]))
        low = datetime.timedelta(minutes=2)
        high = datetime.timedelta(minutes=13)
        # print(x)
        # print(x-low)
        # print(datetime.datetime.now())
        # print(x-high)
        if x - low > datetime.datetime.now() and x - high < datetime.datetime.now():
            on_soon.append(show)
            return show

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def send_tweet(show):
    cfg = {
    "consumer_key" : creds()[0],
    "consumer_secret" : creds()[1],
    "access_token" : creds()[2],
    "access_token_secret" : creds()[3]
    }

    api = get_api(cfg)
    tweet ="On {} in 5 minutes\n{} {}:00".format(show[3],show[0],show[2])
    status = api.update_status(status=tweet)

def send_second_tweet(show):
    cfg = {
    "consumer_key" : creds()[0],
    "consumer_secret" : creds()[1],
    "access_token" : creds()[2],
    "access_token_secret" : creds()[3]
    }

    api = get_api(cfg)
    tweet ="On {} in 10 minutes\n{} {}:00".format(show[3],show[0],show[2])
    status = api.update_status(status=tweet)

def send_svu_tweet(show):
    cfg = {
    "consumer_key" : creds()[0],
    "consumer_secret" : creds()[1],
    "access_token" : creds()[2],
    "access_token_secret" : creds()[3]
    }

    api = get_api(cfg)
    tweet ="SVU on {} in 10 minutes\n{} {}:00".format(show[3],show[0],show[2])
    status = api.update_status(status=tweet)

def main():
    all_showings = scraper(base_url)
    svu_showings = scraper(svu_url)
    z = finder(svu_showings)
    x = finder(all_showings)
    if x:
        all_showings.remove(x)
    y = finder(all_showings)
    if x and y:
        send_second_tweet(x)
        time.sleep(360)
        send_tweet(y)
    elif x and not y:
        if z:
            send_svu_tweet(z)
            time.sleep(360)
            send_tweet(x)
        else:
            time.sleep(360)
            send_tweet(x)
    else:
        if z:
            time.sleep(360)
            send_svu_tweet(z)
        else:
            time.sleep(360)
    time.sleep(3240)

main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
main()
