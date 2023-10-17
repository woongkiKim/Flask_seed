from flask import Flask, request, render_template
import pandas as pd

from modules.dataPreprocess import DataCleansing

app = Flask(__name__)

cleansing = DataCleansing()


@app.route("/")
def index():
    df = pd.DataFrame()
    return render_template("index.html", df=df)


@app.route("/predict", methods=["POST"])
def predict():
    global df  ## 전역변수로 df를 사용합니다.

    try:
        if request.method == "POST":
            # 입력 데이터 받기
            data = request.form
            data = request.form.to_dict()  # 폼 데이터를 딕셔너리로 변환

            # 딕셔너리를 데이터 프레임으로 변환
            df = pd.DataFrame(data, index=[0])

            print("\n ============= ⭐️ 입력 데이터:\n ", df, "\n =============")

            cleansing.preprocess(df)

            return render_template("index.html", df=df)

        else:
            print("⭐️ 잘못된 접근입니다.")
            return render_template("index.html", df=df)

    except Exception as e:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
