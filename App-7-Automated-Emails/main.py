import yagmail
import pandas
from news import NewsFeed

df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date='2022-24-10', to_date = '2022-25-10')

    email = yagmail.SMTP(user="johnvermont3rd@gmail.com", password="tencpfsvbweaeweu")
    email.send(to=row['email'],
           subject=f"Your {row['interest']} news for today",
           contents=f"Hello row['name']!\n See what's on about {row['interest']} today.{news_feed.get()}\n Teodors",
           attachments="design.txt")

