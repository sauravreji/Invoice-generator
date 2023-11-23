from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    
    client_name = request.form.get('client_name')
    item_name = request.form.get('item_name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')

    
    return render_template('invoice.html', client_name=client_name, item_name=item_name,
                           quantity=quantity, price=price)

if __name__ == '__main__':
    app.run(debug=True)
