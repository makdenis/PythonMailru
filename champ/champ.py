#!/usr/bin/env python
import random
def champ(teams,): #проведение игр
    i=0
    j=0
    while(i<len(teams)):
        while (j < len(teams)):
            if(j>i):
                score = {'N1': '', 'N2': '', 'G1': 0, 'G2': 0}
                score['N1']=teams[i]['Name']
                score['N2'] = teams[j]['Name']
                teams[j]['Fails']=teams[i]['Goals']=score['G1'] = random.randint(0,4)
                teams[i]['Fails'] = teams[j]['Goals']=score['G2'] = random.randint(0, 4)

                #print(score)
                if(score['G1']>score['G2']):
                    teams[i]['Win']+=1
                    teams[i]['Points']+=3
                    teams[j]['Lose'] += 1

                if (score['G2'] > score['G1']):
                    teams[j]['Win'] += 1
                    teams[j]['Points'] +=3
                    teams[i]['Lose'] += 1
                if (score['G2'] == score['G1']):
                    teams[j]['Neutral'] += 1
                    teams[i]['Neutral'] +=1
                    teams[i]['Points'] +=1
                    teams[j]['Points']+=1
                print("{0:5} - {1:5}   {2:1} - {3:1}".format(score['N1'], score['N2'], score['G1'], score['G2']))
                table.append(score)
                #print(table)

            j+=1
        j=0
        i+=1
def search(table): #поиск матча
    a=""
    b=""
    print("Введите первую команду")
    a=input()
    print("Введите вторую команду")
    b=input()
    for i in table:

        if((i['N1']==a and i['N2']==b) or (i['N1']==b and i['N2']==a) ):
            print("{0} - {1}   {2} - {3}".format(i['N1'],i['N2'],i['G1'],i['G2']))
def result(teams): #итоговая таблица
    teams=reversed(sorted(teams, key=lambda x: x['Points']))
    print('Name    Points    Win  Lose  Neutral  Goals  Fails')
    for i in teams:
        print("{0:5}      {1:2}     {2:2}    {3:2}   {4:4}   {5:5}   {6:3}".format(i['Name'],i['Points'],i['Win'],i['Lose'],i['Neutral'],i['Goals'],i['Fails']))
def stats(teams):  #статистика команды
    print("Введите команду")
    name=input()
    for i in teams:
        if(i['Name']==name):
            print(i)
table=[]

Keks={'Name':'Keks','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
Lols={'Name':'Lols','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
BMSTU={'Name':'BMSTU','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
MSU={'Name':'MSU','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
RGGU={'Name':'RGGU','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
HSE={'Name':'HSE','Points':0,'Win':0,'Lose':0,'Neutral':0,'Goals':0,'Fails':0}
teams = [Keks, Lols, BMSTU, MSU, RGGU, HSE]
print("Проведение чемпионата")
champ(teams)
print("итоговая таблица")
result(teams)
print("поиск матча")
search(table)
print("статистика команды")
stats(teams)

