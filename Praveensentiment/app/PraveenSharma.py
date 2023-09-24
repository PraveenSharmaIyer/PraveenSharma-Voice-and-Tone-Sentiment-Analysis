import Praveensentiment.praveen as pi
import speech_recognition as sr 
import librosa
import numpy as np
import tempfile
import os
recognizer=sr.Recognizer()
with sr.Microphone() as source:

    print('Clearing background noise...')
    recognizer.adjust_for_ambient_noise (source, duration=1)
    print('Waiting for your message...')
      
    recordedaudio=recognizer.listen(source) 
    print('Done recording..')

try:

    print("Printing the message..") 
    text=recognizer.recognize_google (recordedaudio, language="en-US") 
    
    print('Your message: {}'.format(text)) 
        # Save audio data to a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(recordedaudio.get_wav_data())

    # Analyze audio amplitude
    p, sr = librosa.load(temp_audio.name, sr=None)
    amplitude = np.max(np.abs(p))

    # Classify based on amplitude
    if amplitude > 0.5:  # Adjust this threshold as needed
        print("Amplitude is high, output: Anger")
    elif amplitude > 0.2:  # Adjust this threshold as needed
        print("Amplitude is medium, output: Calm")
    else:
        print("Amplitude is low, output: Sweaty")

    # Delete the temporary audio file
    os.remove(temp_audio.name)
except Exception as ex:

      print(ex)

w= str(text)
d=w.split()
m=pi.praveensentiment(d)
print("positive=",m[0],";","negative=",m[1],";","neutral=",m[2])

