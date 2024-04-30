from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')


total_spots = 100

@app.route('/count')
def get_count():
    global total_spots
    return jsonify({'count': total_spots})

@app.route('/broken_beam')
def broken_beam():
    global total_spots
    if total_spots > 0:
        total_spots -= 1
    return jsonify({'count': total_spots})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)


