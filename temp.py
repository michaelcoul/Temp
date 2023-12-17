from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_weather():
    response = requests.get('http://wttr.in/Tolyatti?format=%C+%t')
    return response.text

@app.route('/')
def home():
    weather = get_weather()
    return render_template('home.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)

