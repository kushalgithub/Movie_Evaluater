# coding=utf-8
import tweepy
import sys
import json

consumer_key = 'PeH7lROp4ihy4QyK87FZg'
consumer_secret = '1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og'
access_token_key = '1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7'
access_token_secret = 'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
myApi = tweepy.API(auth)


def rest_query_ex1():
    geo_long = []
    geo_lat = []
    geo_rad = "10000mi"
    qi = []
    geo_long.append(40.7142700)
    geo_long.append(29.7604)
    geo_long.append(39.9526)
    geo_long.append(29.4241)
    geo_long.append(33.4483771)
    geo_long.append(30.3321838)
    geo_long.append(39.9611755)
    geo_long.append(35.1495343)
    geo_long.append(39.7392358)
    geo_long.append(39.2903848)

    geo_lat.append(-74.0059700)
    geo_lat.append(-95.3698)
    geo_lat.append(-75.1652)
    geo_lat.append(-98.4936)
    geo_lat.append(-112.0740373)
    geo_lat.append(-81.65565099999999)
    geo_lat.append(-82.99879419999999)
    geo_lat.append(-90.0489801)
    geo_lat.append(-104.990251)
    geo_lat.append(-76.6121893)

    qi.append("guardians of the galaxy vol. 2")
    qi.append("the boss baby")
    qi.append("smurfs")
    qi.append("the fate of the furious")
    qi.append("half girlfriend")
    qi.append("xXxe")
    qi.append("Beauty and the Beast")
    qi.append("King Arthur")
    qi.append("Get Out")
    qi.append("Moana")

    for t in range(len(geo_lat)-1):
        geocodes = str(geo_long[t]) + "," + str(geo_lat[t]) + "," + geo_rad
        tweets = myApi.search(q=qi[t], geocode=geocodes)
        for tweet in tweets:
            observation = {"text": tweet.text}
            with open(qi[t] + ".txt", 'w') as f1:
                f1.write(str(observation))

if __name__ == '__main__':
    rest_query_ex1()
