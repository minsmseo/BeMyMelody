from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import librosa
import numpy as np

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

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # 음원 로드
        y, sr = librosa.load(filepath, sr=None)
        # 코드 추출: 여기서는 피치를 기반으로 단순 루트 추정
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        chords = extract_chords(chroma)

        return jsonify({"chords": chords})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def extract_chords(chroma):
    # 크로마에서 각 시간 프레임마다 가장 강한 음을 추출
    chord_names = ['C', 'C#', 'D', 'D#', 'E', 'F',
                   'F#', 'G', 'G#', 'A', 'A#', 'B']
    chords = []
    for i in range(chroma.shape[1]):
        strongest = np.argmax(chroma[:, i])
        chords.append(chord_names[strongest])
    return chords


@app.route('/',methods=['GET'])
def index():
    return "🎵 BeMyMelody Flask Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)