from pydub import AudioSegment
def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav')

ogg2wav("D:\\details\\red.ogg")