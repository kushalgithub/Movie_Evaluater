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
    geo = ' 40.7142700,-74.0059700,1000mi'  # new york

    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print   tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex2():
    geo = "29.7604,-95.3698,10000mi"  # huston
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex3():
    geo = '39.9526,-75.1652,10000mi'  # phili
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex4():
    geo = '29.4241,-98.4936 ,10000mi'  # san anto
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex5():
    geo = ' 33.4483771, -112.0740373,1000mi'  # Phoenix
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print   tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex6():
    geo = "30.3321838.-81.65565099999999,10000mi"  # Jacksonville
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex7():
    geo = '39.9611755,-82.99879419999999,10000mi'  # Ohio
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex8():
    geo = '35.1495343,-90.0489801 ,10000mi'  # Tennessee
    tweets = myApi.search(q="#everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex9():
    geo = '39.7392358, -104.990251,10000mi'  # Colorado
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


def rest_query_ex10():
    geo = '39.2903848,-76.6121893 ,10000mi'  # Maryland
    tweets = myApi.search(q="everything, everything", geocode=geo)
    for tweet in tweets:
        print  tweet.text
        observation = {"text": tweet.text}
        with open('everything.txt', 'a+') as f1:
            f1.write(json.dumps(str(observation)))
            f1.write("\n")
            f1.write("\n")


if __name__ == '__main__':
    rest_query_ex1()
    rest_query_ex2()
    rest_query_ex3()
    rest_query_ex4()
    rest_query_ex5()
    rest_query_ex6()
    rest_query_ex7()
    rest_query_ex8()
    rest_query_ex9()
    rest_query_ex10()
