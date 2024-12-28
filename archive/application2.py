from flask import Flask

application = Flask(__name__)  # Rename app to application for Gunicorn compatibility

@application.route('/')
def home():
    return "Hello, World! Welcome to my Flask App!"

@application.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)