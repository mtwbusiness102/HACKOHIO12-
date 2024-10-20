import whisper
import warnings

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


def morseCodeTranslator(text):
    low_sent = text.lower()
    letters = list(low_sent)

    MCode = ""
    for char in letters:
        if char == "a":
            MCode += ".-" + " "
        elif char == "b":
            MCode += "-..." + " "
        elif char == "c":
            MCode += "-.-." + " "
        elif char == "d":
            MCode += "-.." + " "
        elif char == "e":
            MCode += "." + " "
        elif char == "f":
            MCode += "..-." + " "
        elif char == "g":
            MCode += "--." + " "
        elif char == "h":
            MCode += "...." + " "
        elif char == "i":
            MCode += ".." + " "
        elif char == "j":
            MCode += ".---" + " "
        elif char == "k":
            MCode += "-.-" + " "
        elif char == "l":
            MCode += ".-.." + " "
        elif char == "m":
            MCode += "--" + " "
        elif char == "n":
            MCode += "-." + " "
        elif char == "o":
            MCode += "---" + " "
        elif char == "p":
            MCode += ".--." + " "
        elif char == "q":
            MCode += "--.-" + " "
        elif char == "r":
            MCode += ".-." + " "
        elif char == "s":
            MCode += "..." + " "
        elif char == "t":
            MCode += "-" + " "
        elif char == "u":
            MCode += "..-" + " "
        elif char == "v":
            MCode += "...-" + " "
        elif char == "w":
            MCode += ".--" + " "
        elif char == "x":
            MCode += "-..-" + " "
        elif char == "y":
            MCode += "-.--" + " "
        elif char == "z":
            MCode += "--.." + " "
        elif char == "1":
            MCode += ".----" + " "
        elif char == "2":
            MCode += "..---" + " "
        elif char == "3":
            MCode += "...--" + " "
        elif char == "4":
            MCode += "....-" + " "
        elif char == "5":
            MCode += "....." + " "
        elif char == "6":
            MCode += "-...." + " "
        elif char == "7":
            MCode += "--..." + " "
        elif char == "8":
            MCode += "---.." + " "
        elif char == "9":
            MCode += "----." + " "
        elif char == "0":
            MCode += "-----" + " "
        else: 
            MCode += "/"

    return MCode  # Return Morse code


"""
morse_code = morseCodeTranslator(transcriber_words())
print("Morse Code:", morse_code) 
# Run the transcriber function
transcriber_words()
"""
