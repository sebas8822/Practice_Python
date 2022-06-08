# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:38:57 2022

@author: sebas
"""

class ShortQuestion():
    
    def __init__(self, ques, ans):
        self.question = ques
        self.answer = ans
        
    def getQuestion(self):
        return self.question
    
    
    def check_answer(self,attempt):
        return attempt == self.answer