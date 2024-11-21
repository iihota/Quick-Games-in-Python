# Connect- 4 game. A board of 7 columns x 6 rows is displayed that is held up in physical game
# as in figure below with row 1 is the bottom row.
# Players choose a symbol, either X or O. In their turn, they drop the symbol from top of the
# board (number 6) until it settles in the bottom empty cell. See video:
# https://www.youtube.com/watch?v=ylZBRUJi3UQ The first player to connect 4 symbols
# horizontally, vertically or diagonally wins.

#  -------------------------------------------------------------------

# Created in 2023-11-12




#  6 list's for the game item's (X or O) consider it empty.
numbers_list = [' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ']  # and this just for column representation - almost important.

list1 = ['   ','   ','   ','   ','   ','   ','   ']
list2 = ['   ','   ','   ','   ','   ','   ','   ']
list3 = ['   ','   ','   ','   ','   ','   ','   ']
list4 = ['   ','   ','   ','   ','   ','   ','   ']
list5 = ['   ','   ','   ','   ','   ','   ','   ']
list6 = ['   ','   ','   ','   ','   ','   ','   ']

#==========================================================
# to veiw it to the user.
print(*numbers_list,sep="|")
print("---------------------------")
print(*list1,sep="|")
print(*list2,sep="|")
print(*list3,sep="|")
print(*list4,sep="|")
print(*list5,sep="|")
print(*list6,sep="|")
#==========================================================

# infinity loop, but it will break when any one win.
while True:
#----------------------------------------------------------
    # to get the number of column to play in it.
    player_1 = int(input("player_1 enter number from 1 to 7 : "))
    while player_1 < 1 or player_1 > 7 or list1[player_1 - 1] == ' X ' or list1[player_1 - 1] == ' O ':
        player_1 = int(input("player_1 please enter a valid number form 1 to 7 : "))
#----------------------------------------------------------

    # this to look where will the " X " will be in in a column.
    if list6[player_1 - 1] == "   ":
        list6[player_1 - 1] = ' X '
    elif list5[player_1 - 1] == "   ":
        list5[player_1 - 1] = ' X '
    elif list4[player_1 - 1] == '   ':
        list4[player_1 - 1] = ' X '
    elif list3[player_1 - 1] == '   ':
        list3[player_1 - 1] = ' X '
    elif list2[player_1 - 1] == '   ':
        list2[player_1 - 1] = ' X '
    elif list1[player_1 - 1] == '   ':
        list1[player_1 - 1] = ' X '
#---------------------------------------------------------

    # veiw the again to the player's.
    print(*numbers_list,sep="|")
    print("---------------------------")
    print(*list1,sep="|")
    print(*list2,sep="|")
    print(*list3,sep="|")
    print(*list4,sep="|")
    print(*list5,sep="|")
    print(*list6,sep="|")

#----------------------------------------------------------
#                  after that look for if one win !!
#----------------------------------------------------------
#  there are four positions for win : lengthwise , crosswise , right tilted and left tilted.
#----------------------------------------------------------

    # first : crosswise.
    # look for " X X X X " in all list if it existing that mean player_1 win 
    width1 = ''.join(list1)
    width2 = ''.join(list2)
    width3 = ''.join(list3)
    width4 = ''.join(list4)
    width5 = ''.join(list5)
    width6 = ''.join(list6)
    if (" X  X  X  X " in width1) or (" X  X  X  X " in width2) or (" X  X  X  X " in width3) or (" X  X  X  X " in width4) or (" X  X  X  X " in width5) or (" X  X  X  X " in width6):
        print ("\n##############  player_1 win  #############\n")
        break
    
    
#------------------------------------------------------------
    # second : lengthwise.
    # look for " X X X X " in first item and cecond and... untel seventh item in every list and look  if it was existed that mean player_1 win
    hight = list1[player_1 - 1] + list2[player_1 - 1] + list3[player_1 - 1] + list4[player_1 - 1] + list5[player_1 - 1] + list6[player_1 - 1] 
    if (" X  X  X  X " in hight):
        print ("\n##############  player_1 win  #############\n")
        break

#-------------------------------------------------------------


    
    
#--------------------------------------------------------------

    # third : right tilted.
    # there is 6 miles i introduced them.
    # look for " X X X X " in all of them and look if it was existed that mean player_1 win.
    mil1 = list3[0] + list4[1] + list5[2] + list6[3]
    mil2 = list2[0] + list3[1] + list4[2] + list5[3] + list6[4]
    mil3 = list1[0] + list2[1] + list3[2] + list4[3] + list5[4] + list6[5]
    mil4 = list1[1] + list2[2] + list3[3] + list4[4] + list5[5] + list6[6]
    mil5 = list1[2] + list2[3] + list3[4] + list4[5] + list5[6] 
    mil6 = list1[3] + list2[4] + list3[5] + list4[6]
    
    if (" X  X  X  X " in mil1) or (" X  X  X  X " in mil2) or (" X  X  X  X " in mil3) or (" X  X  X  X " in mil4) or (" X  X  X  X " in mil5) or (" X  X  X  X " in mil6) :
        print ("\n##############  player_1 win  #############\n")
        break

#------------------------------------------------------------

    # same thing in left tilted.
    mil11 = str(list3[6] + list4[5] + list5[4] + list6[3])
    mil22 = str(list2[6] + list3[5] + list4[4] + list5[3] + list6[2])
    mil33 = str(list1[6] + list2[5] + list3[4] + list4[3] + list5[2] + list6[1])
    mil44 = str(list1[5] + list2[4] + list3[3] + list4[2] + list5[1] + list6[0])
    mil55 = str(list1[4] + list2[3] + list3[2] + list4[1] + list5[0] )
    mil66 = str(list1[3] + list2[2] + list3[1] + list4[0])
    
    if (" X  X  X  X " in mil11) or (" X  X  X  X " in mil22) or (" X  X  X  X " in mil33) or (" X  X  X  X " in mil44) or (" X  X  X  X " in mil55) or (" X  X  X  X " in mil66) :
        print ("\n##############  player_1 win  #############\n")
        break
    
    
    
    
    


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# same things in player_2 with out any difference

#----------------------------------------------------------
    player_2 = int(input("player_2 enter number from 1 to 7 : "))
    while player_2 < 1 or player_2 > 7 or list1[player_2 - 1] == ' X ' or list1[player_2 - 1] == ' O ':
        player_2 = int(input("player_2 please enter a valid number form 1 to 7 : "))
#----------------------------------------------------------

    if list6[player_2 - 1] == "   ":
        list6[player_2 - 1] = ' O '
    elif list5[player_2 - 1] == "   ":
        list5[player_2 - 1] = ' O '
    elif list4[player_2 - 1] == '   ':
        list4[player_2 - 1] = ' O '
    elif list3[player_2 - 1] == '   ':
        list3[player_2 - 1] = ' O '
    elif list2[player_2 - 1] == '   ':
        list2[player_2 - 1] = ' O '
    elif list1[player_2 - 1] == '   ':
        list1[player_2 - 1] = ' O '
        
#---------------------------------------------------------


    print(*numbers_list,sep="|")
    print("---------------------------")
    print(*list1,sep="|")
    print(*list2,sep="|")
    print(*list3,sep="|")
    print(*list4,sep="|")
    print(*list5,sep="|")
    print(*list6,sep="|")
#---------------------------------------------------------
    width1 = ''.join(list1)
    width2 = ''.join(list2)
    width3 = ''.join(list3)
    width4 = ''.join(list4)
    width5 = ''.join(list5)
    width6 = ''.join(list6)
    
#---------------------------------------------------------

    if (" O  O  O  O " in width1) or (" O  O  O  O " in width2) or (" O  O  O  O " in width3) or (" O  O  O  O " in width4) or (" O  O  O  O " in width5) or (" O  O  O  O " in width6):
        print ("\n##############  player_2 win  #############\n")
        break
    
#---------------------------------------------------------

    hight = list1[player_1 - 1] + list2[player_1 - 1] + list3[player_1 - 1] + list4[player_1 - 1] + list5[player_1 - 1] + list6[player_1 - 1] 
    if (" O  O  O  O " in hight):
        print ("\n##############  player_2 win  #############\n")
        break
    


#----------------------------------------------------------

    mil1 = str(list3[0] + list4[1] + list5[2] + list6[3])
    mil2 = str(list2[0] + list3[1] + list4[2] + list5[3] + list6[4])
    mil3 = str(list1[0] + list2[1] + list3[2] + list4[3] + list5[4] + list6[5])
    mil4 = str(list1[1] + list2[2] + list3[3] + list4[4] + list5[5] + list6[6])
    mil5 = str(list1[2] + list2[3] + list3[4] + list4[5] + list5[6] )
    mil6 = str(list1[3] + list2[4] + list3[5] + list4[6])
    
    if (" O  O  O  O " in mil1) or (" O  O  O  O " in mil2) or (" O  O  O  O " in mil3) or (" O  O  O  O " in mil4) or (" O  O  O  O " in mil5) or (" O  O  O  O " in mil6) :
        print ("\n##############  player_2 win  #############\n")
        break
    
#----------------------------------------------------------
    
    mil11 = str(list3[6] + list4[5] + list5[4] + list6[3])
    mil22 = str(list2[6] + list3[5] + list4[4] + list5[3] + list6[2])
    mil33 = str(list1[6] + list2[5] + list3[4] + list4[3] + list5[2] + list6[1])
    mil44 = str(list1[5] + list2[4] + list3[3] + list4[2] + list5[1] + list6[0])
    mil55 = str(list1[4] + list2[3] + list3[2] + list4[1] + list5[0] )
    mil66 = str(list1[3] + list2[2] + list3[1] + list4[0])
    
    if (" O  O  O  O " in mil11) or (" O  O  O  O " in mil22) or (" O  O  O  O " in mil33) or (" O  O  O  O " in mil44) or (" O  O  O  O " in mil55) or (" O  O  O  O " in mil66) :
        print ("\n##############  player_2 win  #############\n")
        break
    
    
    