#!/usr/bin/python3
import snowboydecoder
import sys
import signal
import speech_recognition as sr
import gensim
import pyttsx3
import numpy as np
from scipy import spatial
import json
import sys
from gtts import gTTS
import os

import datetime

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python3 demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=1)
print('Listening... Press Ctrl+C to exit')

engine = pyttsx3.init("espeak")
#voices = engine.getProperty('voices')  DO Not uncomment
engine.setProperty('gender', 'female')
engine.setProperty('voice',"hindi+f2")
engine.setProperty('rate', 130)

with open('hindi_ques.json', 'r') as qa:
    data = json.load(qa)
questions = []
answers = []
for q,a in data.items():
    questions.append(q)
    answers.append(a)

model = gensim.models.KeyedVectors.load_word2vec_format('cc.hi.300.vec',limit=50000) 
# model = gensim.models.fasttext.load_facebook_vectors('cc.hi.300.bin', encoding='utf-8')
def stt():
    r = sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("SAY NOW")
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=1, phrase_time_limit=5)
        print("Processing audio now")

    try:
        print("here")
        speech = r.recognize_google(audio, language='hi_IN')
        print("You said:", speech)
        return speech
      # print("You said:",r.recognize_sphinx(audio))
    except IndexError:                                  # the API key didn't work
        print("No internet connection")
    except KeyError:                                    # the API key didn't work
        print("Invalid API key or quota maxed out")
    except LookupError:                                 # speech is unintelligible
        print("Could not understand audio")
        tts("could not understand")
    except:
        print("no audio received")
        tts("come near to me and speak clearly please")


# question = ['unkwown','how old are you', 'how are you', 'what is the time',
#   'hello','what is your name',
#  'what to do in emergency',]
# answer = ['unknown','I am 2 days old', 'I am a bot',
#  'the time is whatever you want it to be','hello there','my name is robob',
#  'call 100']

def sentenceDistance(inputSpeech):
    # distance = list(len(question))
    mindist = 1000
    min = 0
    for i in range(len(questions)):
        distance = model.wmdistance(question[i], inputSpeech)
        if(distance < mindist):
            min = i
            mindist = distance
    return min

def tts(outputSpeech):
    if not isinstance(outputSpeech, int):
        engine.say('could not understand or could not connect to internet')
        engine.runAndWait()
        return
#    outputSpeech = int(outputSpeech)
    print('OUTPUT:',answers[outputSpeech])
    #os.system('echo "' + answers[outputSpeech] + '" | festival --tts')
    #return

    #engine.say(answers[outputSpeech])
    #engine.runAndWait()

    obj = gTTS(text=answers[outputSpeech], lang='hi')
    obj.save("wel.mp3")
    os.system("mpg123 wel.mp3")


index2word_set = set(model.wv.index2word)
def avg_feature_vector(sentence, model, num_features, index2word_set):
    words = sentence.split()
    feature_vec = np.zeros((num_features, ), dtype='float32')
    n_words = 0
    for word in words:
        if word in index2word_set:
            n_words += 1
            feature_vec = np.add(feature_vec, model[word])
    if (n_words > 0):
        feature_vec = np.divide(feature_vec, n_words)
    return feature_vec

def sentenceDistanceCos(inputSpeech):
    # distance = list(len(question))
    min = 0
    mindist = 0.8
    for i in range(len(questions)):
        # dis1 = avg_feature_vector(questions[i], model=model, num_features=300, index2word_set=index2word_set)
        dist = avg_feature_vector(inputSpeech, model=model, num_features=300, index2word_set=index2word_set)
        distance = spatial.distance.cosine(dist, quesVector[i])
        # print('distance with',question[i],distance)
        if(distance < mindist):
            min = i
            mindist = distance
    print('distance',distance)
    return min

quesVector = []
def calculateInitialQuestions():
    for ques in questions:
        quesVector.append(avg_feature_vector(ques, model=model, num_features=300, index2word_set=index2word_set))

calculateInitialQuestions()

def fun():
      snowboydecoder.play_audio_file()
      try:
          print("----------------------------\n")
          print("TIME:",datetime.datetime.now())
          #stt2 = input("SAY NOW: ")
          tts(sentenceDistanceCos(stt()))

      except KeyboardInterrupt:
          print ('Keyboard Interrupt')
          sys.exit(0)

      except (OSError, RuntimeError) as err:
          print("AN ERROR OCCURED!!")

      except sr.UnknownValueError:
          print("Speech Recognition could not understand audio")
          tts("try again")

      except sr.RequestError as e:
          print("Could not request results from Speech Recognition service; {0}".format(e))
          tts("please connect to internet")



# main loop

engine.say("powered on")
#engine.runAndWait()
for i in range(0,100):
      while True:
            try:
            # do stuff
                detector.start(detected_callback=fun,
                #snowboydecoder.play_audio_file,
                interrupt_check=interrupt_callback,
                sleep_time=0.03)
            except:
                continue
            break


detector.terminate()
