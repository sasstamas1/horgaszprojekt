from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

from main.Model.Lake import Lake

app = Flask(__name__)

c = MongoClient(host="localhost", port=27017)
dbh = c["FISHING_APPLICATION"]


def savelake(lake):
    to = {
        "name": lake.name,
        "location": lake.location,
        "price": lake.price,
        "fish": lake.fish,
    }

    dbh.Lakes.insert_one(to)


def allLake():
    lakes = dbh.Lakes.find({})
    tavak = []
    for to in lakes:
        tavak.append(to)

    return tavak


def uniqueLake(name):
    lakes = dbh.Lakes.find({"name": name}).count()
    if lakes is 0:
        return True
    else:
        return False


def findlake_byname(name):
    lakes = dbh.Lakes.find({"name": name})
    for lake in lakes:
        return lake


def findlakeid_byname(name):
    lakes = dbh.Lakes.find({"name": name})
    for lake in lakes:
        return lake


def sortlakeasc():
    lakes = dbh.Lakes.find().sort("name")
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortlakedsc():
    lakes = dbh.Lakes.find().sort("name", -1)
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortlocationasc():
    lakes = dbh.Lakes.find().sort("location")
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortlocationdsc():
    lakes = dbh.Lakes.find().sort("location", -1)
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortpriceasc():
    lakes = dbh.Lakes.find().sort("price")
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortpricedsc():
    lakes = dbh.Lakes.find().sort("price", -1)
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortfishasc():
    lakes = dbh.Lakes.find().sort("fish")
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak


def sortfishdsc():
    lakes = dbh.Lakes.find().sort("fish", -1)
    tavak = []
    for to in lakes:
        tavak.append(to)
    return tavak
