import weather_fun
import logging
from flask import Flask, render_template, request

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
handler = logging.FileHandler('./logs/app.log')
app.logger.addHandler(handler)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Function that handles the methods triggered by the user"""
    if request.method == 'POST':
        city = request.form['search']
        app.logger.info('Someone used ur site and typed this city:')
        app.logger.info(city)
        data = weather_fun.error_checking(city)
        if data == "empty" or data == "not_found" or data == "illegal" or data == "api_error":
            # error found , renders the html page with error
            return render_template('weather.html', data=None, error=data)
        # Sends the data to the rendered html page, no errors
        return render_template('weather.html', data=data, error=None)
    elif request.method == 'GET':
        # renders the main page with no data or errors
        return render_template('weather.html', data=None, error=None)


@app.errorhandler(404)
def error404(e):
    """Handles wrong URL entered"""
    return render_template('weather.html', data=None, error=404)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
