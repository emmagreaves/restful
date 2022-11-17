from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def initial():

    if 'vericlass_outside_class' in request.args:
        x = request.args.get('vericlass_outside_class')
        y = request.args.get('vericlass_in_class')
        return render_template("prefilled.html", x=x, y=y)
    else:
        return render_template("index.html")

@app.route("/calculated", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        x = float(request.form.get("homeworkHours"))
        y = float(request.form.get("lectureHours"))
        z = float(request.form.get("outsideHours"))
        s = float(request.form.get("sectionHours"))
        coeff = 0.1917802797
        mincoeff= 0.02783
        number = round((coeff)*(x/7 + y/5 + z/7 + s/5)*60)
        # minNumber = round((mincoeff)*(x/7 + y/5 + z/7 + s/5)*60)
        # number = round((researchNumber + minNumber)/2)
        return render_template("calculated.html", number = number)
    else:
        return render_template("index.html")

