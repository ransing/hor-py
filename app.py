from flask import Flask , render_template,request
from horoscope import zodiac_sign
from datetime import datetime

# app = Flask("My Flask App")
app = Flask(__name__, template_folder='./templates') 
app.config['EXPLAIN_TEMPLATE_LOADING']=True 



@app.route("/") 
def default_path():
	return render_template ("home.html") 



@app.route("/horoscope", methods=["POST"])
def read_form():
	form_data = request.form
	date = datetime.strptime(form_data["dob"], '%Y-%m-%d').date()
	month = date.month
	day = date.day
	print(date)
	sign= zodiac_sign (month,day)
	print(sign)
	return render_template (sign.lower() +'.html') 



if __name__ == '__main__':
	app.run(debug=True)
