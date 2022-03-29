import logging
import json

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

from ccxt import binance

keyboard = {}
args = {}
b = binance()

def welcome() -> None:
    args['welcome'] = 'Welcome'
    keyboard['welcome'] = [
        [
            InlineKeyboardButton('Bitcoin', callback_data='btc'),
            InlineKeyboardButton('Ethereum', callback_data='eth'),
        ],
        [
            InlineKeyboardButton('Menu', callback_data='welcome'),
        ]
    ]

def btc() -> None:
    data = b.fetch_order_book(symbol='BTC/USDT')
    args['btc'] = 'Binance BTC/USDT bids: ' + str(data['bids'][0]) + '\nBinance BTC/USDT asks: ' + str(data['asks'][0])
    keyboard['btc'] = [
        [
            InlineKeyboardButton('Refresh', callback_data='btc'),
            InlineKeyboardButton('Menu', callback_data='welcome'), 
        ],
    ]

def eth() -> None:
    data = b.fetch_order_book(symbol='ETH/USDT')
    args['eth'] = 'Binance ETH/USDT bids: ' + str(data['bids'][0]) + '\nBinance ETH/USDT asks: ' + str(data['asks'][0])
    keyboard['eth'] = [
        [
            InlineKeyboardButton('Refresh', callback_data='eth'),
            InlineKeyboardButton('Menu', callback_data='welcome'), 
        ],
    ]

def update_bidask() -> None:
    welcome()
    btc()
    eth()
