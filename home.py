from flask import Flask, request, send_file, render_template_string
import matplotlib.pyplot as plt
import io

app = Flask(__name__)
data = []

@app.route('/', methods=['GET'])
def home():
    return render_template_string("""
        <h1>Temperature Data</h1>
        <img src="/plot" alt="Temperature Plot">
    """)

@app.route('/temperature', methods=['GET'])
def temperature():
    temp = request.args.get('temp')
    data.append(float(temp))
    return "Temperature received"

@app.route('/plot', methods=['GET'])
def plot():
    plt.figure()
    plt.plot(data)
    plt.title('Temperature data')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

