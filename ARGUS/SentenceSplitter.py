'''
Created on Jun 15, 2017

@author: Peter
'''
from nltk.tokenize import word_tokenize
from nltk import Nonterminal, nonterminals, Production, CFG
from nltk import pos_tag, grammar
from nltk import tree
from nltk.parse import RecursiveDescentParser
from _overlapped import NULL
from nltk import grammar
import nltk
from Tests import makeGrammar

class Repsonse(object):
    mySentence="";
    myWords=[]
    myTags=[]
    myTree=NULL

    def __init__(self, inputSentence):
        #nltk.corpus.myCorpus.tagged_words(tagset='universal')
        
        self.mySentence=inputSentence
        self.myWords=inputSentence.split()
        self.myTags=pos_tag(word_tokenize(inputSentence), tagset='universal')
        
        
        self.createTree2()
        
    def createTree1(self, tags):
        isVerb=False
        tempList=list("")
        curTree=NULL
        prevTree=NULL
        
        for words in reversed(tags):
            #start creating a VP branch
            if(words[1]=='VERB' or words[1]=='ADV'):
                #continuing on current branch
                if(isVerb):
                    tempList.append(words[0])
                #finish the previous branch so that we can start the VP branch
                else:
                    if(prevTree==NULL and curTree==NULL):
                        curTree=tree.Tree('NP', tempList)
                    else:
                        prevTree=curTree
                        curTree=tree.Tree('NP', [tempList, prevTree] )
                    isVerb=True
                    tempList.clear()
                    tempList.append(words[0])
            #start creating a NP branch
            elif(words[1]=='NOUN' or words[1]=='ADJ'):
                #continuing on current branch
                if(not isVerb):
                    tempList.append(words[0])
                #finish the previous branch so that we can start the NP branch
                else:
                    if(prevTree==NULL and curTree==NULL):
                        curTree=tree.Tree('VP', tempList)
                    else:
                        prevTree=curTree
                        curTree=tree.Tree('VP', [tempList, prevTree] )
                    isVerb=False
                    tempList.clear()
                    tempList.append(words[0])
            else:
                tempList.append(words[0])
        if(isVerb):
            prevTree=curTree
            curTree=tree.Tree('VP', tempList)
        else:
            prevTree=curTree
            curTree=tree.Tree('NP', tempList)
        self.myTree=tree.Tree('S', [curTree, prevTree])
    
    def makeGrammar(self):
        gram="""
  S  -> NP VP Conj
  NP -> Det Nom | PropN 
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP | V Adv
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  Adv -> 'quickly'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
  Conj -> 'but'
  """
        
        #arrays to hold each type of word
        adj=[]
        adp=[]
        adv=[]
        conj=[]
        det=[]
        noun=[]
        num=[]
        prt=[]
        pron=[]
        verb=[]
        x=[]
        
        #find the pos_tag of each word and add it to the approate array
        for words in self.myTags:
            if(words[1]=='ADJ'):
                adj.append(words[0])
            elif(words[1]=='ADP'):
                adp.append(words[0])
            elif(words[1]=='ADV'):
                adv.append(words[0])
            elif(words[1]=='CONJ'):
                conj.append(words[0])
            elif(words[1]=='DET'):
                det.append(words[0])
            elif(words[1]=='NOUN'):
                noun.append(words[0])
            elif(words[1]=='NUM'):
                num.append(words[0])
            elif(words[1]=='PRT'):
                prt.append(words[0])
            elif(words[1]=='PRON'):
                pron.append(words[0])
            elif(words[1]=='VERB'):
                verb.append(words[0])
            elif(words[1]=='X'):
                x.append(words[0])
            else:
                #split the sentences up
                return 0;
        
        if(len(conj)!=0):
            for words in conj:
                gram=gram[:397]+'\''+words+'\' | '+gram[397:]
        if(len(prt)!=0):
            for words in prt:
                gram=gram[:383]+'\''+words+'\' | '+gram[383:]
        if(len(adp)!=0):
            for words in adp:
                gram=gram[:382]+'\''+words+'\' | '+gram[382:]
        if(len(verb)!=0):
            for words in verb:
                gram=gram[:321]+'\''+words+'\' | '+gram[321:]
        if(len(adv)!=0):
            for words in adv:
                gram=gram[:303]+'\''+words+'\' | '+gram[303:]
        if(len(adj)!=0):
            for words in adj:
                gram=gram[:250]+'\''+words+'\' | '+gram[250:]
        if(len(noun)!=0):
            for words in noun:
                gram=gram[:194]+'\''+words+'\' | '+gram[194:]     
        if(len(det)!=0):
            for words in det:
                gram=gram[:175]+'\''+words+'\' | '+gram[175:]     
        if(len(pron)!=0):
            for words in pron:
                gram=gram[:131]+'\''+words+'\' | '+gram[131:]
        
        return nltk.CFG.fromstring(gram)
        
    def createTree2(self):
        grammar1 = self.makeGrammar()
        rd = RecursiveDescentParser(grammar1)
        for tree in rd.parse(self.myWords):
            print(tree)
        
    def outputTree(self):
        self.myTree.draw()
        
    def getTree(self):
        return self.myTree
    
    def getSentence(self):
        return self.mySentence
    
    def getTokens(self):
        return self.myWords
            