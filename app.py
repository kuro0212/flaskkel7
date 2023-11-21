from flask import Flask, render_template
from flask import request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return render_template('index.html')

#Galery#

@app.route('/galery/', methods=['GET'])
def galery():
	return render_template('/galery/index.html')

@app.route('/galery/bersama/', methods=['GET'])
def bersama():
	return render_template('/galery/bersama.html')

@app.route('/galery/random/')
def random():
	return render_template('/galery/random.html')

@app.route('/galery/sendiri/')
def sendiri():
	return render_template('/galery/sendiri.html')


#contact#
@app.route('/contact/', methods=['GET'])
def contact():
	return render_template('/contact/index.html')

#about
@app.route('/about/', methods=['GET'])
def about():
	return render_template('/about/index.html')

#project
@app.route('/project/', methods=['GET'])
def project():
	return render_template('/project/index.html')


#@app.route('/about/')
#def about():
#	return render_template('/about/index.html')



if __name__ == '__main__':
	app.run(debug=True, port=8080, host='0.0.0.0')
