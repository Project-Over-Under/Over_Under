from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import re
from time import sleep

def get_games(y='2022',w='4'):
    '''
    takes in a year_number and a week_number as strings and outputs a list of endpoints from www.pro-football-reference.com which lead
    to each boxscore page from that week.  NB: playoff weeks are numbered as week_17,18,19,etc.
    '''
    url = f'https://www.pro-football-reference.com/years/{y}/week_{w}.htm'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    html_links = soup.find_all('td', class_='right gamelink')
    games = [item.find('a')['href'] for item in html_links]
    return games

def get_homes(games):
    '''
    takes in a list of urls (games) and outputs a list of the home team from each game
    '''
    home_re = r'[a-z]{3}'
    homes = [re.findall(home_re,i)[3] for i in games]
    return homes

def get_seasons(games):
    '''
    takes in a list of urls (games) and outputs a list of the season_year for each game
    '''
    date_re = r'[0-9]{4}'
    seasons = [int(re.findall(date_re,i)[0]) for i in games]
    return seasons

def get_seasons_playoffs(games):
    '''
    takes in a list of urls (games) and outputs a list of the season_year for each game
    '''
    date_re = r'[0-9]{4}'
    seasons = [(int(re.findall(date_re,i)[0]))-1 for i in games]
    return seasons


def get_weeks(games,w=4):
    '''
    takes in a list of urls (games) and a week_number (as a int), then outputs a list of week_numbers
    for each game
    '''
    weeks = [w for i in games]
    return weeks

def get_week_list(games):
    '''
    takes in a list of urls (games) and outputs a list of weeks as int dtype
    '''
    week_list = []
    for game in games:
        url = f'https://www.pro-football-reference.com/{game}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        span = soup.find_all('div', class_='section_wrapper')[0].find_all('span')[0]
        span = str(span)
        week_re = r'[0-9]{1,2}'
        week = re.findall(week_re,span)
        week = week[0]
        week_list.append(week)
    return week_list

def get_home_teams(games):
    '''
    takes in a list of urls (games) and outputs a list of home_teams as string dtype
    '''
    home_teams = []
    for game in games:
        url = f'https://www.pro-football-reference.com/{game}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        href = soup.find_all('div', class_='scorebox')[0].find_all('strong')
        href = [tag for tag in href if tag.find('a')]
        team = href[1].find('a').contents[0]
        home_teams.append(team)
    return home_teams

def get_temps(games):
    '''
    takes in a list of urls (games) and outputs a list of temperature_values for each game
    '''
    temps = []
    try:
        for game in games:
            url = f'https://www.pro-football-reference.com/{game}'
            response = requests.get(url)
            wx_digits = r'\d{1,2}'
            soup = BeautifulSoup(response.content, 'html.parser')
            div_grid = soup.find_all('div', class_='content_grid')[0]
            div = div_grid.find_all('div')[0]
            div_wrap = div.find_all('div')[0]
            soup_wrap4 = div_wrap.contents[4]
            soup4 = BeautifulSoup(soup_wrap4, 'html.parser')
            wx = soup4.find_all('td','center')[-3]
            content = str(wx.contents[0])
            temp = re.findall(wx_digits,content)[0]
            temps.append(temp)
        return temps
    except:
        pass
def get_winds(games):
    '''
    takes in a list of urls (games) and outputs a list of wind_values for each game
    '''
    winds = []
    try:
        for game in games:
            url = f'https://www.pro-football-reference.com/{game}'
            response = requests.get(url)
            wx_digits = r'\d{1,2}'
            soup = BeautifulSoup(response.content, 'html.parser')
            div_grid = soup.find_all('div', class_='content_grid')[0]
            div = div_grid.find_all('div')[0]
            div_wrap = div.find_all('div')[0]
            soup_wrap4 = div_wrap.contents[4]
            soup4 = BeautifulSoup(soup_wrap4, 'html.parser')
            wx = soup4.find_all('td','center')[-3]
            content = str(wx.contents[0])
            wind = re.findall(wx_digits,content)[2]
            winds.append(wind)
        return winds
    except:
        pass


def get_hums(games):
    '''
    takes in a list of urls (games) and outputs a list of humidity_values for each game
    '''
    hums = []
    try:
        for game in games:
            url = f'https://www.pro-football-reference.com/{game}'
            response = requests.get(url)
            wx_digits = r'\d{1,2}'
            soup = BeautifulSoup(response.content, 'html.parser')
            div_grid = soup.find_all('div', class_='content_grid')[0]
            div = div_grid.find_all('div')[0]
            div_wrap = div.find_all('div')[0]
            soup_wrap4 = div_wrap.contents[4]
            soup4 = BeautifulSoup(soup_wrap4, 'html.parser')
            wx = soup4.find_all('td','center')[-3]
            content = str(wx.contents[0])
            hum = re.findall(wx_digits,content)[1]
            hums.append(hum)
        return hums
    except:
        pass



def create_wx_df(y='2022',w='4',s=100):
    '''
    takes in a year_number (string), week_number (string), and a number_of_seconds (int), then
    outputs a WEEKLY DataFrame which includes 6 columns: Season-Week-Home_Team-Temperature-Wind-Humidity
    '''
    games = get_games(y=y,w=w)
    home_teams = get_home_teams(games)
    sleep(s)
    seasons = get_seasons(games)
    weeks = get_week_list(games)
    sleep(s)
    temps = get_temps(games)
    sleep(s)
    winds = get_winds(games)
    sleep(s)
    hums = get_hums(games)
    sleep(s)
    df = pd.DataFrame({
        'schedule_season':seasons,
        'schedule_week':weeks,
        'team_home':home_teams,
        'weather_temperature':temps,
        'weather_wind_mph':winds,
        "weather_humidity":hums 
    })
    return df



def create_wx_df_playoffs(y='2022',w='4',s=100):
    '''
    takes in a year_number (string), week_number (string), and a number_of_seconds (int), then
    outputs a WEEKLY DataFrame which includes 6 columns: Season-Week-Home_Team-Temperature-Wind-Humidity
    '''
    games = get_games(y=y,w=w)
    home_teams = get_home_teams(games)
    sleep(s)
    seasons = get_seasons_playoffs(games)
    temps = get_temps(games)
    sleep(s)
    winds = get_winds(games)
    sleep(s)
    hums = get_hums(games)
    sleep(s)
    df = pd.DataFrame({
        'schedule_season':seasons,
        'team_home':home_teams,
        'weather_temperature':temps,
        'weather_wind_mph':winds,
        "weather_humidity":hums 
    })
    return df

def create_wx_df_mult(year,weeks,s=100):
    '''
    takes in a year (string), a list of weeks (strings), and a number_of_seconds (int) to sleep/delay between scrapes
    then outputs a single YEARLY DataFrame which includes 6 columns: Season-Week-Home_Team-Temperature-Wind-Humidity
    '''
    dfs = []
    for i in weeks:
        df = create_wx_df(y=year,w=i,s=s)
        dfs.append(df)
    return pd.concat(dfs,ignore_index=True)