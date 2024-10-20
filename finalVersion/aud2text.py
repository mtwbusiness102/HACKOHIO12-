import pyaudio
import keyboard
import time
import wave
import os
import warnings
import whisper
def transcriber_words():
    
    warnings.simplefilter(action='ignore', category=FutureWarning)
    model = whisper.load_model("tiny")

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio("Recorded.wav")
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # get the recognized text
    transcript = result.text
    print("Transcript:", transcript)  # Output the transcript
    
    # Call the morseCodeTranslator function
     # Output the Morse code

    return transcript  # Return the transcript
def vocierec():
        count=0
        file_path = r'C:\hackathon\Recorded.wav'
        if os.path.exists(file_path):
            os.remove(file_path)    
            count=1

        chunk = 1024
        format = pyaudio.paInt16
        channels = 2
        rate = 44100
        Output_Filename = "Recorded.wav"
        
        p = pyaudio.PyAudio()

        stream = p.open(format=format,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

        frames = []
        print("Press SPACE to start recording")
        keyboard.wait('space')
        print("Recording... Press SPACE to stop.")
        time.sleep(0.2)

        while True:
            try:
                data = stream.read(chunk)  
                frames.append(data)
            except KeyboardInterrupt:
                break
            if keyboard.is_pressed('space'):
                print("stopping recording") 
                time.sleep(0.2)
                break   

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(Output_Filename, 'wb')  
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()  


        if count==1:
            
            result=transcriber_words()
            return result




  
            


            