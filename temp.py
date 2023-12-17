from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Генерация случайных данных для температуры
    # В реальном сценарии вы будете получать эти данные от Arduino и SIM800L
    temperature_data = [random.randint(20, 40) for _ in range(10)]

    # Создание графика
    plt.figure(figsize=(10,5))
    plt.plot(temperature_data)
    plt.title('Temperature Data')
    plt.grid(True)
    plt.ylabel('Temperature (°C)')
    plt.xlabel('Time')
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('home.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
