from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

historia_zakupow = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', zakupy=historia_zakupow)

@app.route('/dodaj_zakup', methods=['POST'])
def dodaj_zakup():
    global historia_zakupow

    imie = request.form['imie']
    data_str = request.form['data']
    ilosc_str = request.form['ilosc']

    try:
        data = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
        ilosc = int(ilosc_str)

        historia_zakupow.append((imie, data, ilosc))

    except ValueError:
        return "Nieprawidłowy format danych. Spróbuj ponownie."

    return render_template('index.html', zakupy=historia_zakupow)

if __name__ == '__main__':
    app.run(debug=True)