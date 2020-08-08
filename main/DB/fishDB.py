from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

c = MongoClient(host="localhost", port=27017)
dbh = c["FISHING_APPLICATION"]


def savefish(fish):
    hal = {
        "name": fish.name,
        "size": fish.size,
        "date": fish.date,
        "time": fish.time,
        "bait": fish.bait
    }

    dbh.Fish.insert_one(hal)


def allfish():
    fishs = dbh.Fish.find({})
    fish_list = []
    for fish in fishs:
        fish_list.append(fish)

    return fish_list


def allfishs_bydate(date):
    fishs = dbh.Fish.find({"date": date})
    fish_list = []
    for fish in fishs:
        fish_list.append(fish)
    return fish_list


def sortfishnameasc():
    fishs = dbh.Fish.find().sort("name")
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortfishnamedsc():
    fishs = dbh.Fish.find().sort("name", -1)
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortsizeasc():
    fishs = dbh.Fish.find().sort("size")
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortsizedsc():
    fishs = dbh.Fish.find().sort("size", -1)
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortdateasc():
    fishs = dbh.Fish.find().sort("date")
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortdatedsc():
    fishs = dbh.Fish.find().sort("date", -1)
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sorttimeasc():
    fishs = dbh.Fish.find().sort("time")
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sorttimedsc():
    fishs = dbh.Fish.find().sort("time", -1)
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortbaitasc():
    fishs = dbh.Fish.find().sort("bait")
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak


def sortbaitdsc():
    fishs = dbh.Fish.find().sort("bait", -1)
    halak = []
    for fish in fishs:
        halak.append(fish)
    return halak
