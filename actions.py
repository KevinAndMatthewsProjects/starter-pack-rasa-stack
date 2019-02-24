# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from alpha_vantage.timeseries import TimeSeries
from random import randint

import logging
import requests
import json
from rasa_core_sdk import Action

logger = logging.getLogger(__name__)

''' Rasa Custom Action that runs when user uses the stock command.
    Usage: stock [symbol] where the symbol is case insensitive.
    The action reads the symbol and tells the user relevant stock information.
    Utilizes the open source AlphaVantage Python wrapper API:
    https://github.com/RomelTorres/alpha_vantage
'''
class StockInfo(Action):
    def name(self):
        return "action_stockInfo"
    def run(self, dispatcher, tracker, domain):
        apiKeysList = ['M79VIZP56M8PZX9G','KLY5YQTR8LV6H8WL', '3Q2HALY82A6I4QRC']
        apiKey = apiKeysList[randint(0, 2)]
        inpt = str(tracker.latest_message["text"])
        sym = inpt.split("stock")[1].replace(" ", "")
        res = ""
        try:
            ts = TimeSeries(key=apiKey, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=sym,interval='1min', outputsize='compact')
            info = data.tail(1).values.tolist()[0]
            res =  "At time " + data.tail(1).index.format()[0] + " EST: \nThe opening price of " + str(sym) + " was " + str(info[4]) + ". The low is " + str(info[3]) + ". The high is " + str(info[1]) + "."
            dispatcher.utter_message(res)
        except Exception as e:
            res = "That was not a valid stock symbol."
            dispatcher.utter_message(res)
        return []
class HealthArticles(Action):
    def name(self):
        return "action_healthArticles"
    def run(self, dispatcher, tracker, domain):
        try:
            generated = set()
            indices = []
            inpt = str(tracker.latest_message["text"])
            searchTopic = "health " + inpt.split("health")[1]
            topic = inpt.split("health")[1]
            if searchTopic == " ":
                searchTopic = "health"
                topic = "health"
            req = requests.get("https://newsapi.org/v2/everything?q="+ searchTopic + "&from=2019-01-23&sortBy=publishedAt&apiKey=eea212d3003b4b5694d753f8612e47a8")
            res = "Here are a few articles related to " + topic + ":\n\n"
            for i in range(5):
                gen = randint(0, len(req.json()["articles"])-1)
                while gen in generated:
                    gen = gen = randint(0, len(req.json()["articles"])-1)
                generated.add(gen)
                indices.append(gen)
            for i in range(len(indices)):
                res += req.json()["articles"][indices[i]]["url"] + "\n"
            dispatcher.utter_message(res)
        except:
            dispatcher.utter_message("Sorry, I was unable to find any articles.")
        return []
    
class FinanceTips(Action):
    def name(self):
        return "action_financeTips"
    def run(self, dispatcher, tracker, domain):
        tips = ["Take bigger risks once in a while.", 
		"Invest in yourself.",
		"Know how much you spend.", 
		"Always have cash if you need it.", 
		"Start saving when you are young.", 
		"Do not increase spending when you get a raise.", 
		"Look at your credit report.", 
		"Use your credit card rewards.", 
		"Save for a rainy day.",
		"Fifteen minutes can save you fifteen percent or more on car insurance!",
		"When purchasing goods, consider how much you will be using it!",
		"It is wise to invest some stock options if you have some leftover!"
		"Create budgets for yourself, whether it be with food or a car!",
		"Don't forget to check your bank account once in a while!",

		
]
        dispatcher.utter_message(tips[randint(0,len(tips)-1)])
        return []
