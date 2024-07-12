import speech_recognition as sr
import pyttsx3 

#Initialize the recognizer 
r = sr.Recognizer() 
while(True):
            #Use the microphone as source for input.
            with sr.Microphone() as source2: 
                        #Wait for a second to let the recognizer
                        #adjust the energy threshold based on
                        #the surrounding noise level                         
                        r.adjust_for_ambient_noise(source2, duration=0.2)
                        #Listens for the user's input 
                        audio2 = r.listen(source2)
            
                        #Using google to recognize audio
                        MyText = r.recognize_google(audio2, language='en-US')
                        MyText = MyText.lower()
            
                        print("Did you say ", MyText)