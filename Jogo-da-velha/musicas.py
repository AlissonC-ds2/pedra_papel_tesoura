from pydub import AudioSegment
from pydub.playback import play

##Transformando as musicas em funçẽs para rodar no main script
def vitoria():
    audio = AudioSegment.from_mp3('ganhou.mp3')
    corte = audio[:4500]
    play(corte)

def empate():
    audio2 = AudioSegment.from_wav('empate1.wav')
    corte1 = audio2[:4500]
    play(corte1)

def perdeu():
    audio3 = AudioSegment.from_mp3('perdeu.mp3')
    play(audio3)

