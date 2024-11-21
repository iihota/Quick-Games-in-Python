# like X,O just by numbers first player arrive to 15 first will win.
 
list1 = [0,0,0]
list2 = [0,0,0]
list3 = [0,0,0]
list_player1 = [1, 3, 5, 7, 9]
list_player2 = [0, 2, 4, 6, 8]
print("\n")
print(*list1,sep=" | ")
print("-----------")
print(*list2,sep=" | ")
print("-----------")
print(*list3,sep=" | ")


#==================================================================
while True:
    
    print("\n",list_player1)
    player1 = int(input("player_1 enter number what you want to play : "))
    while player1 not in list_player1 :
        player1 = int(input("player_1 enter avalid number what you want to play : "))
        

    player1_raw = int(input("player_1 enter raw's number from 1 to 3 : "))
    while player1_raw > 3 :
        player1_raw = int(input("player_1 enter raw's number from 1 to 3 : "))
        
        
    player1_colmn = int(input("player_1 enter colomn's number from 1 to 3 : "))
    while player1_colmn > 3 :
        player1_colmn = int(input("player_1 enter colomn's number from 1 to 3 : "))
        
        
        

    if player1_raw == 1 and player1_colmn == 1 and list1[0] == 0:
        list1[0] = player1

    if player1_raw == 1 and player1_colmn == 2 and list1[1] == 0:   
        list1[1] = player1

    if player1_raw == 1 and player1_colmn == 3 and list1[2] == 0:
        list1[2] = player1

    if player1_raw == 2 and player1_colmn == 1 and list2[0] == 0:
        list2[0] = player1

    if player1_raw == 2 and player1_colmn == 2 and list2[1] == 0:
        list2[1] = player1
        
    if player1_raw == 2 and player1_colmn == 3 and list2[2] == 0:
        list2[2] = player1
        
    if player1_raw == 3 and player1_colmn == 1 and list3[0] == 0:
        list3[0] = player1
        
    if player1_raw == 3 and player1_colmn == 2 and list3[1] == 0:
        list3[1] = player1
        
    if player1_raw == 3 and player1_colmn == 3 and list3[2] == 0:
        list3[2] = player1
    list_player1.remove(player1)

#----------------------------------------------------



    if sum(list1) == 15:
        print ("\n##############  player_1 win  #############\n")
        break

    if sum(list2) == 15:
        print ("\n##############  player_1 win  #############\n")
        break
    
    if sum(list3) == 15:
        print ("\n##############  player_1 win  #############\n")
        break
#---------------------------------------------------

    if list1[0] + list2[0] + list3[0] == 15 :
        print ("\n##############  player_1 win  #############\n")
        break
    
    if list1[1] + list2[1] + list3[1] == 15 :
        print ("\n##############  player_1 win  #############\n")
        break
    
    if list1[2] + list2[2] + list3[2] == 15 :
        print ("\n##############  player_1 win  #############\n")
        break
    
#-----------------------------------------------------

    if list3[0] + list2[1] + list1[2] == 15:
        print ("\n##############  player_1 win  #############\n")
        break
    
    if list3[2] + list2[1] + list1[0] == 15:
        print ("\n##############  player_1 win  #############\n")
        break
    
    if (len(list_player1) == 0 and len(list_player2) == 1) or (len(list_player1) == 1 and len(list_player2) == 0):
        print ("##########  draw  ##########")
        break

    print("\n")
    print(*list1,sep=" | ")
    print("-----------")
    print(*list2,sep=" | ")
    print("-----------")
    print(*list3,sep=" | ")


#====================================================

    print("\n",list_player2)


    player2 = int(input("player_2 enter number what you want to play : "))
    while player2 not in list_player2 :
        player2 = int(input("player_2 enter avalid number what you want to play : "))
        

    player2_raw = int(input("player_2 enter raw's number from 1 to 3 : "))
    while player2_raw > 3 :
        player2_raw = int(input("player_2 enter raw's number from 1 to 3 : "))
        
        
    player2_colmn = int(input("player_2 enter colomn's number from 1 to 3 : "))
    while player2_colmn > 3 :
        player2_colmn = int(input("player_2 enter colomn's number from 1 to 3 : "))
        
        
        
    if player2_raw == 1 and player2_colmn == 1 and list1[0] == 0:
        list1[0] = player2

    if player2_raw == 1 and player2_colmn == 2 and list1[1] == 0:   
        list1[1] = player2

    if player2_raw == 1 and player2_colmn == 3 and list1[2] == 0:
        list1[2] = player2

    if player2_raw == 2 and player2_colmn == 1 and list2[0] == 0:
        list2[0] = player2

    if player2_raw == 2 and player2_colmn == 2 and list2[1] == 0:
        list2[1] = player2
        
    if player2_raw == 2 and player2_colmn == 3 and list2[2] == 0:
        list2[2] = player2
        
    if player2_raw == 3 and player2_colmn == 1 and list3[0] == 0:
        list3[0] = player2
        
    if player2_raw == 3 and player2_colmn == 2 and list3[1] == 0:
        list3[1] = player2
        
    if player2_raw == 3 and player2_colmn == 3 and list3[2] == 0:
        list3[2] = player2
    
    list_player2.remove(player2)
    
    
#=========================================
        
    
    if sum(list1) == 15:
        print ("\n##############  player_2 win  #############\n")
        break

    if sum(list2) == 15:
        print ("\n##############  player_2 win  #############\n")
        break
    
    if sum(list3) == 15 :
        print ("\n##############  player_2 win  #############\n")
        break
#---------------------------------------------------

    if list1[0] + list2[0] + list3[0] == 15 :
        print ("\n##############  player_2 win  #############\n")
        break
    
    if list1[1] + list2[1] + list3[1] == 15 :
        print ("\n##############  player_2 win  #############\n")
        break
    
    if list1[2] + list2[2] + list3[2] == 15 :
        print ("\n##############  player_2 win  #############\n")
        break
    
#-----------------------------------------------------

    if list3[0] + list2[1] + list1[2] == 15:
        print ("\n##############  player_2 win  #############\n")
        break
    
    if list3[2] + list2[1] + list1[0] == 15:
        print ("\n##############  player_2 win  #############\n")
        break
    
    
    if (len(list_player1) == 0 and len(list_player2) == 1) or (len(list_player1) == 1 and len(list_player2) == 0):
        print ("##########  draw  ##########")
        break
    print("\n")
    print(*list1,sep=" | ")
    print("-----------")
    print(*list2,sep=" | ")
    print("-----------")
    print(*list3,sep=" | ")