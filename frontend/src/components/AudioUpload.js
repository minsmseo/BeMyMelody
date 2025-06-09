import React, { useState } from 'react';

const AudioUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!selectedFile) {
      alert('Please select a file first!');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        console.log('Server response:', data);
        alert(`Received chords: ${data.chords}`);
      })
      .catch((err) => {
        console.error(err);
        alert('Upload failed.');
      });
  };

  return (
    <div>
      <h2>🎵 Upload your melody</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="audio/*" onChange={handleChange} />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
};

export default AudioUpload;
