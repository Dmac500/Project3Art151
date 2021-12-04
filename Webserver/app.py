from flask import Flask, render_template ,jsonify
import numpy as np
import requests
import RPi.GPIO as GPIO
import time

#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
   
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
   
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
   
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    return distance
 

app = Flask(__name__)





Fighter=[]
key = "e86a7e8f44a945e48b1dfadbf47ee10b"
url = f"https://api.sportsdata.io/v3/mma/scores/json/Fighters?key={key}"
rec = requests.get(url).json()


      


@app.route("/")
def helloworld():

    templateData = {
        'title': "hello",
         'x': 10
    }
    

    return render_template('index.html',**templateData)

@app.route("/testcall", methods = ['POST'])
def updateCall():
    
    
    if distance() < 10 and distance() > 0:
         Fighter.clear()
        
         for i in range(len(rec)): 
          if rec[i]["WeightClass"] == 'Featherweight':
            Fighter.append(rec[i])

         newindex = np.random.randint(0,high=len(Fighter)-1)
         newindex1 = np.random.randint(0,high=len(Fighter)-1)
         print(distance())
    elif distance() < 20 and distance() > 10:
        Fighter.clear()
      
        for i in range(len(rec)):
            if rec[i]["WeightClass"] == 'Lightweight':
                Fighter.append(rec[i])

        newindex = np.random.randint(0,high=len(Fighter)-1)
        newindex1 = np.random.randint(0,high=len(Fighter)-1)
        print(distance())   
    elif distance() > 20 and distance() < 30:
      
        Fighter.clear()
        
        for i in range(len(rec)):
         if rec[i]["WeightClass"] == 'Welterweight':
            Fighter.append(rec[i])

        newindex = np.random.randint(0,high=len(Fighter)-1)
        newindex1 = np.random.randint(0,high=len(Fighter)-1)
        print(distance())
    elif distance() > 40 and distance() < 50:
      
        Fighter.clear()
        
        for i in range(len(rec)):
         if rec[i]["WeightClass"] == 'Middleweight':
            Fighter.append(rec[i])
            
        newindex = np.random.randint(0,high=len(Fighter)-1)
        newindex1 = np.random.randint(0,high=len(Fighter)-1)
        print(distance())
    elif distance() > 50 and distance() < 60:
      
        Fighter.clear()
      
        for i in range(len(rec)):
         if rec[i]["WeightClass"] == 'Heavyweight':
            Fighter.append(rec[i])
        newindex = np.random.randint(0,high=len(Fighter)-1)
        newindex1 = np.random.randint(0,high=len(Fighter)-1)
        print(distance())
    
        
    rand_num = Fighter[newindex]
    rand_num1 = Fighter[newindex1]
    print(distance())
    fighter1={
        "FirstName" : rand_num["FirstName"] ,
        "LastName" : rand_num["LastName"] , 
        "Nickname" : rand_num["Nickname"] ,
        "wins" :  rand_num["Wins"], 
        "Losses":  rand_num["Losses"],
        "Reach" : rand_num["Reach"],
        "TechnicalKnockouts": rand_num["TechnicalKnockouts"],
        'Submissions': rand_num["Submissions"],
        'TitleWins' : rand_num["TitleWins"],
        'TitleLosses': rand_num["TitleLosses"],
        "strkper" : rand_num["CareerStats"]["SigStrikeAccuracy"],
        "TakedownAverage":rand_num["CareerStats"]["TakedownAverage"],
        "SigStrikesLandedPerMinute":rand_num["CareerStats"]["SigStrikesLandedPerMinute"],
        "WeightClass":rand_num["WeightClass"],
        "winper" : rand_num["Wins"]/(rand_num["Wins"]+rand_num["Losses"]) * 100,}
    fighter2 ={
        "FirstName1" : rand_num1["FirstName"] ,
        "LastName1" : rand_num1["LastName"] , 
        "Nickname1" : rand_num1["Nickname"] ,
        "wins1" : rand_num1["Wins"], 
        "Losses1":  rand_num1["Losses"],
        "Reach1" : rand_num1["Reach"],
        "TechnicalKnockouts1": rand_num1["TechnicalKnockouts"],
        'Submissions1': rand_num1["Submissions"],
        'TitleWins1' : rand_num1["TitleWins"],
        'TitleLosses1': rand_num1["TitleLosses"],
        "strkper1" : rand_num1["CareerStats"]["SigStrikeAccuracy"],
        "TakedownAverage1":rand_num1["CareerStats"]["TakedownAverage"],
        "WeightClass1":rand_num1["WeightClass"],
        "SigStrikesLandedPerMinute1":rand_num1["CareerStats"]["SigStrikesLandedPerMinute"],
        "winper1" : rand_num1["Wins"]/(rand_num1["Wins"]+rand_num1["Losses"]) * 100
        }
    
    fighter = {
    "fighter1" : fighter1,
    "fighter2" : fighter2
    }
    
     
    return jsonify('', render_template("rand_num.html",**fighter))



if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=80, debug= True)