from abc import ABC
import psycopg2
from bs4 import BeautifulSoup
import requests
from html.parser import HTMLParser
import random

top_25 = []


class BestSub:
    def __init__(self):
        with open("DBCredentials.txt") as db_stuff:
            db_credentials = db_stuff.readlines()
            db_name = db_credentials[0].strip("\n")
            db_pass = db_credentials[1].strip("\n")
            db_host = db_credentials[2].strip("\n")
            db_port = db_credentials[3].strip("\n")
        try:
            conn = psycopg2.connect(database=db_name,
                                    user=db_name,
                                    password=db_pass,
                                    host=db_host,
                                    port=db_port)
            cursor = conn.cursor()
            print(conn.get_dsn_parameters(), "\n")
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            print("Connected to", record, "\n")
        except(Exception, psycopg2.Error) as error:
            print("Error", error)
        finally:
            if conn:
                cursor.close()
                conn.close()

    # noinspection PyMethodMayBeStatic
    def get_best(self):
        global top_25
        proxy = requests.get('https://free-proxy-list.net/')
        soup = BeautifulSoup(proxy.content, 'html.parser')
        table_body = soup.find('tbody')
        row = table_body.find('tr')
        proxy_num = row.find('td')
        proxy_num = proxy_num.text

        proxies = {
            "http": proxy_num,
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }
        page = requests.get('https://www.reddit.com/subreddits/leaderboard/', headers=headers, proxies=proxies)
        soup = BeautifulSoup(page.content, features='html.parser')
        popular_subs = soup.find_all('li', attrs={'class': "_267lcOmg8VvXcoj9O0Q1TB"})
        parser = MyHTMLParser()
        parser.feed(str(popular_subs))
        rand_num = random.randint(0, 24)
        random_top = top_25[rand_num]  # Add this random to DB.
        # print(random_top)


class MyHTMLParser(HTMLParser, ABC):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if "/r/" in attr[1]:
                top_25.append(attr[1])


# just testing functionality
bs = BestSub()
# bs.get_best()
