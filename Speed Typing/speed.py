import time

while True:
    t1=time.time()
    inputtext=str(input('START TYPING TO CHECK YOUR SPEED:'))
    t2=time.time()
    wordcount=len(inputtext.split())
    timetaken=t2-t1
    wpm=wordcount/timetaken
    print("WPM=",wpm)
    print("Timetaken=",timetaken)
