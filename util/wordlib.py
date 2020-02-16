import pyphen
import random
import re


dic = pyphen.Pyphen(lang='nl_NL')
d={}

def sylco(word) :

    word = word.lower()

    # exception_add are words that need extra syllables
    # exception_del are words that need less syllables

    exception_add = ['serious','crucial']
    exception_del = ['fortunately','unfortunately']

    co_one = ['cool','coach','coat','coal','count','coin','coarse','coup','coif','cook','coign','coiffe','coof','court']
    co_two = ['coapt','coed','coinci']

    pre_one = ['preach']

    syls = 0 #added syllable number
    disc = 0 #discarded syllable number

    #1) if letters < 3 : return 1
    if len(word) <= 3 :
        syls = 1
        return syls

    #2) if doesn't end with "ted" or "tes" or "ses" or "ied" or "ies", discard "es" and "ed" at the end.
    # if it has only 1 vowel or 1 set of consecutive vowels, discard. (like "speed", "fled" etc.)

    if word[-2:] == "es" or word[-2:] == "ed" :
        doubleAndtripple_1 = len(re.findall(r'[eaoui][eaoui]',word))
        if doubleAndtripple_1 > 1 or len(re.findall(r'[eaoui][^eaoui]',word)) > 1 :
            if word[-3:] == "ted" or word[-3:] == "tes" or word[-3:] == "ses" or word[-3:] == "ied" or word[-3:] == "ies" :
                pass
            else :
                disc+=1

    #3) discard trailing "e", except where ending is "le"

    le_except = ['whole','mobile','pole','male','female','hale','pale','tale','sale','aisle','whale','while']

    if word[-1:] == "e" :
        if word[-2:] == "le" and word not in le_except :
            pass

        else :
            disc+=1

    #4) check if consecutive vowels exists, triplets or pairs, count them as one.

    doubleAndtripple = len(re.findall(r'[eaoui][eaoui]',word))
    tripple = len(re.findall(r'[eaoui][eaoui][eaoui]',word))
    disc+=doubleAndtripple + tripple

    #5) count remaining vowels in word.
    numVowels = len(re.findall(r'[eaoui]',word))

    #6) add one if starts with "mc"
    if word[:2] == "mc" :
        syls+=1

    #7) add one if ends with "y" but is not surrouned by vowel
    if word[-1:] == "y" and word[-2] not in "aeoui" :
        syls +=1

    #8) add one if "y" is surrounded by non-vowels and is not in the last word.

    for i,j in enumerate(word) :
        if j == "y" :
            if (i != 0) and (i != len(word)-1) :
                if word[i-1] not in "aeoui" and word[i+1] not in "aeoui" :
                    syls+=1

    #9) if starts with "tri-" or "bi-" and is followed by a vowel, add one.

    if word[:3] == "tri" and word[3] in "aeoui" :
        syls+=1

    if word[:2] == "bi" and word[2] in "aeoui" :
        syls+=1

    #10) if ends with "-ian", should be counted as two syllables, except for "-tian" and "-cian"

    if word[-3:] == "ian" :
    #and (word[-4:] != "cian" or word[-4:] != "tian") :
        if word[-4:] == "cian" or word[-4:] == "tian" :
            pass
        else :
            syls+=1

    #11) if starts with "co-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:2] == "co" and word[2] in 'eaoui' :

        if word[:4] in co_two or word[:5] in co_two or word[:6] in co_two :
            syls+=1
        elif word[:4] in co_one or word[:5] in co_one or word[:6] in co_one :
            pass
        else :
            syls+=1

    #12) if starts with "pre-" and is followed by a vowel, check if exists in the double syllable dictionary, if not, check if in single dictionary and act accordingly.

    if word[:3] == "pre" and word[3] in 'eaoui' :
        if word[:6] in pre_one :
            pass
        else :
            syls+=1

    #13) check for "-n't" and cross match with dictionary to add syllable.

    negative = ["doesn't", "isn't", "shouldn't", "couldn't","wouldn't"]

    if word[-3:] == "n't" :
        if word in negative :
            syls+=1
        else :
            pass

    #14) Handling the exceptional words.

    if word in exception_del :
        disc+=1

    if word in exception_add :
        syls+=1

    # calculate the output
    return numVowels - disc + syls

#checks if a sequence of two words is valid
def check_valid(w1,w2,lastspot):
    #sets variables for the parts of speech of the two words
    pos1 = d[w1]['pos']
    pos2 = d[w2]['pos']

    # 0 = is valid
    # 1 = second word should be changed
    # 2 = first word should be changed
        # (this should never happen because it will break the line constructor)
    #if first word is an article

    if(pos1 == 'a'):
        if(pos2 == 'n'):
            return 0
        else:
            return 1
    #if first word is a verb
    elif(pos1 == 'v'):
        #if verb -> article, adverb, preposition
        if(pos2 == 'a'
        or pos2 == 'r'
        or pos2 == 'i'):
            return 0
        else:
            return 1
    #if first word is a noun
    elif(pos1 == 'n'):
        if(pos2 == 'v'
        or pos2 == 'i'):
            return 0
        else:
            return 1
    #if first word is a adverb
    elif(pos1 == 'r'):
         if(pos2 == 'a'
         or pos2 == 'i'):
             return 0
         else:
             return 1
    #if first word is a preposition
    elif(pos1 == 'i'):
         if(pos2 == 'a'):
             return 0
         else:
             return 1
    else:
       return 0

def get_line_haiku(length, word):
    #initial syllable count set high so while loop runs once
    syl_count = 100
    #initializes line string, which will eventually be the output
    line = ""
    line_syl = ""
    rannum = random.randint(0, length)
    containword = 0
    #generates lines until it finds a line exactly equal to length
    while ((word != None and (syl_count > length or containword == 0))
           or (word == None and (syl_count > length))):
        containword = 0
        #resets variables every run
        syl_count = 0
        line = ""
        line_syl = ""
        line_pos = ""
        #chooses new initial first and second words
        if (int(rannum*5/3/length) == 0 and word != None):
            w1 = word
            containword = 1
        else:
            w1 = random.choice(list(d))
        #adds words to line until it makes a line equal to or greater than the length
        while(syl_count < length):

            w2 = ""
            #chooses a random second word
            if (int(rannum*3/length) == 0 or word == None):
                w2 = random.choice(list(d))
            else:
                if (check_valid(w1,word, (syl_count + d[word]['syl']) >= length) == 0):
                    w2 = word
                    if(d[w1]['syl'] + syl_count != length):
                        containword = 1
                else:
                   w2 = random.choice(list(d))
            #checks if two word sequence is valid
            valid = check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
            #if initial valid check is false, generates random second words
            #until it reaches a valid two word sequence
            while valid != 0:
                if(valid == 1):
                    w2 = random.choice(list(d))
                elif(valid == 2):
                    w1 = random.choice(list(d))
                #print("w1: " + w1 + ", w2: " + w2)
                valid = check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
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
            #makes second word the new first word, goes to top and repeats
            w1 = w2
    return (line + " | " + line_pos + " | " + line_syl)

def get_line_sonnet(length, word, rhyme):
    #initial syllable count set high so while loop runs once
    syl_count = 100
    #initializes line string, which will eventually be the output
    line = ""
    line_syl = ""
    rannum = random.randint(0, length)
    containword = 0
    #generates lines until it finds a line exactly equal to length
    while ((word != None and (syl_count > length or containword == 0))
           or (word == None and (syl_count > length))):
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
            valid = check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
            #if initial valid check is false, generates random second words
            #until it reaches a valid two word sequence
            while valid != 0:
                if(valid == 1):
                    w2 = random.choice(list(d))
                elif(valid == 2):
                    w1 = random.choice(list(d))
                #print("w1: " + w1 + ", w2: " + w2)
                valid = check_valid(w1,w2, (syl_count + d[w2]['syl']) >= length)
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
            #makes second word the new first word, goes to top and repeats
            w1 = w2
    return (line + " | " + line_pos + " | " + line_syl)

def get_haiku(word):
    rannum = random.randint(0, 2)
    output = []
    if(rannum == 0):
        output.append(get_line_haiku(5, word))
        output.append(get_line_haiku(7, None))
        output.append(get_line_haiku(5, None))


    elif(rannum == 1):
        output.append(get_line_haiku(5, None))
        output.append(get_line_haiku(7, word))
        output.append(get_line_haiku(5, None))

    elif(rannum == 2):
        output.append(get_line_haiku(5, None))
        output.append(get_line_haiku(7, None))
        output.append(get_line_haiku(5, word))

    print(output)
    return output

def get_dict():
    return d
'''
def get_sonnet():
    output = get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) ++ "\n\n"
    output2 = get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) ++ "\n\n"
    output3 = get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) + "\n" + get_line_sonnet(10) ++ "\n\n"
    output4 = get_line_sonnet(10) + "\n" + get_line_sonnet(10)

'''
#opens data file
data = open("data.txt", "r")
#for each line of data in the file
for line in data:
  #split that line by spaces
  attr = line.split()
  #adds word to dictionary, under that word there is 'pos',  'freq', and 'syl'
  d[attr[1]] = {'pos' : attr[2], 'freq' : attr[3], 'syl' : sylco(attr[1])} #get_syllables(attr[1])}

# word = random.choice(list(d))
# print(word) # prints word
# print(d[word]['pos']) # prints part of speech of word
# print(d[word]['freq']) # prints frequency of word
# print(d[word]['syl']) # prints syllables in word
# print(get_line(5))
# print(get_line(7))
# print(get_line(5))
get_haiku("across")
#get_sonnet()
