from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    server_data = {
        'first_name' : 'Levi',
        'last_name' : 'Gotsman',
    }
    
    return render_template('index.html', server_data=json.dumps(server_data))


@app.route('/fluffybunnies/<id>')
def fluffybunnies(id):
    return render_template('fluffybunnies.html',id=id)

@app.route('/data')
def data():
    some_data = [
        {
            'item': 'Chair',
            'price': 15.99,
            'image': 'https://www.potterybarn.com/pbimgs/rk/images/dp/wcm/201824/0483/trieste-dining-chair-o.jpg?01AD=3XvrvPmLuAg_Hy9Z-_Aaaj1reuZ3Qn7ONQBpTkNOZnyuqLGCRVWbG_w&01RI=9431F8ADB7C8497&01NA='
        },
        {
            'item': 'Desk',
            'price': 104.77,
            'image': 'https://target.scene7.com/is/image/Target/15451685'
        },
    ]
    return json.dumps(some_data)
    
    
if __name__ == "__main__":
    app.run(debug=True)