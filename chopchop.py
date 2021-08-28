
player_1=[1,1]
player_2=[1,1]
print('-> enter A for attack enter\n-> enter S for split')

#player 1
def p1():
    movep1=input('enter attack move A\S : ')
    if movep1=='A' or movep1=='a':
        print('for attack enter move combination: \nLR for left to right \nLL for left to left \nRR for right to right \nRL for right to left')            
        mcp1=input('move combination= ')
        
        if mcp1=='lr' or mcp1== 'LR':
            player_2[1] += player_1[0]
        if mcp1=='ll' or mcp1=='LL':
            player_2[0]+= player_1[0]
        if mcp1=='rr' or mcp1=='RR':
           player_2[1]+= player_1[1]           
        if mcp1=='rl' or mcp1=='RL':
            player_2[0]+= player_1[1]
        
        
    if movep1=='S' or movep1=='s':
        print('for split \n enter hand to be splitted (1 for left and 2 for right)')
        handp1= input('enter hand (1 or 2)=')
        leftsp1=input('<left hand after split>=')
        rightsp1=input('<right hand after split>=')

        try:
            if(handp1==1):
                if(player_1[0]>1):
                    player_1[0]= leftsp1
                    player_1[1]=rightsp1
                
            if(handp1==2):
                if(player_1[2]>1):
                    player_1[0]= leftsp1
                    player_1[1]=rightsp1
        except Exception:
	        print('split can be done only when selected hand has more than one finger')
        
    print('current status:')
    print('player 1=',player_1 )
    print('player 2=',player_2 )

#player 2
def p2():
    movep2=input('enter attack move A\S : ')
    if movep2=='A' or movep2=='a':
        print('for attack enter move combination: \nLR for left to right \nLL for left to left \nRR for right to right \nRL for right to left')            
        mcp2=input('move combination= ')
        if mcp2=='lr' or mcp2== 'LR':
            player_1[1] += player_1[0]
        if mcp2=='ll' or mcp2=='LL':
            player_1[0]+= player_1[0]
        if mcp2=='rr' or mcp2=='RR':
           player_1[1]+= player_1[1]           
        if mcp2=='rl' or mcp2=='RL':
            player_1[0]+= player_1[1]
        
        
    if movep2=='S' or movep2=='s':
        print('for split \n enter hand to be splitted (1 for left and 2 for right)')
        handp2= input('enter hand (1 or 2)=')
        leftsp2=input('<left hand after split>=')
        rightsp2=input('<right hand after split>=')

        try:
            if(handp2==1):
                if(player_2[0]>1):
                    player_2[0]= leftsp2
                    player_2[1]=rightsp2
                
            if(handp2==2):
                if(player_1[2]>1):
                    player_1[0]= leftsp2
                    player_1[1]=rightsp2
        except Exception:
	        print('split can be done only when selected hand has more than one finger')
        
    print('current status:')
    print('player 1=',player_1 )
    print('player 2=',player_2 )

while (player_1[0]<5 or player_1[1]<5) and (player_2[0]<5 or player_2[1]<5):
    print('player 1 turn')
    p1()
    
    print('player 2 turn')
    p2()
    
if(player_1[0]>=5 and player_1[1]>=5):
    print('player 1 wins')
if(player_2[0]>=5 and player_2[1]>=5):
    print('player 2 wins')    
