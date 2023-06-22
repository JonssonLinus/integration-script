from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/process_url', methods=['GET'])
def process_url():
    # Get the URL parameter from the request
    email = request.args.get('email')
    print('E-mail address: '+ email)
    # Perform any necessary processing with the URL

    # Redirect the user's browser to a new URL
    return redirect(url_for('new_page'))

@app.route('/new_page')
def new_page():
    return "Thank you for completing the survey!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)