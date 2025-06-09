# 🎶 BeMyMelody

BeMyMelody is a web application that analyzes uploaded melody audio files, automatically generates chords, and plays them together in a new audio output.

## 💡 Features

- [x] Upload melody audio files (.mp3, .wav)
- [x] Extract pitch from audio (melody analysis)
- [x] Automatically generate chord progressions
- [ ] Render and play combined melody + chord audio

## 🛠 Tech Stack

### Frontend
- React
- Tone.js (for audio playback)

### Backend
- Python (Flask)
- Librosa (for audio analysis)
- PrettyMIDI / Music21 (for MIDI and chord generation)

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/your-username/BeMyMelody.git
cd BeMyMelody
