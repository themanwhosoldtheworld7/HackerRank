# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:54:08 2020

@author: win10
"""



# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    Board = CreateBoard(n)    
    r_q,c_q = r_q-1,c_q-1
    for o in obstacles:
        O = Piece(o[0]-1,o[1]-1)
        PlacePeice(Board,O,-1)    
    
    Moves = 0
        
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'right') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'left') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'up') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'down') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'LDup') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'LDdown') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'RDup') 
    Moves = Moves + M
    
    Queen = Piece(r_q, c_q)
    M = checkMoves(Board,Queen,'RDdown') 
    Moves = Moves + M
                
    return Moves   

class Piece: 
    def __init__(self, X = int , Y = int): 
        self.X = X
        self.Y = Y
    
    def Move(self,x=0,y=0,D=None):
        if D == None:
            self.X = self.X + x
            self.Y = self.Y + y
            return
        if D == 'left':
            self.X,self.Y = self.X, self.Y - 1
            return     
        
        if D == 'right':
            self.X,self.Y = self.X, self.Y + 1
            return   
        
        if D == 'up':
            self.X,self.Y = self.X - 1, self.Y
            return   
        
        if D == 'down':
            self.X,self.Y = self.X +1 , self.Y
            return     
      
        if D == 'LDup':
            self.X,self.Y = self.X -1 , self.Y -1
            return 
        
        if D == 'LDdown':
            self.X,self.Y = self.X +1 , self.Y + 1
            return 
        
        if D == 'RDup':
            self.X,self.Y = self.X +1 , self.Y -1
            return 
        
        if D == 'RDdown':
            self.X,self.Y = self.X -1 , self.Y +1
            return 
        return

def CreateBoard(n):
   
    Board = [0] * n
    for i in range(n):
        Board[i] = [0]*n
    return Board
    
def PlacePeice(Board, P = Piece() , Identifier = int):
    Board[P.X][P.Y] = Identifier
    return

def WithinEdge(Board, P = Piece()):
    n = len(Board)
    if P.X <0 or P.X>n-1 or P.Y<0 or P.Y>n-1:
        return False
    return True

def checkMoves(Board, P = Piece(), Dir = str):
    CanMove = True
    M = 0
    while CanMove:
        P.Move(D=Dir)
        if WithinEdge(Board,P):
            M+=1                
        else:
            CanMove = False
            
            break
        if Board[P.X][P.Y] == -1:
            CanMove = False
            M = M-1
            
    return M
         

print(queensAttack(10,2,1,1,[[2,2],[3,4]]))


