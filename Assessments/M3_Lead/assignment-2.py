# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
stt=int(input("enter: "))
sot=int(input("enter: "))
sth=int(input("enter: "))
soh=int(input("enter: "))
temp=random.randint(stt,sot)
hum=random.randint(sth,soh)
while(1):
    if(temp>90 and hum>85):
        print("alarm rang")
    else:
        break;


