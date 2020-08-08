from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

c = MongoClient(host="localhost", port=27017)
dbh = c["FISHING_APPLICATION"]


def savefishing(fishing):
    hal = {
        "date": fishing.date,
        "Lake": fishing.Lake,
        "Fishs": fishing.Fishs,
        "withwho": fishing.withwho
    }

    dbh.Fishing.insert_one(hal)


def allfishing():
    fishings = dbh.Fishing.find({})
    fishing_list = []
    for fishing in fishings:
        fishing_list.append(fishing)

    return fishing_list


def findallfishing_bylake(lakeid):
    fishings = dbh.Fishing.find({})
    fishingsonlake = []
    for fishing in fishings:
        if fishing['Lake']['_id'] == lakeid:
            fishingsonlake.append(fishing)
    return fishingsonlake
