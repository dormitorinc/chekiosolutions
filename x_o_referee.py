def checkio(game):
    
    
    ls=[]
    for i in range(0,3):
        ls.append(game[i])
    winner = ''
    draw = 0
    if ls[0][0] == ls[1][1]==ls[2][2] and ls[0][0]!= '.':
        winner = ls[0][0]
        
        draw +=1
    if ls[0][2] == ls[1][1]== ls[2][0] and ls[1][1]!= '.':
        winner = ls[1][1]
        draw+=1
    for row in game:
        if row[0] == row[1] == row[2] and row[0] != '.':
            winner = row[0]
            draw +=1
        else:
            pass

    new_game = zip(*game)
    
    
    for x in new_game:
        if x[0] == x[1] == x[2] and x[0] != '.':
            winner = x[0]
            draw+=1
        else:
            pass
    
    if winner != '' and draw != 0:
        return winner
    else:
        return 'D'









    
    
    
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

