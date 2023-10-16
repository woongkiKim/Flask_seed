from flask import Flask, request, render_template
import pandas as pd
from modules.dataPreprocess import DataCleansing

app = Flask(__name__)

cleansing = DataCleansing()

@app.route("/")
def index():
    df=pd.DataFrame()
    return render_template("index.html", df=df)



if __name__ == '__main__':
    app.run(debug=True, port=5001)