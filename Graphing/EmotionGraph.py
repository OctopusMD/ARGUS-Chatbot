'''
Name: Peter Wright
Project: ARGUS Chatbot for Rampo College Honors Symposium
Date: March 22, 2018
'''
from Graphing import EmotionPoint
import math
import matplotlib.pyplot as plt


class EmotionGraph(object):
    myPoints=[]         #holds Emotion points added to the graph
    myAverage=0         #holds the average of all the emotion points 
    myEmotions={}       #holds the standard emotion values
    myImg=plt.imread("715px-Plutchik-wheel.svg.png")   
    
    '''
    Function Name: constructor 
    Purpose: create an EmotionGraph object
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) intialize the average EmotionPoint to be at the origin
        2) create dictionary of key emotions and their polar coordinates
    Assistance Received: 
        none 
    '''
    def __init__(self):
        self.myAverage=EmotionPoint.EmotionPoint(0.0, 0.0)
        
        #standard emotions are held in a dictionary so they can be easily set
        self.myEmotions["terror"]=[0.5, 0]
        self.myEmotions["fear"]=[1.25, 0]
        self.myEmotions["apprehension"]=[1.75, 0]
        self.myEmotions["submission"]=[2, math.pi/8]
        self.myEmotions["admiration"]=[0.5, math.pi/4]
        self.myEmotions["trust"]=[1.25, math.pi/4]
        self.myEmotions["acceptance"]=[1.75, math.pi/4]
        self.myEmotions["love"]=[2, 3*math.pi/8]
        self.myEmotions["ecstasy"]=[0.5, math.pi/2]
        self.myEmotions["joy"]=[1.25, math.pi/2]
        self.myEmotions["serenity"]=[1.75, math.pi/2]
        self.myEmotions["optimism"]=[2, 5*math.pi/8]
        self.myEmotions["vigilance"]=[0.5, 3*math.pi/4]
        self.myEmotions["anticipation"]=[1.25, 3*math.pi/4]
        self.myEmotions["interest"]=[1.75, 3*math.pi/4]
        self.myEmotions["aggressiveness"]=[2, 7*math.pi/8]
        self.myEmotions["rage"]=[0.5, math.pi]
        self.myEmotions["anger"]=[1.25, math.pi]
        self.myEmotions["annoyance"]=[1.75, math.pi]
        self.myEmotions["contempt"]=[2, 9*math.pi/8]
        self.myEmotions["loathing"]=[0.5, 5*math.pi/4]
        self.myEmotions["disgust"]=[1.25, 5*math.pi/4]
        self.myEmotions["boredom"]=[1.75, 5*math.pi/4]
        self.myEmotions["remorse"]=[2, 11*math.pi/8]
        self.myEmotions["grief"]=[0.5, 3*math.pi/2]
        self.myEmotions["sadness"]=[1.25, 3*math.pi/2]
        self.myEmotions["pensiveness"]=[1.75, 3*math.pi/2]
        self.myEmotions["disapproval"]=[2, 13*math.pi/8]
        self.myEmotions["amazement"]=[0.5, 7*math.pi/4]
        self.myEmotions["surprise"]=[1.25, 7*math.pi/4]
        self.myEmotions["distraction"]=[1.75, 7*math.pi/4]
        self.myEmotions["awe"]=[2, 15*math.pi/8]
    
    '''
    Function Name: deconstructor 
    Purpose: delete an EmotionGraph object
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) delete all the EmotionPoints saved
        2) set average to 0
    Assistance Received: 
        none 
    '''
    def __del__(self):
        del self.myPoints[:]

        myAverage=0

    '''
    Function Name: addEmotionPoint 
    Purpose: add an EmotionPoint object to the graph
    Parameters: 
        emopoint, holds the new emopoint to add to graph
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) add emopoint to list of EmotionPoints
        2) reconfigure the average point to match new data
    Assistance Received: 
        none 
    '''
    def addEmotionPoint(self, emopoint):
        self.myPoints.append(emopoint) 
        
        #reconfigure graphing data
        self.configure()
    
    '''
    Function Name: addEmotion 
    Purpose: add an EmotionPoint to the graph based on string parameter
    Parameters: 
        emotion, holds a string that matches a key in myEmotions
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) add EmotionPoint to list that matches dictionary entry's data 
        2) reconfigure the average point to match new data
    Assistance Received: 
        none 
    '''
    def addEmotion(self, emotion):
        self.myPoints.append(EmotionPoint.EmotionPoint(self.myEmotions[emotion][0], self.myEmotions[emotion][1]))

        #reconfigure graphing data
        self.configure()

    '''
    Function Name: addOppositeEmotion 
    Purpose: add an EmotionPoint to the graph based on the opposite of the string parameter
    Parameters: 
        emotion, holds a string that matches a key in myEmotions
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) save phi value that matches dictionary entry's data 
        2) a pi to it to get the reflection over origin
        3) add EmotionPoint with new data to list
        4) reconfigure the average point to match new data
    Assistance Received: 
        none 
    '''
    def addOppositeEmotion(self, emotion):
        #find the point opposite to emotion on graph
        oppPoint=self.myEmotions[emotion][1]+math.pi
        #make sure that phi for new point isn't over 2*pi
        oppPoint%=2*math.pi

        self.myPoints.append(EmotionPoint.EmotionPoint(self.myEmotions[emotion][0], oppPoint))

        #reconfigure graphing data
        self.configure()

    '''
    Function Name: configure 
    Purpose: recalculate the value of the average EmotionPoint
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        numx, holds sum of all the x values for all EmotionPoints
        numy, holds sum of all the y values for all EmotionPoints
    Algorithm: 
        1) iterate over list of EmotionPoints
        2) add y value to numy
        3) add x value to numx
        4) check to make sure that list of EmotionPoints isn't size 0
        5) set X value of myAverage to numx/size of list
        6) set y value of myAverage to numy/size of list
    Assistance Received: 
        none 
    '''
    def configure(self):        
        numx=0  #total of all X values for all points
        numy=0  #total of all y values for all points
        
        #calculate totals
        for spot in self.myPoints:
            numy+=spot.getY()
            numx+=spot.getX()

        #check to make sure there are points, if not next lines will cause error
        if len(self.myPoints)==0:
            return

        #set the X and Y for the average emotionpoint    
        self.myAverage.setX(numx/len(self.myPoints))
        self.myAverage.setY(numy/len(self.myPoints))
    
    '''
    Function Name: plot 
    Purpose: display the graph to the user
    Parameters: 
        lineFlag, if true connect the dots in order appeared, else plot the points and the average
    Return Value: 
        none 
    Local Variables: 
        xpoints, list holds x values for plotting
        ypoints, list holds y values for plotting
    Algorithm: 
        1) iterate over EmotionPoints saving the x and y values to lists 
        2) add image of Plutchik's Emotion Wheel to graph
        3) check if lineFlag is true
        4) if so plot x and y points in red and connect the dots
        5) else plot x and y points in red and the average in blue
    Assistance Received: 
        none 
    '''
    def plot(self, lineFlag):
        xpoints=[]  #holds x values for plotting
        ypoints=[]  #holds y values for plotting
        
        #adds all the emotion points onto the graph    
        for points in self.myPoints:
            xpoints.append(points.getX())
            ypoints.append(points.getY())
        
        plt.imshow(self.myImg, extent=[-2.96,2.96,-2.96,2.96])
        
        if lineFlag:
            plt.plot(xpoints, ypoints, '.r-')  
        else:
            #points will be red dots
            plt.plot(xpoints, ypoints, 'ro')    
            #points will be blue dots
            plt.plot(self.myAverage.getX(), self.myAverage.getY(), 'bo')    

        plt.show()

    #setters
    def setPoints(self, points):
        self.myPoints=points

        #reconfigure
        self.configure()

    def setEmotions(self, emotions):
        self.myEmotions=emotions

    def setImage(self, image):
        self.myImg=image

    #getters
    def getPoints(self):
        return self.myPoints

    def getAverage(self):
        return self.myAverage

    def getEmotions(self):
        return self.myEmotions

    def getImage(self):
        return self.myImg

