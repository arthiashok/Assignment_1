from flask import Flask, render_template, request, session, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = '9970436dddec6e16b82c62475435623fdbe7fa03'

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

BTSDB = 'BTS.db'

def fetchTable(con):

  members = []
  cur = con.execute('SELECT amount FROM members')
  for row in cur:
    members.append(list(row))

  albums = []
  cur = con.execute('SELECT album,date,image FROM albums')
  for row in cur:
    albums.append(list(row))

  concerts = []
  cur = con.execute('SELECT concert FROM concerts')
  for row in cur:
    concerts.append(list(row))

  awards = []
  cur = con.execute('SELECT quantity FROM awards')
  for row in cur:
    awards.append(list(row))

  return {'members':members, 'albums':albums, 'concerts':concerts, 'awards':awards}

@app.route('/')
def index():
  con = sqlite3.connect(BTSDB)
  BTS = fetchTable(con)
  con.close()
  return render_template('index.html', disclaimer='&copy; Arthi Ashok & BTS', members=BTS['members'], albums=BTS['albums'], concerts=BTS['concerts'], awards=BTS['awards'])

@app.route('/result', methods=['POST'])
def order():
  result = []
  for i in request.form:
      result.append(i)

  if request.form['members'] == '7':
      result.append('members correct')
  if request.form['awards'] == '93':
     result.append('awards correct')

  print(result)

  return render_template('result.html', result=(len(result)-2)/21.0*100)

  # change the -1 offset to match the number of radio button questions
  # change the 40 to match the total number of questions
