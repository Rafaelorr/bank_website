from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        naam = request.form.get("naam")
        wachtwoord = request.form.get("wachtwoord")
        begin_cash = request.form.get("begin_cash")
        print(naam)
        print(wachtwoord)
        print(begin_cash)
    return render_template("sign_up.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")