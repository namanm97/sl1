from flask import *
import time 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def prg9serverFunction():
	if request.method == "GET":
		return render_template("Prg9.html")

	if request.method == "POST":

		#Check if date entered in dd/mm/yyyy format and is not an invalid date
		# Eg. 31/11/2016 - November has 30 days only, not 31
		# Eg. 30/02/1998 - February will never have 30 days
		# Client Side Java Script did not validate this
		# Using Python's 'time' package and 'strptime' function to do these validations

		#Use strptime() function which raises an exception if date is invalid
		try:
			time.strptime(request.form["dob"],"%d/%m/%Y")
		except ValueError:
			msg = "You entered an invalid date! This is validated by the server-side Python Program"
			return render_template("Prg9.html", msg=msg)

		#If form fields are valid return success HTML page
		return render_template("success.html")

if __name__ == '__main__':
	app.run()
