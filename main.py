# improts #
from flask import Flask
import csv
import json

# Open CSV File and Create List #
with open('simpleMoviesList.csv', newline='') as f:
  reader = csv.DictReader(f)
  myList = list(reader)

# Set up Flask ROutes # app = Flask('app')
app= Flask('app')

@app.route('/')
def allMovies():
 return json.dumps(myList)

@app.route('/top-five')
def topFive():
  sortedList = sorted(myList, key = lambda i: i ['avg_vote'],reverse=True)
  return json.dumps(sortedList[:5])

@app.route('/get-year/<year>')
def getYear(year):
  filteredList = []
  for i in myList:
    if int(i['year']) == int(year):
      filteredList.append(i)
  return json.dumps(filteredList) 

# Challenge: create a route to get the 10 latest movies released #