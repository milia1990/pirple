#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 01:19:00 2018
Homework Assignment #2: Functions
@author: sergeymilkin
"""
#                   <<<modules>>>
import time
#                   <<<defined functions>>>

def Title(a):
    a = a + "I Got Love (feat. Рем Дигга)"
    return a

def Artist(a):
    a = a + "Miyagi & Эндшпиль"
    return a  

def Year(a):
    a = 0
    a = a + 2016
    return a

def WaitForCallFunction(call):
    call = "Wait..."
    print(call * 2)
    time.sleep(1.5)
    print(call * 2)
    time.sleep(1)
    print(call * 2)
    time.sleep(1.5)
    print("\nTadaaam!This is your called function :) \n")
    return call

def MyBestMusic():
    b = ''
    print("call function <Title>: ", Title(b))
    print("call function <Artist>: ", Artist(b))
    print("call function <Year>: ", Year(b))

#                   <<<main program>>>
enter_value = True
if enter_value == True:
    print("Sorry,but your input value is \"False\" and you lose.")
    print("But we always have a second chance!\nSo what now? (^-^)")
    time.sleep(5)
    call = ""
    WaitForCallFunction(call)
    MyBestMusic()
    
    
    







    
    