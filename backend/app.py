from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # React 요청 허용

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # --- 여기에 코드 추출 알고리즘 들어갈 예정 ---
    # 예시로 고정된 코드 리턴
    example_chords = ['C', 'G', 'Am', 'F']

    return jsonify({'chords': example_chords})
@app.route('/',methods=['GET'])
def index():
    return "🎵 BeMyMelody Flask Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)