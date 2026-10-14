from flask import Flask, request
import math

app = Flask(__name__)

def lcm(x, y):
    if x == 0 or y == 0:
        return 0
    return abs(x * y) // math.gcd(x, y)

def valid_nat(val):
    return val.isdigit() and int(val) >= 0

@app.route('/bpalij22_gmail_com')
def lcm_endpoint():
    x = request.args.get('x', '')
    y = request.args.get('y', '')
    
    if not valid_nat(x) or not valid_nat(y):
        return 'NaN', 200, {'Content-Type': 'text/plain; charset=utf-8'}
    
    result = lcm(int(x), int(y))
    return str(result), 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)