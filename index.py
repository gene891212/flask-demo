import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    temperature = random.randint(20, 30)  # 生成隨機溫度值（範例：20°C 至 30°C）
    humidity = random.randint(40, 60)  # 生成隨機濕度值（範例：40% 至 60%）
    return render_template("index.html", temperature=temperature, humidity=humidity)


if __name__ == "__main__":
    app.run(debug=True)
