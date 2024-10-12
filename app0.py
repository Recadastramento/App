from flask import Flask, render_template
from sugest import sugestoes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sugestoes', methods=['GET'])
def sugestoes_route():
    return sugestoes()

if __name__ == '__main__':
    app.run(debug=True)
