import time,random,csv

#Config
tablesize = 9 #For tables 9x9, 12x12, 15x15,etc... (actually can be as large as you want, if you have the time for it)

#Generate times table answer dictionary
ogdict = {}
for a in range(tablesize):
    for b in range(tablesize):
        ogdict[str(a+1)+'*'+str(b+1)] = (a+1)*(b+1) #add key/value pair a:b to dict like so dict[a]=b


#Generate (answer times for times table) dictionary
timesdict = {}
for a in range(tablesize):
    for b in range(tablesize):
        timesdict[str(a+1)+'*'+str(b+1)] = 'null'
 
 
#Make copy of dicts as list for ordered accessing
oglist = list(ogdict.items()) #items() returns a list of tuples, one for each key/value pair in dict
timeslist = list(timesdict.items())
#print(oglist)

#Ask user for answer
while 'null' in timesdict.values(): #Keep asking until user has answered correctly the whole times table
    choice=random.randint(0,(tablesize*tablesize-1))
    if timesdict[oglist[choice][0]]!='null': #If user has already answered this question correctly, don't ask
        continue           #continue is for breaking this while instance and starting the next
    print(oglist[choice][0])
    start = time.time() #Start taking the time
    userInput = input() 
    
#Check user answer, record time to answer if correct 
    if userInput.isdigit()==False:  #Sanitize inputs to avoid valueErrors
        print('TRY AGAIN')
    elif int(userInput) != oglist[choice][1]:
        print('TRY AGAIN')
        while userInput != str(oglist[choice][1]):
            userInput = input()
            if userInput != str(oglist[choice][1]):
                print('TRY AGAIN')
            else:
                end = time.time()
                print('CORRECT')
                t = end-start
                t = round(t,1)
                timesdict[oglist[choice][0]] = t
    else:
        end = time.time()
        print('CORRECT')
        t = end-start
        t = round(t,1)
        timesdict[oglist[choice][0]] = t
        
print(timesdict)

#Export timesdict as csv (boilerplate-ish)
with open('Times table report.csv', mode = 'w',newline='') as report1: #If you don't put newline='' it makes extra blank rows. According to StackOverflow it's because of some windows fuckery.
    writer = csv.writer(report1, dialect='excel',delimiter=';')
       
    #Construct table: make lists like (1*1,time,1*2,time,etc.)/(2*1,time,2*2,time,etc.),etc. then write each as one row
    for a in range(0,tablesize):
        auxlist = []  #Auxiliary list for writing csv tables of varying size (design requirement)
        for b in range(0,tablesize):
            auxlist.append(oglist[a*tablesize+b][0]) #append 2*3
            auxlist.append(timesdict[oglist[a*tablesize+b][0]]) #append time user took to answer
        writer.writerow(auxlist) #.writerow() can take as argument lists of any size, allowing warying row lenghts
report1.close()    

print('A csv file (you can open it with excel) with you results has been generated. You can also check them out just above.')

#By Milan Weibel @ UC Chile, feel free to distribute giving due credit
