from flask import Flask, jsonify, request
from font_convert import generate_font_bitmap
app = Flask(__name__)

# 创建一个简单的首页路由
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# 创建一个 /send_data 路由用于返回 JSON 数据
@app.route('/send_data', methods=['GET'])
def send_data():
    str = request.args.get('str','1')  # 获取 num 参数的列表
    bitmap=generate_font_bitmap(str)
    data = {
        "str":str,
        "bitmap":bitmap
    }
    return jsonify(data)

# 创建一个接收数据的路由
@app.route('/receive_data', methods=['POST'])
def receive_data():
    if request.is_json:
        data = request.get_json()
        return jsonify({"received_data": data}), 200
    else:
        return jsonify({"error": "Invalid JSON"}), 400

# 运行服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444)