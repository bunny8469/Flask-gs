from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('Programming.html')

@app.route('/404')
def about():
	return render_template('404.html')

if __name__ == '__main__':
	app.run(Debug = True)