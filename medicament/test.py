# -*- coding: utf-8 -*-

'''
@author: a_kayerov
'''
def list_find(lst): 
    for x in lst:
        print(x) 
        for elem in x:
            print(elem)  
    return 0

s = [["line1",0,0,0,0,0,0,0,0],["line2",0,0,0,0,0,0,0,0],["line3",0,0,0,0,0,0,0,0],["line4",0,0,0,0,0,0,0,0]]
row = ["line1","line2","line3","line4"]    

list_find(s) 



     