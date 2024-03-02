# MARVIN UWALAKA 
# import random module
import random
content = open('word5Dict.txt','r')         #  open currupted file  to be read
uncorrupted_file = open('scrabble5txt','w') #  open uncorrupted file to be written in 
infile = content.read()                     #  read file 
infile = infile.split('#')                  #  sepreate words by '#'
def check_edgeCases(infile):
    """  checks edge cases of words in infile 
         input infile of type list 
         returns words of type list """
    words=[]
    for word in infile:  
        if word.isalpha():
            words.append(word)    
        if len(word) > 5:
            word = word.split('\n')
            words.append(word[0])
            words.append(word[1])
    return words 
words =  check_edgeCases(infile)
for word in words:
    uncorrupted_file.write(word+'\n')
        
#  close openfiles 
content.close()             
uncorrupted_file.close()

class ScrabbleDict:
    def __init__(self, size,filename):
        self.dict_ = {}
        self.size = size 
        self.filename = filename 
        self.tries = 0
        
        #  initializes dictionary with words as key and value with uncorrupted_file
        content = open(str(filename),'r')
        infile =  content.read()
        words = infile.splitlines()
        for word in words:
            if len(word) == size:
                self.dict_[word] = word 
    
    def check(self, word):
        # checks if a word is in dictionary 
        return word in self.dict_
    
    def getSize(self): 
        # returns size of ditionary 
        return len(self.dict_)  
   
    def getWords(self,letter):
        #  returns word that start with 'letter' in alphabetical order 
        list_of_words = []
        for value in self.dict_.values():
            list_of_words.append(value)
        return list_of_words
    
    def getWordSize(self):
        return self.size
        
    def tries(self,guess):
        if guessed:
            self.tries += 1 
        
    def wordmeetsrequirements(self,word):
        # checks if word in a self.dictionary and id the right size 
        # returns bool value 
        return  word in self.dict_ and len(word) == self.size 
    
    def getMaskedWords(self, template):
        # input template of type str 
        # returns word of type str that fit template 
        maskedWords = []
        for key in self.dict_.keys():
            i = 0
            matching = True
            while matching and i < self.size:
                if template[i] == key[i] or template[i] == '*' :
                    matching = True 
                else:
                    matching = False
                i += 1
            if matching:
                maskedWords.append(key)
        return maskedWords
                    
    def getConstrainedWords(self,template,letters):
        # input template of type str and letters of type str
        # returns list of words of type str that fit template and wildcard spots contain letters 
        maskedWords = self.getMaskedWords(template)
        ConstrainedWords = []
        i = -1 
        for letter in template:
            i += 1
            if letter == '*':
                for word in maskedWords:
                    if word[i] in list(letters):
                        ConstrainedWords.append(word)
        return ConstrainedWords
                    
    def dictionary_analysis(self):
        alphabet= list('abcdefghijklmnopqrstuvwxyz')
        alpha_dict = {}
        letters_count = []
        letters_percentages = []
        totalapp = 0 
        # creates a dictionry with all letters as key 
        for letter in alphabet:
            alpha_dict[letter] = []
        # total apperances of all letters 
        for letter in alphabet:
            for key in self.dict_.keys():
                totalapp += key.count(letter) 
        # gets information for each letter 
        for letter in alphabet:
            count = 0 
            histogram  = ''
            for key in self.dict_.keys():
                count += key.count(letter)
            percentage = count/totalapp *100 
            histogram  =  '*' * round(percentage)
            alpha_dict.get(letter).append(letter.upper() +':')
            alpha_dict.get(letter).append(count)
            letters_count.append(count)
            letters_percentages.append(round(percentage,2))
            alpha_dict.get(letter).append(round(percentage,2))
            alpha_dict.get(letter).append(histogram)
        max_count = len(str(max(letters_count)))
        max_per = len(str(max(letters_percentages)))-1  
        # prints  formatted analysis 
        for value in alpha_dict.values():
            print(str(value[0])+' '+str(value[1])+'  ' + ' '*(max_count-len(str(value[1])))+ str(value[2])+'%' +'  ' + ' '*(max_per-(len(str(value[2]))-1)) +value[3])
    
                             
def check_attempt(wordle_of_day,attempt,tries,trials,word_found): 
    # checks if attempt of type str is the word of the day and prints feedback and analysis of previous attempts 
    # inputs wordle of the day(str), tries(int), trials(list),word_found(bool)
    
    trial_result = ""    # initiallize trial_result instance
    attempList = list(attempt) 
    wordList = list(wordle_of_day)
    colours = {'green':[],'orange':[],'red':[]}
    checked_green_letters = []  # letters that have been checked as part of green category to be used as reference 
    checked_orange_letters= []  # letters that have been checked as part of orange category to be used as reference 
    checked_red_letters = []    # letters that have been checked as part of red category to be used as reference 
    for letters in range(len(wordList)):
        b = attempList.pop(0)     
        c = wordList.pop(0)
        attempList.append(b)
        if b == c:
            b = b.upper()
            if b in checked_green_letters or b in checked_orange_letters or b in checked_red_letters:    # if letter is already in any of the categories 
                colours.get('green').append(b+str(checked_orange_letters.count(b)+checked_green_letters.count(b)+ checked_red_letters.count(b)+1)) # add the num instances to that letter
            elif attempt.count(b.lower()) > 1:
                colours.get('green').append(b+"1")
            else:
                colours.get('green').append(b)
            checked_green_letters.append(b)   
        elif b not in wordle_of_day or (attempList.count(b) > wordle_of_day.count(b)) : 
            attempList.pop(-1)
            b = b.upper()
            if b in checked_orange_letters or b in checked_green_letters or b in checked_red_letters :
                colours.get('red').append(b +str(checked_orange_letters.count(b)+checked_green_letters.count(b)+ checked_red_letters.count(b)+1)) 
            elif attempt.count(b.lower()) > 1:
                colours.get('red').append(b+"1")
            else:
                colours.get('red').append(b)   
            checked_red_letters.append(b)        
        elif b.lower() in wordle_of_day :
            b = b.upper()
            if b in checked_orange_letters or b in checked_green_letters or b in checked_red_letters:
                colours.get('orange').append(b +str(checked_orange_letters.count(b)+checked_green_letters.count(b)+ checked_red_letters.count(b)+1)) 
            elif attempt.count(b.lower()) > 1:
                colours.get('orange').append(b+"1")
            else:
                colours.get('orange').append(b)
                attempList.append(b)
            checked_orange_letters.append(b) 
            
    # sort results alphabetically 
    colours.get('green').sort()
    colours.get('orange').sort()
    colours.get('red').sort()
    
    # get result of the trial 
    trial_result = attempt.upper() + " Green = {"+ ", ".join(colours.get('green'))+"} - Orange = {" +  ", ".join(colours.get('orange'))+"} – Red = {"+  ", ".join(colours.get('red'))+"}"
    
    # add trials to trials based of these conditions 
    if tries > 1:
        trials.append('\n'+ trial_result)
    else:
        trials.append(trial_result)
        
    # check if word has been word 
    if len(colours.get('green')) == len(attempt):
        word_found = True 
        
    return trials,word_found

# def main function
# runs wordle game and test scrable class 
def main():
   
   
    #   get word of the day using random module 
    wordle_of_day =  (list(wordle.dict_.items()).pop(random.randint(0,wordle.getSize())))
    wordle_of_day =  wordle_of_day[1]
    tries = 1   # tries user has 
    trials = [] # results of trials 
    word_found = False 
    attempt = '' 
    attempts = []   # words player has been attepmted by user 
    while tries < 7 and not word_found: 
        attempt = input('Attempt ' + str(tries) +': Please enter a 5 five-letter word: ').lower()
        #  checkes conditions to see if attempt meets requirements and prints corresponding output
        if attempt in attempts and wordle.wordmeetsrequirements(attempt):
            print(attempt.upper() + ' was already entered')
        elif wordle.wordmeetsrequirements(attempt) :
            attempts.append(attempt) 
            trials,word_found = check_attempt(wordle_of_day,attempt,tries,trials,word_found) 
            print("".join(trials))
            tries += 1
        if len(attempt) > wordle.size:
            print(attempt.upper() + ' is too long') 
        if len(attempt) < wordle.size:
            print(attempt.upper() + ' is too short')
        if attempt not in wordle.dict_ and len(attempt) == wordle.size:
            print(attempt.upper() + ' is not a recognized word')
        
    # checks if user won or not 
    if word_found:
        print('Found in '+ str(tries - 1)+ ' attempts. Well done. The Word is '+ wordle_of_day.upper())
        
    else:
        print('Sorry you lose. The Word is ' + wordle_of_day.upper())

if __name__ == "__main__":
    wordle = ScrabbleDict(5,'scrabble5txt')  #  test __init__(self, size, filename)
    wordle.dictionary_analysis()             #  test task 5 
    print(wordle.check('lalls'))             #  test check(self, word)
    print(wordle.getSize())                  #  test getSize()
    a_words = wordle.getWords('a')           #  test getWords(self,letter)
    print(a_words)
    print(wordle.getWordSize())              #  test getWordSize()
    main()
