from flask import Flask, request, render_template
import pandas as pd
import models

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    noc = dis = hp = wt = ac = year = origin = None  # Initialize variables outside the if block
    res = None  # Initialize res variable
    if request.method == "POST":
        noc = request.form["noc"]
        dis = float(request.form['dis'])  # Convert to float
        hp = request.form['hp']
        wt = request.form['wt']
        ac = float(request.form['ac'])  # Convert to float
        year = request.form['year']
        origin = request.form['origin']

        data = {
            'cylinders': noc,
            'displacement': dis,
            'horsepower': hp,
            'weight': wt,
            'acceleration': ac,
            'model_year': year,
            'origin': origin
        }
        sample = pd.DataFrame(data, index=[0])
        pred = models.predict(sample)
        res = "Predicted Mileage is {:.2f} Miles/Gallon".format(pred[0])

    return render_template("index.html", res=res)

if __name__ == "__main__":
    app.run(debug=True)
