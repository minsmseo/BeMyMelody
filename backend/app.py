from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # React 요청 허용

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


#확장자 제한
ALLOWED_EXTENSIONS = {'wav','mp3','m4a'}

#파일 확장자 확인 함수
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True) # 폴더 없으면 생성
        file.save(save_path)
        return jsonify({"message": "File uploaded successfully", "path": save_path}), 200

    # --- 여기에 코드 추출 알고리즘 들어갈 예정 ---
    # 예시로 고정된 코드 리턴
    example_chords = ['C', 'G', 'Am', 'F']

    return jsonify({"error": "File type not allowed"}), 400
@app.route('/',methods=['GET'])
def index():
    return "🎵 BeMyMelody Flask Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)