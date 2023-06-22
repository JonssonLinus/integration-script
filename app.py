from flask import Flask, request

app = Flask(__name__)

@app.route('patient_email', methods=['GET'])
def process_url(patient_email):
    # Use the script_parameter in your script execution
    # For example, print it to the console
    url = request.args.get('url')

    # Execute your script using the information from the URL
    # Add your script execution logic here

    return redirect(url_for('http://www.google.com'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)