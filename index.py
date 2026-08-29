from app import app
from flask import jsonify

@app.route('/')
def index():
    return jsonify({"message": "Leo Mdz API Gerador de Contas Guedt Free Fire", "status": "active"})

if __name__ == '__main__':
    app.run()