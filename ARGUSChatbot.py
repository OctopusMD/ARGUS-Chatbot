'''
Name: Peter Wright
Project: ARGUS Chatbot for Rampo College Honors Symposium
Date: March 22, 2018
'''
from chatterbot import ChatBot
from ARGUS.Response import Response
from Graphing.EmotionGraph import EmotionGraph

#construct the chatbot
ARGUS=ChatBot('ARGUS', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
ARGUS.train("chatterbot.corpus.english")

#introduction
print("----------------------Welcome to the ARGUS Chatbot!----------------------")
print("This chatbot will display a graph explaining the emotions it found in ")
print("your previous statement. The red points are the emotions found based on ")
print("your response and the blue point is the average emotion of the response.")
print("Before continuing the conversation with the chatbot you must first ")
print("close the graph. Say goodbye the chatbot to end the conversation.")
print("-------------------------------------------------------------------------")

userInput="Hello"			#holds the user input, start with a greeting to the chatbot so it greets the user
allAverages=[]				#holds the average points of each response

#continue until the user says goodbye
while(True):
	#talk to chatbot
    print("ARGUS: "+str(ARGUS.get_response(userInput)))
    #get user response
    print("Me: ", end='')
    userInput=input()

    #check if the user wants to leave
    if userInput.lower()=="goodbye":
    	break

    #graph the results
    userResponse=Response(userInput)

    #save average emotion for overall graph
    allAverages.append(userResponse.getGraph().getAverage())

    #clear Response object for next input
    del userResponse

#outroduction
print("--------------------Thank you for using ARGUS Chatbot!-------------------")
print("Here are the average emotions for each response:")
#output each average emotion
counter=1
for points in allAverages:
	print("Response "+str(counter)+": "+points.getEmotion())
	counter+=1
print("-------------------------------------------------------------------------")

totalGraph=EmotionGraph()	#graph that holds the progress of the user
#add averages to totalGraph
totalGraph.setPoints(allAverages)
#plot the overall results connecting the points
totalGraph.plot(True)