from flask import Flask, render_template, request

app = Flask(__name__)

def make_pattern(pattern_type, count):
    count = int(count)
    result = []

    if pattern_type == "lower":
        for i in range(1, count + 1):
            result.append("* " * i)
    elif pattern_type == "upper":
        for i in range(count, 0, -1):
            result.append("* " * i)
    elif pattern_type == "pyramid":
        for i in range(1, count + 1):
            result.append(" " * (count - i) + "* " * i)
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        pattern_type = request.form['pattern_type']
        count = request.form['count']
        output = make_pattern(pattern_type, count)
        return render_template('result.html', output=output, title=pattern_type.capitalize())
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
