from app import app
from flask import render_template
import os
import json

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/metro')
def getMetro():

	metroFile = os.path.abspath(os.path.dirname(__file__) + '/metroTable.json')
	with open(metroFile) as infile:
		metroTable =  json.load(infile)
	metroStr = json.dumps(metroTable, separators=(',',':'))

	#return render_template('index.html', metro=metroStr, boat=boatStr)
	return metroTable

@app.route('/boat')
def getBoat():
	boatFile = os.path.abspath(os.path.dirname(__file__) + '/boatTable.json')
	with open(boatFile) as infile:
		boatTable =  json.load(infile)
	boatStr = json.dumps(boatTable, separators=(',',':'))

	#return render_template('index.html', metro=metroStr, boat=boatStr)
	return boatTable
