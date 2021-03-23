
import difflib

dictionary = {
    #add conversations here in the format -  "what is your name":"my name is lydia"
}

words = list(dictionary.keys())
def word_check(s):
    
    if s not in words:
        answer = difflib.get_close_matches(s, words, 3, 0.3)
        botans = (f'{",".join(str(x) for x in answer)}')
        #print(botans)
        botans = botans[0:botans.find(",")]
        #print(botans)
        print(dictionary.get(botans))
while True:
    s = input(">>>>")
    s = str(s)
    word_check(s)
        