import tkinter as tk
from tkinter.constants import DISABLED, NORMAL, CURRENT
from api_in import main
import pyaudio
import keyboard
import time
import wave
import os
from aud2text import transcriber_words 
from slangLib import library
 
#https://www.dictionary.com/e/slang/ till page 5
    
key_words = []
prompt = ""
global b 
b=""

voice_is_on = False

def vocierec2():
        
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
                

                  # Add the label to the window
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

     
#function to handle when the user presses the enter button, calls parse word term
def enter_prompt():
     input = txt_prompt.get("1.0","end")
     txt_prompt.delete("1.0", "end")
     parse_word_term(input)

#clears the current prompt and allows the user to enter a new one
def change_prompt():
     txt_def.config(state=NORMAL)
     txt_prompt.config(state=NORMAL)
     txt_def.delete("1.0", "end")
     txt_prompt.delete("1.0", "end")
     key_words.clear()
     txt_def.config(state=DISABLED)
     
def voice_input():
     global voice_is_on
     status="off"
     if voice_is_on:
          voice_is_on = False
          voice_prompt.config(text="Click to start",bg='green') 
     
     
        
     else:
          voice_prompt.config(text="Click to prime", bg='red')
          voice_is_on = True
          a=vocierec2()
          
          global b
          b=""
          status="on"
          for char in a:
             b += char.lower() 
          print(b)
          txt_prompt.insert(tk.END, b)
          

             

#when a highlighted word is clicked on use the urban dictionary api to fetch the definition and other useful information
def print_def(event):
     txt_def.config(state= NORMAL)
     txt_def.delete("1.0","end")
     idx = int(event.widget.tag_names(CURRENT)[1])
     output = main(key_words[idx])
     space_left = 70
     for segment in output.split():
          if len(segment) < space_left and segment == "Definition:":
               txt_def.insert(tk.END, '\n' + '\n' + segment + '\n')
               space_left = 70
          elif len(segment) < space_left and segment == "Example:":
               txt_def.insert(tk.END, '\n' + '\n' + segment + '\n')
               space_left = 70

          elif len(segment) < space_left:
               txt_def.insert(tk.END, segment + " ")
               space_left = space_left - (len(segment) + 1)
          else:
               space_left = 70
               txt_def.insert(tk.END, segment + '\n')
# breaks the input string into many substrings, compares each word in the input to a library of key words
# clears the input and re prints it with key words marked in blue, when these words are clicked on call the
# print_def function
def parse_word_term(statement):
     
     statement_list = statement.split()
     words_processed = 0
     index = 0
     while words_processed < len(statement_list):

          if statement_list[words_processed] in library:
               txt_prompt.insert(tk.END,statement_list[words_processed]+ " ",('slang', str(index)))
               key_words.append(statement_list[words_processed])
               index = index + 1
               words_processed = words_processed + 1
          elif words_processed < len(statement_list)-1:
               if statement_list[words_processed] + " " + statement_list[words_processed + 1] in library:
                    txt_prompt.insert(tk.END, statement_list[words_processed] + " " + statement_list[words_processed + 1] + " ", ('slang', str(index)))
                    key_words.append(statement_list[words_processed] + " " + statement_list[words_processed + 1])
                    words_processed = words_processed + 2
                    index = index + 1
               else:
                    txt_prompt.insert(tk.END, statement_list[words_processed] + " ")
                    words_processed = words_processed + 1
          else:
               txt_prompt.insert(tk.END, statement_list[words_processed] + " ")
               words_processed = words_processed + 1

     txt_prompt.config(state = DISABLED)

window = tk.Tk()
window.title("slang translator")
window.geometry("1080x1920")
label_start = tk.Label(window, text="Press space to start/stop ")

#create labels for the gui, these will be static and not change
prompt = tk.Label(window, text= "Current Prompt")
def_label = tk.Label(window, text = "Definition")
#create text boxes for prompt and definition
txt_prompt = tk.Text(window, height = 5, width = 45)
txt_def = tk.Text(window, height = 15, width = 90)
#create a button for the user to enter the next prompt
next_prompt = tk.Button(window, text= "New Prompt", command = change_prompt)
enter_prompt = tk.Button(window, text= "Enter", command = enter_prompt)
voice_prompt = tk.Button(window, text= "Toggle Voice", command = voice_input)
#now attach the created elements to the window
prompt.pack()
txt_prompt.pack()
def_label.pack()
txt_def.pack()
next_prompt.pack()
enter_prompt.pack()
voice_prompt.pack()
label_start.pack()

     

  

    

txt_def.config(state=DISABLED)
txt_prompt.tag_config('slang', foreground="blue")
txt_prompt.tag_bind('slang', '<Button-1>', print_def)

window.mainloop()
    