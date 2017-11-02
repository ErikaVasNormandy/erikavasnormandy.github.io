
import flask, flask.views
import os


app = flask.Flask(__name__)
app.secret_key="Jaffa"

class View(flask.views.MethodView):
	def get(self):
		return flask.render_template('index.html')

	def get('/sickOS'):
		return flask.render_template('/sickOS/sickOS.html')

	def post(self):
		#return flask.request.form['expression']
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods = ['GET', 'POST'])

app.debug = True

app.run()
