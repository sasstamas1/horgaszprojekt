import os

from flask import Flask, render_template, request, redirect, url_for

from main.DB.fishDB import allfish, savefish, allfishs_bydate
from main.DB.fishingDB import savefishing, allfishing, findallfishing_bylake
from main.Model.Fish import Fish
from main.Model.Fishing import Fishing
from main.Model.Lake import Lake
from main.DB.lakesDB import savelake, allLake, uniqueLake, findlake_byname, findlakeid_byname
from main.Sortfunctions.sortFunctions import sortlake_bylocation, sortlake_byname, sortlake_byprice, sortlake_byfish, \
    sortfish_byname, sortfish_bysize, sortfish_bydate, sortfish_bytime, sortfish_bybait

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html")


@app.route('/tavak')
def lakes():
    tavak = allLake()
    return render_template("tavak.html", tavak=tavak)


@app.route('/halfajok')
def fishs():
    fishlist = allfish()
    return render_template("halfajok.html", fishlist=fishlist)


@app.route('/horgaszatok')
def fishings():
    fishinglist = allfishing()
    return render_template("horgaszatok.html", fishings=fishinglist, lakes=allLake())


@app.route('/addnewlake', methods=['POST'])
def addnewlake():
    if uniqueLake(request.form['name']):
        lake = Lake(request.form['name'], request.form['location'], request.form['price'], request.form['fish'])
        savelake(lake)
        tavak = allLake()
        msg = "Sikeres mentés!"
        return render_template("tavak.html", tavak=tavak, msg=msg)

    else:
        tavak = allLake()
        error = "A tó már szerepel az adatbázisban!"
        return render_template("tavak.html", tavak=tavak, error=error)


@app.route('/<name>', methods=['POST'])
def lakedatapage(name):
    lake = findlake_byname(name)
    Fishings = findallfishing_bylake(lake['_id'])
    lake = Lake(lake['name'], lake['location'], lake['price'], lake['fish'])
    allfishonlake = []
    for fishing in Fishings:
        for fish in fishing['Fishs']:
            allfishonlake.append(fish)
    print(allfishonlake)
    return render_template("datapage.html", name=name, location=lake.location, price=lake.price, fish=lake.fish,
                           Fishings=Fishings, fishs=allfishonlake)


@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return redirect(url_for('/'))
    else:
        times = request.form.getlist('input_text1[]')
        fishs = request.form.getlist('input_text2[]')
        sizes = request.form.getlist('input_text3[]')
        baits = request.form.getlist('input_text4[]')
        date = request.form['date']
        max = len(times)
        for i in range(max):
            if fishs[i] is not '' and sizes[i] is not '' and times[i] is not '' and baits[i] is not '' \
                    and fishs[i] is not None and sizes[i] is not None and times[i] is not None and baits[i] is not None:
                savefish(Fish(fishs[i], sizes[i], date, times[i], baits[i]))
        Fishes_List = allfishs_bydate(date)
        Lake = findlakeid_byname(request.form['lake'])
        fishing = Fishing(date, Lake, Fishes_List, request.form['withwho'])
        savefishing(fishing)
        fishinglist = allfishing()
        return render_template('horgaszatok.html', fishings=fishinglist)


@app.route('/sortlakebylocation', methods=['POST'])
def sortlakebylocation():
    return sortlake_bylocation()


@app.route('/sortlakebyname', methods=['POST'])
def sortlakebyname():
    return sortlake_byname()


@app.route('/sortlakebyprice', methods=['POST'])
def sortlakebyprice():
    return sortlake_byprice()


@app.route('/sortlakebyfish', methods=['POST'])
def sortlakebyfish():
    return sortlake_byfish()


###########################################
@app.route('/sortfishbyname', methods=['POST'])
def sortfishbyname():
    return sortfish_byname()


@app.route('/sortfishbysize', methods=['POST'])
def sortfishbysize():
    return sortfish_bysize()


@app.route('/sortfishbydate', methods=['POST'])
def sortfishbydate():
    return sortfish_bydate()


@app.route('/sortfishbytime', methods=['POST'])
def sortfishbytime():
    return sortfish_bytime()


@app.route('/sortfishbybait', methods=['POST'])
def sortfishbybait():
    return sortfish_bybait()


################################################


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    os.system('sudo service mongod stop')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run()
