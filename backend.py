from flask import Flask, jsonify, request
from font_convert import generate_font_bitmap,split_image
import base64
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

@app.route('/receive_img', methods=['POST'])
def receive_img():
    request_data = request.get_json()  # 获取 JSON 格式的请求体
    img = request_data.get('img', 'default_value')  # 从 JSON 中提取 img 参数
    # print(img)
    try:
        # 解码 Base64 数据
        img_data = base64.b64decode(img)
        with open("temp.png", "wb") as img_file:
            img_file.write(img_data)  # 将解码后的数据保存为文件
    except Exception as e:
        print(e)
        # response = {"status": "error", "message": str(e)}
    
    bitmap=split_image("temp.png")
    data = {
        "str":"img",
        "bitmap":bitmap
    }
    return jsonify(data)

# 运行服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5444)