from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/sickOS')
def sickOS():
	return render_template("sickOS.html")

if __name__ == '__main__':
	app.run(debug=True);
