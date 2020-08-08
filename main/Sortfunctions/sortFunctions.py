import os

from flask import Flask, render_template, request

from main.DB.fishDB import sortfishnameasc, sortfishnamedsc, sortsizeasc, sortsizedsc, sortdateasc, sortdatedsc, \
    sorttimeasc, sorttimedsc, sortbaitasc, sortbaitdsc
from main.DB.lakesDB import sortlakeasc, sortlakedsc, sortlocationasc, sortlocationdsc, \
    sortpriceasc, sortpricedsc, sortfishasc, sortfishdsc

app = Flask(__name__)
sorttmp: int = 1


def sortlake_byname():
    global sorttmp
    if sorttmp is 1:
        tavak = sortlakeasc()
        sorttmp = 2
    else:
        tavak = sortlakedsc()
        sorttmp = 1
    return render_template("tavak.html", tavak=tavak)


def sortlake_bylocation():
    global sorttmp
    if sorttmp is 1:
        tavak = sortlocationasc()
        sorttmp = 2
    else:
        tavak = sortlocationdsc()
        sorttmp = 1
    return render_template("tavak.html", tavak=tavak)


def sortlake_byprice():
    global sorttmp
    if sorttmp is 1:
        tavak = sortpriceasc()
        sorttmp = 2
    else:
        tavak = sortpricedsc()
        sorttmp = 1
    return render_template("tavak.html", tavak=tavak)


def sortlake_byfish():
    global sorttmp
    if sorttmp is 1:
        tavak = sortfishasc()
        sorttmp = 2
    else:
        tavak = sortfishdsc()
        sorttmp = 1
    return render_template("tavak.html", tavak=tavak)


#########################################

def sortfish_byname():
    global sorttmp
    if sorttmp is 1:
        fishs = sortfishnameasc()
        sorttmp = 2
    else:
        fishs = sortfishnamedsc()
        sorttmp = 1
    return render_template("halfajok.html", fishlist=fishs)


def sortfish_bysize():
    global sorttmp
    if sorttmp is 1:
        fishs = sortsizeasc()
        sorttmp = 2
    else:
        fishs = sortsizedsc()
        sorttmp = 1
    return render_template("halfajok.html", fishlist=fishs)


def sortfish_bydate():
    global sorttmp
    if sorttmp is 1:
        fishs = sortdateasc()
        sorttmp = 2
    else:
        fishs = sortdatedsc()
        sorttmp = 1
    return render_template("halfajok.html", fishlist=fishs)


def sortfish_bytime():
    global sorttmp
    if sorttmp is 1:
        fishs = sorttimeasc()
        sorttmp = 2
    else:
        fishs = sorttimedsc()
        sorttmp = 1
    return render_template("halfajok.html", fishlist=fishs)


def sortfish_bybait():
    global sorttmp
    if sorttmp is 1:
        fishs = sortbaitasc()
        sorttmp = 2
    else:
        fishs = sortbaitdsc()
        sorttmp = 1
    return render_template("halfajok.html", fishlist=fishs)
