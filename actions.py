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
    
