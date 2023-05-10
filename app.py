from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

historia_zakupow = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dodaj_zakup', methods=['POST'])
def dodaj_zakup():
    imie = request.form['imie']
    data_str = request.form['data']
    ilosc_str = request.form['ilosc']

    try:
        data = datetime.datetime.strptime(data_str, "%Y-%m-%d").date()
        ilosc = int(ilosc_str)

        historia_zakupow.append((imie, data, ilosc))

    except ValueError:
        return "Nieprawidłowy format danych. Spróbuj ponownie."

    return render_template('index.html')

@app.route('/historia_zakupow')
def historia_zakupow():
    return render_template('historia.html', historia=historia_zakupow)

if __name__ == '__main__':
    app.run(debug=True)
