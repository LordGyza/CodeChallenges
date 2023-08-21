#i forgot to add comments for those learning
#this part imports a random and time libraries
 
import random
import time

#defines the function of random language and lang is equal to one of the 21 languages in the list chosen at random

def ranLang():
  lang = random.randint(0,21)
  return lang

#greeting stores all the language greetings that will be randomly selected from in the def ranlang part

greeting = ["Hello","Bonjour",
"Hola","Zdravstvuyte",
"Nǐn hǎo",
"Salve","Konnichiwa",
"Guten Tag", "Okay / Plesier",
"ঠিক আছে (thik aase)",
"មិនអីទេ (Min-Ey-Te)",
"唔使客氣 (Mmm sai hak hei)",
"Graag gedaan",
"Okei / Palun",
"Ole hyvä",
"Drud",
"Sat Shri Akaal",
"As-salamu alaykum",
"Aloha",
"Shalom",
"HNamaste",
"Ayubowan",
"Sawatdi" ]

#displays to screen the choosen greeting 

print(f" Greeting in a random language: {greeting[ranLang()]} ")
  time.sleep(2.5)
