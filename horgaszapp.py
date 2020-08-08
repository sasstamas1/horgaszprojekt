#!/usr/bin/env python
import os
import webbrowser
os.system('sudo service mongod start')
webbrowser.open("http://127.0.0.1:5000/")
os.system('python3 app.py')


