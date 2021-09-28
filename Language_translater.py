from googletrans import Translator

translater = Translator()


Sentence = "How are you?"
result = translater.translate(Sentence,dest="ro")

print(result)