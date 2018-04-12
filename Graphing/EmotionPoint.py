'''
Name: Peter Wright
Project: ARGUS Chatbot for Rampo College Honors Symposium
Date: March 22, 2018
'''

#needed for trigonometry needed to convert x and y to r and phi, also gives value of pi
import math

class EmotionPoint(object):
    myX=0.0         #x value of the point
    myY=0.0         #y value of the point
    myR=0.0         #r value of the point
    myPhi=0.0       #phi value of the point
    myEmotions=[]   #list of possible emotions this point can represent
    
    '''
    Function Name: constructor 
    Purpose: create an EmotionPoint object
    Parameters: 
        r, holds r value of polar coordinate
        phi, holds the phi value of polar coordinate
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) set myR and myPhi to parameters
        2) calculate the x and y values based on the polar coordinate values
        3) create a list of the key emotions being checked
    Assistance Received: 
        none 
    '''
    def __init__(self, r, phi):
        self.myR=r
        self.myPhi=phi
        
        #calculate the x and y points because they aren't given
        self.recalculateXY()

        #list of possible emotions this point can represent
        self.myEmotions.append("awe")
        self.myEmotions.append("terror")
        self.myEmotions.append("fear")
        self.myEmotions.append("apprehension")
        self.myEmotions.append("submission")
        self.myEmotions.append("admiration")
        self.myEmotions.append("trust")
        self.myEmotions.append("acceptance")
        self.myEmotions.append("love")
        self.myEmotions.append("ecstasy")
        self.myEmotions.append("joy")
        self.myEmotions.append("serenity")
        self.myEmotions.append("optimism")
        self.myEmotions.append("vigilance")
        self.myEmotions.append("anticipation")
        self.myEmotions.append("interest")
        self.myEmotions.append("aggressiveness")
        self.myEmotions.append("rage")
        self.myEmotions.append("anger")
        self.myEmotions.append("annoyance")
        self.myEmotions.append("contempt")
        self.myEmotions.append("loathing")
        self.myEmotions.append("disgust")
        self.myEmotions.append("boredom")
        self.myEmotions.append("remorse")
        self.myEmotions.append("grief")
        self.myEmotions.append("sadness")
        self.myEmotions.append("pensiveness")
        self.myEmotions.append("disapproval")
        self.myEmotions.append("amazement")
        self.myEmotions.append("surprise")
        self.myEmotions.append("distraction")
    
    '''
    Function Name: recalculatePolar 
    Purpose: calculate the polar coordinate values based on the xy values
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) save value of r based on the hypotenuse of the triangle created by x and y 
        2) find out if x or y are on an axis
        3) if so set myPhi to appropiate pi/2 value to avoid divide by 0 error
        4) else find what quadrant the point is in
        5) apply the correct formula based on which quadrant and save it myPhi
        6) check for floating point errors to set either r or phi to 0
    Assistance Received: 
        none 
    '''
    def recalculatePolar(self):
        self.myR=math.sqrt(pow(self.myX, 2)+pow(self.myY, 2))

        if self.myX==0 or self.myY==0:
            if self.myX==0:
                if self.myY>0:
                    self.myPhi=math.pi/2
                else:
                    self.myPhi=3*math.pi/2
            else:
                if self.myX>0:
                    self.myPhi=0
                else:
                    self.myPhi=math.pi
        elif self.myX>0:
            if self.myY>0:
                self.myPhi=math.atan(self.myY/self.myX)
            else:
                self.myPhi=math.atan(self.myY/self.myX)+(2*math.pi)
        else:
            self.myPhi=math.atan(self.myY/self.myX)+math.pi            
        
        #getting floating point errors when x or y should be 0 so
        if math.fabs(self.myR)<1e-14 :
            self.myR=0

        if math.fabs(self.myPhi)<1e-14 :
            self.myPhi=0
            
    '''
    Function Name: recalculatePolar 
    Purpose: calculate the xy values based on the polar coordinate values
    Parameters: 
        none
    Return Value: 
        none 
    Local Variables: 
        none
    Algorithm: 
        1) set myX to be r * cos(phi)
        2) set myY to be r * sin(phi)
        6) check for floating point errors to set either x or y to 0
    Assistance Received: 
        none 
    '''
    def recalculateXY(self):
        self.myX=self.myR*math.cos(self.myPhi)
        self.myY=self.myR*math.sin(self.myPhi)
        
        #getting floating point errors when x or y should be 0 so
        if math.fabs(self.myX)<1e-14 :
            self.myX=0

        if math.fabs(self.myY)<1e-14 :
            self.myY=0
        
    #getters
    '''
    Function Name: getEmotion 
    Purpose: get the emotion of the current EmotionPoint object
    Parameters: 
        none
    Return Value: 
        string holding the emotion the point represents 
        "none" if error has occured
    Local Variables: 
        tempPhi, holds the phi value of the point so as to not change the actual phi value of the EmotionPoint
        tempR, holds the r value of the point so as to not change the actual r value of the EmotionPoint
        counter, holds the number of times completed a loop through the first for loop
        last, holds the rightbound section limit (phi value)
        phiList, holds the phi values being iterated over in the list and are treated as leftbound section limits
        tempX, holds the x value of the point so as to not change the actual x value of the EmotionPoint
        tempY, holds the y value of the point so as to not change the actual y value of the EmotionPoint
    Algorithm: 
        1) iterate over phiList values checking if point is between current phi and last
        2) if first iteration use special if statement to check because phi resets at 2pi
        3) if point is in this section rotate phi to be in section between 5pi/8 and 3pi/8 because that allows easiest math to examine where point is
        4) break the for loop
        5) get x and y from r and new phi values
        6) check to see if the point is in inner most circle using r value
        7) check if point is in pedal using two interesting circles
        8) if in pedal check to see if it is in the upper pedal or lower pedal
        9) if not in pedal find if it is to the righ or left of the pedal
        9) return the value held in emotionlist based on counter value and where it is in the section
    Assistance Received: 
        none 
    '''
    def getEmotion(self):
        tempPhi=self.myPhi                                                                                                  #holds the phi value used to find the Emotion
        tempR=self.myR                                                                                                      #holds the r value used to find Emotion
        counter=0                                                                                                           #shows what section of the graph the point is in
        last=15*math.pi/8                                                                                                   #holds the rightbound section limit
        phiList=[math.pi/8, 3*math.pi/8, 5*math.pi/8, 7*math.pi/8, 9*math.pi/8, 11*math.pi/8, 13*math.pi/8, 15*math.pi/8]   #holds the phi values being interated over in the for loop
        #go through for loop to find which section the point is in
        for phi in phiList:
            if phi!=math.pi/8:
                #point is in this section
                if last<tempPhi<=phi:
                    #rotate to make checking easier
                    if phi>=5*math.pi/8:
                        tempPhi=tempPhi-(phi-(5*math.pi/8))
                    else:
                        tempPhi=tempPhi+((5*math.pi/8)-phi)
                    break
            #first loop works differently because phi cannot be greater than 2pi
            else:
                #point is in this section
                if tempPhi>last or tempPhi<=phi:
                    #rotate to make checking easier
                    tempPhi=tempPhi+math.pi/2
                    break
            last=phi
            counter+=1

        tempX=tempR*math.cos(tempPhi)   #holds the X value used to find the Emotion
        tempY=tempR*math.sin(tempPhi)   #holds the Y value used to find the Emotion

        #check to see if the point is in inner circle
        if tempR<=1:
                #return closest emotion to point
                return self.myEmotions[counter*4+1]
        #check to make sure you don't get math error in square root
        elif math.pow(3.403, 2)-math.pow(tempX-3.003, 2)>=0 and math.pow(3.403, 2)-math.pow(tempX+3.003, 2)>=0:
            #check to see if the point in in the flower pedal
            if tempY<=math.sqrt(math.pow(3.403, 2)-math.pow(tempX-3.003, 2))+0.924 and tempY<=math.sqrt(math.pow(3.403, 2)-math.pow(tempX+3.003, 2))+0.924:
                if tempR<=1.53:
                    #return closest emotion to point
                    return self.myEmotions[counter*4+2]
                elif tempR<=2.65:
                    #return closest emotion to point
                    return self.myEmotions[counter*4+3]
                #there was an error
                else:
                    return "none"
        #check the outside of the pedal
        else:
            if tempPhi<=math.pi/2:
                #return closest emotion to point
                return self.myEmotions[counter*4]
            else:
                #check to stop lookup error in list
                if counter*4+4<len(self.myEmotions):
                    #return closest emotion to point
                    return self.myEmotions[counter*4+4]
                else:
                    #return closest emotion to point
                    return self.myEmotions[(counter*4+4)%32]

    def getX(self):
        return self.myX
    
    def getY(self):
        return self.myY
    
    def getR(self):
        return self.myR
    
    def getPhi(self):
        return self.myPhi
    
    #setters
    def setX(self, x):
        self.myX=x
        
        self.recalculatePolar()
        
    def setY(self, y):
        self.myY=y
        
        self.recalculatePolar()
        
    def setR(self, r):
        self.myR=r
        
        self.recalculateXY()
        
    def setPhi(self, phi):
        self.myPhi=phi
        
        self.recalculateXY()