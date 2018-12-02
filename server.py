from flask import Flask

app = Flask('isItElevenEleven')

@app.route("/")
def hello_world():
	html = "<div>Hello World! The application server has served up some HTML.</div>"
	return html

app.run(host='0.0.0.0', port=80)
