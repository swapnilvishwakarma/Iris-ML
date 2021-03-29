from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('iris.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template('predict.html', data=pred)

@app.route('/predict', methods=['POST'])
def api_prediction(url, form_data):
    r = requests.post(url, data=form_data)
    htmlText = r.text
    soup = BeautifulSoup(htmlText, 'html.parser')
    print(soup.find('h2').text)
    print(soup.find_all('h1')[-1].text)

if __name__ == "__main__":
    app.run(debug=True)
