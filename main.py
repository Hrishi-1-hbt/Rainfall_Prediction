from flask import render_template, Flask, request
import pickle
from datetime import datetime  # To get the current year

app = Flask(__name__)
file = open("model.pkl", "rb")
random_Forest = pickle.load(file)
file.close()

@app.route("/", methods=["GET", "POST"])
def home():
    current_year = datetime.now().year
    year_range = range(current_year, 2031)  # Create a list from current year to 2026

    if request.method == "POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        pred = [Year, Month]
        res = random_Forest.predict([pred])[0]
        res = round(res, 2)
        return render_template('result.html', Month=Month, Year=Year, res=res)
    
    # Pass year range to template
    return render_template('index.html', year_range=year_range)

if __name__ == "__main__":
    app.run(debug=True)
