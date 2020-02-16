import pyphen
import random
import re
import wordlib as wl

def get_line(length, word):
    if(word != None):
        #initial syllable count set high so while loop runs once
        syl_count = 100
        #initializes line string, which will eventually be the output
        line = ""
        line_syl = ""
        rannum = random.randint(0, length)
        containword = 0
        #generates lines until it finds a line exactly equal to length
        while (syl_count > length or containword == 0):
            containword = 0
            #resets variables every run
            syl_count = 0
            line = ""
            line_syl = ""
            line_pos = ""
            #chooses new initial first and second words
            if (int(rannum*5/3/length) == 0):
                w1 = word
                containword = 1
            else:
                w1 = random.choice(list(d))
            #adds words to line until it makes a line equal to or greater than the length
            while(syl_count < length):

                w2 = ""
                #chooses a random second word
                if (int(rannum*3/length) == 0):
                    w2 = random.choice(list(d))
                else:
                    if (check_valid(w1,word, (syl_count + d[word]['syl']) >= length) == 0):
                        w2 = word
                        if(d[w1]['syl'] + syl_count != length):
                            containword = 1
                    else:
                       w2 = random.choice(list(d))

                #print("w1: " + w1 + ", w2: " + w2)
                #checks if two word sequence is valid
                valid = wl.check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
                #if initial valid check is false, generates random second words
                #until it reaches a valid two word sequence
                while valid != 0:
                    if(valid == 1):
                        w2 = random.choice(list(d))
                    elif(valid == 2):
                        w1 = random.choice(list(d))
                    #print("w1: " + w1 + ", w2: " + w2)
                    valid = wl.check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
                #a valid two word sequence was found, adds first word to the sentence

                #makes verb plural
                if (d[w1]['pos'] == 'v'):

                    #if()
                    if (w1[len(w1)-1] == "h" or w1[len(w1)-1] == "x" or w1[len(w1)-1] == "s"):
                        line+= w1 + "es "
                        syl_count+= 1
                    else:
                        line+= w1 + "s "
                elif(w1 == "a"):
                    if(w2[0] == "a" or w2[0] == "e" or w2[0] == "i" or w2[0] == "o" or w2[0] == "u"):
                        line += w1 + "n "
                else:
                    line+=w1 + " "

                syl_count+=d[w1]['syl']
                line_syl += str(d[w1]['syl']) + " "
                line_pos += d[w1]['pos'] + " "
                #if ends in article
                if(syl_count >= length
                  and (d[w1]['pos'] == 'a'
                  or  d[w1]['pos'] == 'j'
                  or  d[w1]['pos'] == 'i'
                  or  d[w1]['pos'] == 'c'
                  or  d[w1]['pos'] == 'r')):
                    syl_count = 100
                    containword = 0
                if(syl_count == length and w2 == word):
                    containword = 0
                    syl_count = 100
                #print(line + ", containword: " + str(containword) + ", hidden w2 = " + w2)
                #makes second word the new first word, goes to top and repeats
                w1 = w2
        # print(line_syl)
        # print(line_pos)
        # return(line)
    else:
        #initial syllable count set high so while loop runs once
        syl_count = 100
        #initializes line string, which will eventually be the output
        line = ""
        line_syl = ""
        #generates lines until it finds a line exactly equal to length
        while syl_count > length:
            #resets variables every run
            syl_count = 0
            line = ""
            line_syl = ""
            line_pos = ""
            #chooses new initial first and second words
            w1 = random.choice(list(d))
            #adds words to line until it makes a line equal to or greater than the length
            while(syl_count < length):
                #chooses a random second word
                w2 = random.choice(list(d))
                #print("w1: " + w1 + ", w2: " + w2)
                #checks if two word sequence is valid
                valid = wl.check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
                #if initial valid check is false, generates random second words
                #until it reaches a valid two word sequence
                while valid != 0:
                    if(valid == 1):
                        w2 = random.choice(list(d))
                    elif(valid == 2):
                        w1 = random.choice(list(d))
                    #print("w1: " + w1 + ", w2: " + w2)
                    valid = wl.check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
                #a valid two word sequence was found, adds first word to the sentence

                #makes verb plural
                if (d[w1]['pos'] == 'v'):

                    #if()
                    if (w1[len(w1)-1] == "h" or w1[len(w1)-1] == "x" or w1[len(w1)-1] == "s"):
                        line+= w1 + "es "
                        syl_count+= 1
                    else:
                        line+= w1 + "s "
                elif(w1 == "a"):
                    if(w2[0] == "a" or w2[0] == "e" or w2[0] == "i" or w2[0] == "o" or w2[0] == "u"):
                        line += w1 + "n "
                else:
                    line+=w1 + " "
                syl_count+=d[w1]['syl']
                line_syl += str(d[w1]['syl']) + " "
                line_pos += d[w1]['pos'] + " "
                #if ends in article
                if(syl_count >= length
                  and (d[w1]['pos'] == 'a'
                  or  d[w1]['pos'] == 'j'
                  or  d[w1]['pos'] == 'i'
                  or  d[w1]['pos'] == 'c'
                  or  d[w1]['pos'] == 'r')):
                    syl_count = 100
                #makes second word the new first word, goes to top and repeats
                w1 = w2
        # print(line_syl)
        # print(line_pos)
        # return(line)

    return (line + " | " + line_pos + " | " + line_syl)

def get_haiku(word):
    rannum = random.randint(0, 2)
    if(rannum == 0):
        output = get_line(5, word) + "\n" + get_line(7, None) + "\n" + get_line(5, None)
    elif(rannum == 1):
        output = get_line(5, None) + "\n" + get_line(7, word) + "\n" + get_line(5, None)
    elif(rannum == 2):
        output = get_line(5, None) + "\n" + get_line(7, None) + "\n" + get_line(5, word)
    print(output)
