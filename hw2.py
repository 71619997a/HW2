from flask import Flask

app = Flask(__name__)


def linkto(area):
    return '<a href="' + area + '">Go to the ' + area + '</a><br>'

@app.route('/')
def start_tour():
    return 'You are outside the house.<br>' \
        + linkto('commons')

@app.route('/commons')
def commons():
    return 'You are in the commons room.<br>' \
        + linkto('kitchen') + linkto('bathroom') + linkto('bedroom')

@app.route('/bedroom')
def bedroom():
    return 'You are in the bedroom.<br>' \
        + linkto('bathroom') + linkto('commons')

@app.route('/bathroom')
def bathroom():
    return 'You are in the bathroom.<br>' \
        + linkto('bedroom') + linkto('commons')

@app.route('/kitchen')
def kitchen():
    return 'You are in the kitchen.<br>' \
        + linkto('commons')

if __name__ == '__main__':
    app.run()

