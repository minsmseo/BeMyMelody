import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("파일을 선택하세요!");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://localhost:5000/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      setResult(res.data.message + " (" + res.data.filename + ")");
    } catch (err) {
      setResult("업로드 실패: " + err.response?.data?.error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🎵 Upload Melody</h2>
      <input type="file" accept="audio/*" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      <p>{result}</p>
    </div>
  );
}

export default App;