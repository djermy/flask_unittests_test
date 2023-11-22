from flask import current_app as app, jsonify

@app.route('/')
def health():
    return jsonify({'message': 'hello world!'})

@app.route('/double/<num>')
def double(num):
    try:
        num = float(num)
        return jsonify({f'value': num*2})
    except ValueError:
        return jsonify({'message': f'ERROR [{num}] is not an integer or float!'}), 400 

@app.route('/half/<num>')
def half(num):
    try:
        num = float(num)
        return jsonify({f'value': num/2})
    except ValueError:
        return jsonify({'message': f'ERROR [{num}] is not an integer or float!'}), 400 

@app.route('/power_of_<power>/<num>')
def power(power, num):
    try:
        num = float(num)
        power = float(power)
        return jsonify({f'value': num**power})
    except ValueError:
        return jsonify()({'message': f'ERROR [{num}] is not an integer or float!'}), 400 