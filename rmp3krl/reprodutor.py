# oh viadagem viu
from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("C:\Users\deour\Downloads\SnapInsta.io - I See the Light (from Disney's Tangled) Violin Cover - Taylor Davis (320 kbps).mp3")
play(song)