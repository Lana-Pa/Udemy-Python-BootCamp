import os

def clear():
    os.system('cls')


def x_o_choose():
    global who
    who = raw_input('Who is going first, X or 0? Your choice: ').upper()
    return who

def draw_board(d):
    print ''
    print '+---+---+---+'
    print '| %s | %s | %s |'% (d['1'],d['2'],d['3'])
    print '+---+---+---+'
    print '| %s | %s | %s |'% (d['4'],d['5'],d['6'])
    print '+---+---+---+'
    print '| %s | %s | %s |'% (d['7'],d['8'],d['9'])
    print '+---+---+---+'
    print ''

def place(d):
    
    choice = raw_input("Pick a number to place %s: " % (str(who)))
    d[choice]= who
    return d

def switch_turn(who):
    if who == 'X':
        return '0'
    if who == '0':
        return 'X'

def is_win(d):
    if d['1'] == d['2'] == d['3'] or \
       d['4'] == d['5'] == d['6'] or \
       d['7'] == d['8'] == d['9'] or \
                                     \
       d['1'] == d['4'] == d['7'] or \
       d['2'] == d['5'] == d['8'] or \
       d['3'] == d['6'] == d['9'] or \
                                     \
       d['1'] == d['5'] == d['9'] or \
       d['3'] == d['5'] == d['7']:

       return True

# -------------------------------------------------------------------------------------------
repeat = 'Y'
while repeat == 'Y' or 'y':
    d = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9'}
    x_o_choose()
    print 'Ok, %s, lets get started!' %(str(who))
    draw_board(d)

    for _ in range(9):

        place(d)
        clear()
        draw_board(d)
        is_win(d)
        if is_win(d):
            print "Game over! %s wins!" % (who)
            break
        else:
            who = switch_turn(who)

    if not is_win(d):
        print "Draw!"

    clear()
    repeat = raw_input("Want to play one more time? Y/N ").upper()
    if repeat == 'N':
         print "Bye! Have a good one!"
         break
