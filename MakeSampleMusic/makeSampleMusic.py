from pydub import AudioSegment
from pydub.generators import Sine

# 각 음 주파수(Hz) - 도, 미, 솔
notes = {
    'C4': 261.63,
    'E4': 329.63,
    'G4': 392.00
}

duration_ms = 1000  # 1초

# 음 생성 함수
def create_tone(frequency, duration):
    return Sine(frequency).to_audio_segment(duration=duration)

# 음들을 이어 붙이기
melody = create_tone(notes['C4'], duration_ms) + \
         create_tone(notes['E4'], duration_ms) + \
         create_tone(notes['G4'], duration_ms)

# wav 파일로 저장
melody.export("melody.wav", format="wav")
print("melody.wav 파일 생성 완료!")