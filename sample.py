import playsound #play final audio
import speech_recognition as sr #speech to text recognition 
from gtts import gTTS #translated text to speech
from tkinter import * #ui design for future
from translate import Translator #translate text
import os #os interactions


dic=('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 
     'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
 'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
     'bs', 'bulgarian', 'bg', 'catalan', 'ca',
  'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
     'zh-cn', 'chinese (traditional)', 'zh-tw',
  'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
     'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
  'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi', 
     'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
  'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati', 
     'gu', 'haitian creole', 'ht', 'hausa', 'ha', 
  'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong', 
     'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
  'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it', 
     'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
  'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
     'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
  'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
     'lb', 'macedonian', 'mk', 'malagasy',
  'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
     'mi', 'marathi', 'mr', 'mongolian', 'mn',
  'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
     'odia', 'or', 'pashto', 'ps', 'persian',
   'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
     'romanian', 'ro', 'russian', 'ru', 'samoan',
   'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 
     'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
   'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so', 
     'spanish', 'es', 'sundanese', 'su', 
  'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
     'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
  'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 
     'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
  'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')

def takecommand(lang): #speech recognition implement
   r = sr.Recognizer()
   with sr.Microphone() as source:
      print("listening.....")
      r.pause_threshold = 1
      audio = r.listen(source)
  
   try:
      print("Recognizing.....")
      query = r.recognize_google(audio, language=lang)
      print(f"user said {query}\n")
   except Exception as e:
      print("say that again please.....")
      return "None"
   return query

#driver code
print('choose language....')
chooseLang = takecommand('en').lower()
while (chooseLang == "None"):
   chooseLang = takecommand('en').lower()
print(chooseLang) # hindi
chooseLang = dic[dic.index(chooseLang)+1]  #hi stored here

while True:
   print('say something')
   query = takecommand(chooseLang) #in hindi priya meri dost hai
   while (query == "None"):
      query = takecommand(chooseLang)

   def destination_language():
      print("Enter the language in which you want to convert \
      : Ex. Hindi , English , etc.") # speech english
      print()
   
      # Input destination language in which the user 
      # wants to translate
      to_lang = takecommand('en') #pass language
      while (to_lang == "None"):
         to_lang = takecommand('en')
      to_lang = to_lang.lower() #english
      return to_lang # return english
  
   to_lang = destination_language() #english

   while (to_lang not in dic):
      print("Language in which you are trying to convert\
      is currently not available ,please input some other language")
      print()
      to_lang = destination_language()
   
   to_lang = dic[dic.index(to_lang)+1] #en stored
#print(to_lang)
# invoking Translator
   translator= Translator(from_lang=chooseLang,to_lang=to_lang) #from hindi to english
   translation = translator.translate(query) #priya is my friend
#print (translation)
  
# This module is imported so that we can 
# play the converted audio

  
# The text that you want to convert to audio

  
# Language in which you want to convert
   language = to_lang #en stored
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
   myobj = gTTS(text=translation, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
   myobj.save("welcome.mp3")
  
# Playing the converted file
   playsound.playsound("welcome.mp3")
#os.system("welcome.mp3")
   os.remove("welcome.mp3")