from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# 카운터 값 저장
counter = 0

# Arduino에서 카운터 값을 받는 엔드포인트
@app.route('/update_sensor', methods=['POST'])
def update_sensor():
    global counter
    data = request.json  # Arduino에서 JSON 데이터를 수신
    if 'counter' in data:
        counter = data['counter']  # 카운터 값을 업데이트
        print(f"Received counter: {counter}")
        return jsonify(success=True)
    return jsonify(success=False), 400

# 웹사이트에서 카운터 값을 가져오는 엔드포인트
@app.route('/get_sensor', methods=['GET'])
def get_sensor():
    return jsonify(sensor_value=counter)  # 카운터 값을 JSON으로 반환

# 점수판 웹 페이지 렌더링
@app.route('/')
def index():
    return render_template('index.html')  # HTML 페이지 렌더링

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

