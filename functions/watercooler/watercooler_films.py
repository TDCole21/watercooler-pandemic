from flask import Flask, render_template, request, redirect, url_for
import os
import re
import random

app = Flask(__name__) #__name__ is for best practice


def films_home():
    users_temp=[]
    Users=[]
    users_file = open("./data/Users.txt", "r")
    for x in users_file:
        users_temp.extend(x.split(";"))
    for i in users_temp:
        Users.append(i.split(":"))
    users_file.close()

    del Users[-1]

    films_temp=[]
    Films=[]
    films_file = open("./data/watercooler/Films.txt", "r")
    for x in films_file:
        films_temp.extend(x.split(";"))
    for i in films_temp:
        Films.append(i.split(":"))
    films_file.close()

    del Films[-1]

    streaming_platforms_temp=[]
    Streaming_Platforms=[]
    streaming_platforms_file = open("./data/watercooler/Streaming_Platforms.txt", "r")
    for x in streaming_platforms_file:
        Streaming_Platforms.extend(x.split(";"))
    streaming_platforms_file.close()

    del Streaming_Platforms[-1]

    films_upcoming_selection=[]
    films_finished_selection=[]
    films_chosen_selection=[]
    for i in Films:
        if int(i[3])==0:
            films_upcoming_selection.append(i)
        elif int(i[3])==1:
            films_chosen_selection.append(i)
        else:
            films_finished_selection.append(i)

    return (films_upcoming_selection, Users, Streaming_Platforms, films_finished_selection, films_chosen_selection)







def films_edit():
    if request.method == "POST":
        details=request.form
        films_name=details['films_name']
        streaming_platforms_name=details.getlist('streaming_platforms_name')
        users_name=details['users_name']
        users_password=details['users_password']

        if len(streaming_platforms_name)>0:
            Streaming_Platforms=""
            for i in range(len(streaming_platforms_name)-1):
                Streaming_Platforms=Streaming_Platforms+str(streaming_platforms_name[i])+", "
            if Streaming_Platforms != "":
                Streaming_Platforms=Streaming_Platforms[0:len(Streaming_Platforms)-2]+" and "+str(streaming_platforms_name[-1])
            else:
                Streaming_Platforms=Streaming_Platforms+str(streaming_platforms_name[-1])

        users_temp=[]
        Users=[]
        users_file = open("./data/Users.txt", "r")
        for x in users_file:
            users_temp.extend(x.split(";"))
        for i in users_temp:
            Users.append(i.split(":"))
        users_file.close()

        del Users[-1]

        for i in range(len(Users)):
            if Users[i][0]==users_name and Users[i][1]==users_password:

                if details['action'] == 'Add':
                    films_name = re.sub("^\s*", "", films_name)
                    films_name = re.sub(":", "-", films_name)
                    films_name = re.sub(";", "-", films_name)
                    Films=open("./data/watercooler/Films.txt", "a")
                    Films.write(films_name+":"+Streaming_Platforms+":"+users_name+":0;")
                
                elif details['action'] == 'Remove':
                    films_temp=[]
                    Films=[]
                    films_file = open("./data/watercooler/Films.txt", "r")
                    for x in films_file:
                        films_temp.extend(x.split(";"))
                    for i in films_temp:
                        Films.append(i.split(":"))
                    films_file.close()

                    del Films[-1]

                    films_file = open("./data/watercooler/Films.txt", "w")
                    for i in range(len(Films)):
                        if Films[i][0]==films_name:
                            pass
                        else:
                            films_file.write(Films[i][0]+":"+Films[i][1]+":"+Films[i][2]+":"+Films[i][3]+";")


                elif users_name=="Cole" and details['action'] == 'Shuffle':
                    films_temp=[]
                    Films=[]
                    films_file = open("./data/watercooler/Films.txt", "r")
                    for x in films_file:
                        films_temp.extend(x.split(";"))
                    for i in films_temp:
                        Films.append(i.split(":"))
                    films_file.close()

                    del Films[-1]

                    films_choice = []
                    for i in range(len(Films)):
                        if Films[i][3]=="1":
                            Films[i][3]="0"
                        if Films[i][3]=="0":
                            films_choice.append(Films[i])

                    random.shuffle(films_choice)

                    films_choice[0][3]="1"

                    for i in range(len(Films)):
                        if Films[i][3]=="2":
                            films_choice.append(Films[i])

                    films_file = open("./data/watercooler/Films.txt", "w")
                    for i in range(len(films_choice)):
                        films_file.write(films_choice[i][0]+":"+films_choice[i][1]+":"+films_choice[i][2]+":"+films_choice[i][3]+";") 


                
                elif users_name=="Cole" and details['action'] == 'Finished':
                    films_temp=[]
                    Films=[]
                    films_file = open("./data/watercooler/Films.txt", "r")
                    for x in films_file:
                        films_temp.extend(x.split(";"))
                    for i in films_temp:
                        Films.append(i.split(":"))
                    films_file.close()

                    del Films[-1]

                    films_choice = []
                    for i in range(len(Films)):
                        if Films[i][3]=="1":
                            Films[i][3]="2"


                    films_file = open("./data/watercooler/Films.txt", "w")
                    for i in range(len(Films)):
                        films_file.write(Films[i][0]+":"+Films[i][1]+":"+Films[i][2]+":"+Films[i][3]+";") 
