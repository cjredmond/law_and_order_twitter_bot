from bs4 import BeautifulSoup
import requests
import tweepy
from credentials import creds

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

cfg = {
"consumer_key" : creds()[0],
"consumer_secret" : creds()[1],
"access_token" : creds()[2],
"access_token_secret" : creds()[3]
}

api = get_api(cfg)
tweet = "Hi"
status = api.update_status(status=tweet)

# if __name__ == "__main__":
#     main()

base_url = "http://www.tvguide.com/tvshows/law-order/tv-listings/100255/"

all_showings = []
# data = requests.get(base_url)
# souper = BeautifulSoup(data.text, 'html.parser')
# day = souper.find_all('span', {'class': 'airing-date-day'})
# date = souper.find_all('span', {'class': 'airing-date-date'})
# time = souper.find_all('span', {'class': 'airing-date-time'})
# channel = souper.find_all('span', {'class': 'airing-details-channels'})

# day = '[<span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>]'
# date = '[<span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>]'
# time = '[<span class="airing-date-time">6:00pm</span>, <span class="airing-date-time">7:00pm</span>, <span class="airing-date-time">8:00pm</span>, <span class="airing-date-time">9:00pm</span>, <span class="airing-date-time">10:00pm</span>, <span class="airing-date-time">11:00pm</span>, <span class="airing-date-time">12:00am</span>, <span class="airing-date-time">1:00am</span>, <span class="airing-date-time">4:00am</span>, <span class="airing-date-time">5:00am</span>, <span class="airing-date-time">10:00am</span>, <span class="airing-date-time">11:00am</span>, <span class="airing-date-time">11:00am</span>, <span class="airing-date-time">12:00pm</span>, <span class="airing-date-time">12:00pm</span>, <span class="airing-date-time">1:00pm</span>, <span class="airing-date-time">1:00pm</span>, <span class="airing-date-time">2:00pm</span>, <span class="airing-date-time">2:00pm</span>, <span class="airing-date-time">3:00pm</span>, <span class="airing-date-time">3:00pm</span>, <span class="airing-date-time">4:00pm</span>, <span class="airing-date-time">5:00pm</span>, <span class="airing-date-time">6:00pm</span>]'

day = ['Tue', 'Tue', 'Tue', 'Tue', 'Tue', 'Tue', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed', 'Wed']
date = ['Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 24', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25', 'Jan 25']
time = ['6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm', '12:00am', '1:00am', '4:00am', '5:00am', '10:00am', '11:00am', '11:00am', '12:00pm', '12:00pm', '1:00pm', '1:00pm', '2:00pm', '2:00pm', '3:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm']
channel = ['WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WE', 'WGNA', 'TNT', 'WE', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'WE', 'ION', 'ION', 'ION', 'ION']


# days_list = []
# date_list = []
# time_list = []
# channel_list = []

# for x in day:
#     days_list.append(x.text)
#
# for x in date:
#     date_list.append(x.text)
#
# for x in time:
#     time_list.append(x.text)
#
# for x in channel:
#     channel_list.append(x.text)
#
# print(days_list, date_list, time_list, channel_list)


for i,show in enumerate(day):
    new_show = []
    new_show.append(day[i])
    new_show.append(date[i])
    new_show.append(time[i])
    new_show.append(channel[i])
    all_showings.append(new_show)

print(all_showings)
