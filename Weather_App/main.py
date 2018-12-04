# Weather_App/main.py

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
	return render_template(
		'weather.html',
		data=[{'name':'Boston'},
		{'name':'London'},
		{'name':'Burlington'},
		{'name':'Nashville'},
		{'name':'Hyannis'},
		{'name':'Portsmouth'},
		{'name':'Montreal'},
		{'name':'Denver'},
		{'name':'Chicago'},
		{'name':'Philadelphia'}])

@app.route("/result", methods=['GET','POST'])
def result():
	data = []
	error = None
	select = request.form.get('comp_select')
	resp = query_api(select)
	pp(resp)
	if resp:
		data.append(resp)
	if len(data) != 2:
		error = 'Bad Response from Weather API'
	return render_template(
		'result.html', data=data, error=error)

if __name__=='__main__':
	app.run(debug=True)