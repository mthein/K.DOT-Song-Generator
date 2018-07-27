from markov_python.cc_markov import MarkovChain
import random

mc = MarkovChain(3)

mc.add_file('phrase_bank.txt')

generated_song = ""

def generate_verse():
    new_verse = ""
    for lyric in mc.generate_text(random.randint(5,16)):
        if lyric == 'i' or lyric == "i'm" or lyric == "i'ma" or lyric == "i'mma":
            lyric = lyric.capitalize()
        if new_verse == "":
            lyric = lyric.capitalize()
        new_verse += lyric + ' '
    return new_verse

def generate_song():
    generated_song = ""
    for i in range(0,random.randint(45,55)):
        generated_song += (generate_verse() + ('\n'))
    return generated_song

print generate_song()
