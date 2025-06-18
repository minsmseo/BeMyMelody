from pydub.generators import Sine
from pydub import AudioSegment

# ffmpeg 경로가 필요하다면 명시적으로 지정
AudioSegment.converter = r"./ffmpeg-release-essentials_build/bin/ffmpeg.exe"  # 실제 ffmpeg 위치로 바꿔줘

# 음 높이(Hz) 정의: 도, 레, 미
notes = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63
}

# 각 음을 500ms로 생성
melody = (
    Sine(notes["C4"]).to_audio_segment(duration=500) +
    Sine(notes["D4"]).to_audio_segment(duration=500) +
    Sine(notes["E4"]).to_audio_segment(duration=500)
)

# 저장
melody.export("melody_CDE.wav", format="wav")

print("✅ 멜로디 생성 완료: melody_CDE.wav")