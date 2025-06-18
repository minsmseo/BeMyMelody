import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [chords, setChords] = useState([]);

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
      alert("Upload completed!");
    } catch (err) {
      console.error(err);
      alert("Upload failed!");
    }
  };

  const handleAnalyze = async () => {
    if (!file) return alert("Please select a file.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post("http://localhost:5000/analyze", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setChords(response.data.chords); // 분석된 코드 저장
    } catch (error) {
      console.error(error);
      alert("Chord analysis failed.");
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>🎵 Upload Melody</h2>
      <input type="file" accept="audio/*" onChange={handleFileChange} />
      <div style={{ marginTop: '10px' }}>
        <button onClick={handleUpload} style={{ marginRight: '10px' }}>
          Upload Only
        </button>
        <button onClick={handleAnalyze}>Analyze Chords</button>
      </div>

      {chords.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <h3>🎼 Chord Progression</h3>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
            {chords.map((chord, index) => (
              <span
                key={index}
                style={{
                  border: '1px solid #ccc',
                  padding: '4px 8px',
                  borderRadius: '4px',
                  backgroundColor: '#f9f9f9',
                }}
              >
                {chord}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;