from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_script/patient_email')
def execute_script(patient_email):
    # Use the script_parameter in your script execution
    # For example, print it to the console
    print('Script parameter:', patient_email)

    # Execute your script using the information from the URL
    # Add your script execution logic here

    return 'Script executed successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)