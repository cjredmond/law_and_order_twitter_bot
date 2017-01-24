from bs4 import BeautifulSoup
import requests

base_url = "http://www.tvguide.com/tvshows/law-order/tv-listings/100255/"

all_showings = []
data = requests.get(base_url)
souper = BeautifulSoup(data.text, 'html.parser')
day = souper.find_all('span', {'class': 'airing-date-day'})
date = souper.find_all('span', {'class': 'airing-date-date'})
time = souper.find_all('span', {'class': 'airing-date-time'})
channel = souper.find_all('span', {'class': 'airing-date-channels'})

# day = '[<span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Tue</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>, <span class="airing-date-day">Wed</span>]'
# day = day.replace('[', "")
# day = day.replace(']', "")
# day = day.split(", ")
#
#
# date = '[<span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 24</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>, <span class="airing-date-date">Jan 25</span>]'
# date = day.replace('[', "")
# date = day.replace(']', "")
# date = day.split(", ")
#
#
# time = '[<span class="airing-date-time">6:00pm</span>, <span class="airing-date-time">7:00pm</span>, <span class="airing-date-time">8:00pm</span>, <span class="airing-date-time">9:00pm</span>, <span class="airing-date-time">10:00pm</span>, <span class="airing-date-time">11:00pm</span>, <span class="airing-date-time">12:00am</span>, <span class="airing-date-time">1:00am</span>, <span class="airing-date-time">4:00am</span>, <span class="airing-date-time">5:00am</span>, <span class="airing-date-time">10:00am</span>, <span class="airing-date-time">11:00am</span>, <span class="airing-date-time">11:00am</span>, <span class="airing-date-time">12:00pm</span>, <span class="airing-date-time">12:00pm</span>, <span class="airing-date-time">1:00pm</span>, <span class="airing-date-time">1:00pm</span>, <span class="airing-date-time">2:00pm</span>, <span class="airing-date-time">2:00pm</span>, <span class="airing-date-time">3:00pm</span>, <span class="airing-date-time">3:00pm</span>, <span class="airing-date-time">4:00pm</span>, <span class="airing-date-time">5:00pm</span>, <span class="airing-date-time">6:00pm</span>]'
# time = time.replace('[', "")
# time = time.replace(']', "")
# time = time.split(", ")
# print(time)


# print(day)
# print(date)
# print(time)
# print(channel)

# for i,show in enumerate(day):
#     new_show = []
#     new_show.append(day[i])
#     new_show.append(date[i])
#     new_show.append(time[i])
#     new_show.append(channel[i])
#     all_showings.append(new_show)
#
# print(all_showings)
