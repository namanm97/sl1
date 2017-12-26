from flask import *



app = Flask(__name__)

# Secret key for sessions
app.secret_key = "secret"

@app.route("/", methods=['GET', 'POST'])
def index():
	# Initialises balance and transaction count from session variables
	# If session keys do not exist, KeyError raised - (occurs the first time program is run)
	# Session variables initialised
	# To clear session - session.clear()
	try:
		balance = session["balance"]
		count = session["count"]
	except KeyError:
		count = session["count"] = 0
		balance = session["balance"] = 8000


	if request.method == "GET":
		return render_template("index.html", balance=balance, msg="")

	if request.method == "POST":

		# Checks if number of transactions is equal to 5
		if session["count"] == 5:
			session.clear()
			msg = "5 transactions complete"
			return render_template("index.html", balance=balance, msg=msg)

		# Checks if user clicked on Withdraw
		if request.form["action"] == 'Withdraw':

			# Checks if amount is greater than balance
			if int(request.form["amount"]) > session["balance"] :
				msg = "Cannot withdraw amount greater than balance"
				return render_template("index.html", balance=balance, msg=msg)

			# Deducts amount entered from balance and stores in session
			# Updates the number of transactions by one
			else:
				balance = balance - int(request.form["amount"])
				session["balance"] = balance
				session["count"] = session["count"] + 1
				msg = "Money Withdrawn"
				return render_template("index.html", balance=balance, msg=msg)

		# Checks if user clicked on Deposit
		elif request.form["action"] == 'Deposit':

			# Adds amount entered to balance and stores in session
			# Updates the number of transactions by one
			balance = balance + int(request.form["amount"])
			session["balance"] = balance
			session["count"] = session["count"] + 1
			msg = "Money Deposited"
			return render_template("index.html", balance=balance, msg=msg)

if __name__ == '__main__':
	app.run()
