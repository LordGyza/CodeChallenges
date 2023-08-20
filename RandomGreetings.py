
import random


def ranLang():
  lang = random.randint(0,21)
  return lang
  
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
print(f" Greeting in a random language: {greeting[ranLang()]} ")