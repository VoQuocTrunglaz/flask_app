from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <div style="font-family: Arial, sans-serif; text-align: center; margin-top: 20%; background-color: #e6f3ff; padding: 20px; border-radius: 10px; width: 300px; margin-left: auto; margin-right: auto;">
        <h1 style="color: #2c3e50;">Xin chào!</h1>
        <p style="color: #7f8c8d; font-size: 18px;">Mình là Trung!</p>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
