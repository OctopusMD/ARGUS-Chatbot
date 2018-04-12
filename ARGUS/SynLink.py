'''
Name: Peter Wright
Project: ARGUS Chatbot for Rampo College Honors Symposium
Date: March 22, 2018
'''

from nltk.corpus import wordnet as wn

class SynLink(object):
    myEmotions=[]   #hold the keys to the myLemmas dictionary for iteration
    myLemmas={}     #holds the synset lemmas for path similarity calculation
    myNegatives=[]  #holds list of words that are negative qualifiers

    '''
    Function Name: constructor 
    Purpose: create the SynLink object to find the emotions in a sentence 
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) construct dictionary holding lemmas for each emotion being checked 
        2) save the keys to the dictionary for later use
        3) save negative qualifiers to list 
    Assistance Received: 
        thesaurus.com, dictionary.com, & merriam-webster.com 
    '''
    def __init__(self):
        #help of thesaurus.com, dictionary.com, & merriam-webster.com
        #lemmas used to find path similarity for each emotion used in EmotionPoint and EmotionGraph class
        self.myLemmas["terror"]=['panic.n.01', 'terrify.v.01', 'panicky.s.01', 'afraid.a.01', 'shockingly.r.01']
        self.myLemmas["fear"]=['fear.n.01', 'fear.v.01', 'fearful.s.01', 'cowardly.a.01', 'fearfully.r.01']
        self.myLemmas["apprehension"]=['apprehension.n.01', 'apprehend.v.03', 'apprehensive.s.01', 'uneasy.a.01', 'anxiously.r.01']
        self.myLemmas["submission"]=['submission.n.01', 'submit.v.01', 'slavish.s.02', 'submissive.a.01', 'deferentially.r.01']
        self.myLemmas["admiration"]=['admiration.n.01', 'admire.v.01', 'admirable.s.01', 'valuable.a.01', 'admirably.r.01']
        self.myLemmas["trust"]=['trust.n.01', 'trust.v.01', 'trustworthy.s.02', 'credible.a.01', 'believably.r.01']
        self.myLemmas["acceptance"]=['acceptance.n.03', 'accept.v.01', 'acceptable.s.02', 'acceptable.a.01', 'acceptably.r.01']
        self.myLemmas["love"]=['love.n.02', 'love.v.01', 'affectionate.s.01', 'loving.a.01', 'fondly.r.01']
        self.myLemmas["ecstasy"]=['ecstasy.n.01', 'elate.v.01', 'ecstatic.s.01', 'elated.a.01', 'fierily.r.01']
        self.myLemmas["joy"]=['joy.n.01', 'rejoice.v.01', 'joyful.a.01', 'elated.s.02', 'gleefully.r.01']
        self.myLemmas["serenity"]=['repose.n.03', 'calm.v.01', 'calm.s.01', 'calm.a.02', 'calmly.r.01']
        self.myLemmas["optimism"]=['optimism.n.01', 'enthuse.v.01', 'affirmative.s.02', 'optimistic.a.01', 'optimistically.r.01']
        self.myLemmas["vigilance"]=['watchfulness.n.01', 'detect.v.01', 'argus-eyed.s.02', 'alert.a.01', 'vigilantly.r.01']
        self.myLemmas["anticipation"]=['anticipation.n.01', 'expect.v.01', 'anticipant.s.01', 'hopeful.a.01', 'expectantly.r.01']
        self.myLemmas["interest"]=['interest.n.01', 'interest.v.01', 'absorbing.s.01', 'interesting.a.01', 'interestingly.r.01']
        self.myLemmas["aggressiveness"]=['aggressiveness.n.01', 'worsen.v.02', 'aggressive.s.02', 'aggressive.a.01', 'aggressively.r.01']
        self.myLemmas["rage"]=['fury.n.01', 'rage.v.02', 'ferocious.s.01', 'violent.a.01', 'ferociously.r.01']
        self.myLemmas["anger"]=['anger.n.01', 'anger.v.01', 'angry.s.02', 'angry.a.01', 'angrily.r.01']
        self.myLemmas["annoyance"]=['irritation.n.01', 'annoy.v.01', 'annoyed.s.01', 'displeasing.a.01', 'annoyingly.r.01']
        self.myLemmas["contempt"]=['contempt.n.01', 'disrespect.v.01', 'aweless.s.02', 'contemptible.a.01', 'contemptibly.r.01']
        self.myLemmas["loathing"]=['abhorrence.n.01', 'hate.v.01', 'loath.s.01', 'unwilling.a.01', 'hatefully.r.01']
        self.myLemmas["disgust"]=['disgust.n.01', 'disgust.v.01', 'disgusting.s.01', 'nasty.a.01', 'disgustingly.r.01']
        self.myLemmas["boredom"]=['boredom.n.01', 'bore.v.01', 'boring.s.01', 'uninteresting.a.01', 'boringly.r.01']
        self.myLemmas["remorse"]=['compunction.n.01', 'anguish.v.01', 'contrite.s.01', 'apologetic.a.01', 'ruefully.r.01']
        self.myLemmas["grief"]=['grief.n.01', 'grieve.v.01', 'bereaved.s.01', 'elegiac.a.01', 'dolefully.r.01']
        self.myLemmas["sadness"]=['sadness.n.01', 'sadden.v.01', 'sad.s.02', 'sad.a.01', 'sadly.r.01']
        self.myLemmas["pensiveness"]=['pensiveness.n.01', 'contemplate.v.01', 'brooding.s.01', 'thoughtful.a.02', 'pensively.r.01']
        self.myLemmas["disapproval"]=['disapproval.n.01', 'disapprove.v.01', 'disapproving.s.01', 'unwilling.a.01', 'disapprovingly.r.01']
        self.myLemmas["amazement"]=['astonishment.n.01', 'amaze.v.01', 'amazing.s.01', 'incredible.a.01', 'amazingly.r.01']
        self.myLemmas["surprise"]=['surprise.n.01', 'surprise.v.01', 'unpredictable.s.02', 'surprising.a.01', 'surprisingly.r.01']
        self.myLemmas["distraction"]=['distraction.n.01', 'distract.v.01', 'distracted.s.01', 'agitated.a.01', 'distractedly.r.01']
        self.myLemmas["awe"]=['awe.n.01', 'awe.v.01', 'dazzled.s.01', 'awed.a.02', 'dazzlingly.r.01']

        #initialize myEmotions to hold the keys in myLemmas
        self.myEmotions=self.myLemmas.keys()

        #initialize myNegatives to hold common negative qualifiers
        self.myNegatives=["not", "neither", "nor", "no", "non"] 
        
    '''
    Function Name: isNegative 
    Purpose: check to see if current word is a negative qualifier
    Parameters: 
        word, string that holds the word being checked
    Return Value: 
        true if word is a negative qualifier
        false otherwise 
    Local Variables: 
        none 
    Algorithm: 
        1) iterate through list of negative qualifiers 
        2) check if parameter word matches element in list
        3) return true if so
        4) if loop doesn't return true return false
    Assistance Received: 
        none 
    '''
    def isNegative(self, word):
        #check against known words in myNegative
        for words in self.myNegatives:
            if word==words:
                return True

        #word is not a negative qualifier
        return False

    '''
    Function Name: closestEmotion 
    Purpose: find the closest emotion to the current word
    Parameters: 
        word, string that holds the word being checked
    Return Value: 
        emotion keyword with the highest path similarity
        if no matches return string "none"
    Local Variables: 
        bestMatcheNum, holds the best path similarity value
        bestMatchStr, holds the emotion of the best path similarity
        tempSet, holds the synset of the current word
        posSet, holds the part of speach of the current word
        similar, holds the path similarity to each emotion keyword lemma 
    Algorithm: 
        1) get the synset of the word
        2) get the part of speach of the word
        3) check which part of speach th word is
        4) iteratre over the emotion keywords
        5) use emotion keyword and part of speach to lookup correct lemma to compare to word
        6) get path similarity between word and emotion keyword
        7) if similar is not empty and has the higher value than anything so far save to bestMatchNum and bestMatchStr
        8) if bestMatchStr is still empty return "none"
        9) else return bestMatchStr
    Assistance Received: 
        none 
    '''
    def closestEmotion(self, word):
        bestMatchNum=0      #holds the best path similarity value
        bestMatchStr=""     #holds the emotion of the best path similarity

        #get the synset of word
        if len(wn.synsets(word))>0:
            tempSet=wn.synsets(word)[0]
        else:
            return "none"
        #get the part of speach of the new synset
        posSet=tempSet.pos()

        #synset is a noun
        if posSet=='n':
            #interate through key emotions
            for key in self.myEmotions:
                #get path similarity
                similar=wn.path_similarity(wn.synset(self.myLemmas[key][0]), tempSet)

                #check to make sure a number was returned
                if similar is not None:
                    #check to see if new best match
                    if similar>bestMatchNum:
                        bestMatchNum=similar
                        bestMatchStr=key
        #synset is a verb                
        elif posSet=='v':
            #interate through key emotions
            for key in self.myEmotions:
                #get path similarity
                similar=wn.path_similarity(wn.synset(self.myLemmas[key][1]), tempSet)

                #check to make sure a number was returned
                if similar is not None:
                    if similar>bestMatchNum:
                        bestMatchNum=similar
                        bestMatchStr=key
        #synset is an adjective of type s
        elif posSet=='s':
            #interate through key emotions
            for key in self.myEmotions:
                #get path similarity
                similar=wn.path_similarity(wn.synset(self.myLemmas[key][2]), tempSet)

                #check to make sure a number was returned
                if similar is not None:
                    #check to see if new best match
                    if similar>bestMatchNum:
                        bestMatchNum=similar
                        bestMatchStr=key
        #synset is an adjective of type a
        elif posSet=='a':
            #interate through key emotions
            for key in self.myEmotions:
                #get path similarity
                similar=wn.path_similarity(wn.synset(self.myLemmas[key][3]), tempSet)

                #check to make sure a number was returned
                if similar is not None:
                    #check to see if new best match
                    if similar>bestMatchNum:
                        bestMatchNum=similar
                        bestMatchStr=key
        #synset is an adjective of type r
        elif posSet=='r':
            #interate through key emotions
            for key in self.myEmotions:
                #get path similarity
                similar=wn.path_similarity(wn.synset(self.myLemmas[key][1]), tempSet)

                #check to make sure a number was returned
                if similar is not None:
                    #check to see if new best match
                    if similar>bestMatchNum:
                        bestMatchNum=similar
                        bestMatchStr=key

        #no best match found
        if bestMatchStr=="":
            return "none"
        #best match found
        else:
            return bestMatchStr

    #setters
    def setLemmas(self, lemmas):
        self.myLemmas=lemmas

    def setEmotions(self, emotions):
        self.myEmotions=emotions

    def setNegatives(self, negatives):
        self.myNegatives=negatives

    #getters
    def getLemmas(self):
        return self.myLemmas

    def getEmotions(self):
        return self.myEmotions

    def getNegatives(self):
        return self.myNegatives