'''
Name: Peter Wright
Project: ARGUS Chatbot for Rampo College Honors Symposium
Date: March 22, 2018
'''
from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk
from ARGUS import SynLink
from Graphing import EmotionGraph

class Response(object):
    mySentence=""	#response sentence
    myWords=[]		#array of words in mySentence
    myTags=[]		#pos tags of words in mySentence
    myGraph=0       #EmotionGraph used to plot emotions of sentence
    mySynLink=0 	#object used to find closest emotions

    '''
    Function Name: constructor 
    Purpose: create the Response object to hold information about the user response 
    Parameters: 
        inputSentence, 
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) save information about the response, ie sentence, words, POS tags
        2) create the EmotionGraph object
        3) create the SynLink object
        4) call emotionReader function to start getting emotional information
        5) display results
    Assistance Received: 
        none
    '''
    def __init__(self, inputSentence):
        #save sentence information
        self.mySentence=inputSentence
        self.myWords=inputSentence.split()
        self.myTags=pos_tag(word_tokenize(inputSentence), tagset='universal')

        #create emotion graph
        self.myGraph=EmotionGraph.EmotionGraph()

        #create SynLink
        self.mySynLink=SynLink.SynLink()

        #start reading the emotions of the sentence
        self.emotionReader()

        #display the finished graph to the user
        self.display()
    
    '''
    Function Name: destructor 
    Purpose: delete the Response object
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) set mySentence to an empty string
        2) delete all the values in myWords
        3) delete all the values in myTags
        4) delete the EmotionGraph object
    Assistance Received: 
        none 
    '''
    def __del__(self):
        self.mySentence=""

        del self.myWords[:]
        del self.myTags[:]

        del self.myGraph

    '''
    Function Name: emotionReader 
    Purpose: get the emotions of the words in the user response and save it to the EmotionGraph
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        negative, holds true if the previous word was a negative qualifier like 'not'
        emotion, holds string of closest emotion
    Algorithm: 
        1) iterate over 2D list of tagged words
        2) check if part of speach tag is one of the checkable types (adjective, adverb, noun, or verb)
        3) if part of speach is adverb then check if the word is a negative qualifier
        4) for all parts of speach check if negative is true
        5) if so get the closest emotion and save it
        6) if not get the closest emotion and save it
        7) if returned emotion is not empty save to EmotionGraph
    Assistance Received: 
        none 
    '''
    def emotionReader(self):
    	negative=False	#True if the previous word was a negative qualifier like 'not'
    	emotion=""		#string to hold closest emotion
    	for words in self.myTags:
            if words[1]=='ADJ':
                #negative word used previously
                if negative:
                    #find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
                        #add opposite emotion to graph
                        self.myGraph.addOppositeEmotion(emotion)
                    #reset negative
                    negative=False
                else:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
                        #add emotion to graph
                        self.myGraph.addEmotion(emotion)
            elif words[1]=='ADV':
                #check if 'not'
                if self.mySynLink.isNegative(words[0]):
                    negative=True
                #negative word used previously
                elif negative:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
    				    #add opposite emotion to graph
                        self.myGraph.addOppositeEmotion(emotion)
    				#reset negative
                    negative=False
                else:
                    #find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
                        #add emotion to graph
                        self.myGraph.addEmotion(emotion)
            elif words[1]=='NOUN':
                #negative word used previously
                if negative:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
    				    #add opposite emotion to graph
                        self.myGraph.addOppositeEmotion(emotion)
    				#reset negative
                    negative=False
                else:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
    				    #add emotion to graph
                        self.myGraph.addEmotion(emotion)
            elif words[1]=='VERB':
                #negative word used previously
                if negative:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
    				    #add opposite emotion to graph
                        self.myGraph.addOppositeEmotion(emotion)
    				#reset negative
                    negative=False
                else:
    				#find closest emotion to word
                    emotion=self.mySynLink.closestEmotion(words[0])
                    #no emotion found
                    if emotion!="none":
    				    #add emotion to graph
                        self.myGraph.addEmotion(emotion)

    '''
    Function Name: display 
    Purpose: display the data found in using the EmotionGraph
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) call the plot function of the EmotionGraph
    Assistance Received: 
        none 
    '''
    def display(self):
        self.myGraph.plot(False)

    #getters
    def getSentence(self):
        return self.mySentence
    
    def getTokens(self):
        return self.myWords

    def getPosTag(self, place):
        return self.myTags[place][1]

    def getGraph(self):
        return self.myGraph

    def getSynLink(self):
        return self.mySynLink

    #setters
    def setSentence(self, sentence):
        self.mySentence=sentence

        self.myWords=sentence.split()
        self.myTags=pos_tag(word_tokenize(sentence), tagset='universal')

    def setGraph(self, graph):
        self.myGraph=graph

    def setSynLink(self, syn):
        self.mySynLink=syn 