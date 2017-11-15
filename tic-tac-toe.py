#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
A Tic Tac Toe Game

@author: theoklitosBam7
'''


import random
import time

marker = {'Player 1': 'X', 'Player 2': 'O'}


def display_board(board):
    '''
    Display a numbered board for the Tic Tac Toe Game.
    '''
    print('    |    |')
    print('  ' + board[7] + ' |  ' + board[8] + ' |  ' + board[9])
    print('7   |8   |9')
    print('-------------')
    print('    |    |')
    print('  ' + board[4] + ' |  ' + board[5] + ' |  ' + board[6])
    print('4   |5   |6')
    print('-------------')
    print('    |    |')
    print('  ' + board[1] + ' |  ' + board[2] + ' |  ' + board[3])
    print('1   |2   |3')


def choose_first():
    '''
    Random drawing for the first player.
    '''
    choice = random.randint(1, 2)
    if choice == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def display_score(score):
    '''
    Display the final score for the Game.
    '''
    print('FINAL SCORE\n')
    for x in ['Player 1', 'Player 2']:
        if x not in score.keys():
            score[x] = 0
    for x, y in score.items():
        print('{0}: {1}'.format(x, y))


def place_marker(board, mark, position):
    '''
    Place the mark symbol in specific position on the board.
    '''
    board[position] = mark


def win_check(board, mark):
    '''
    Check if the mark symbol creates tic-tac-toe.
    '''
    if (board[1] == mark and board[2] == mark and board[3] == mark) or \
            (board[4] == mark and board[5] == mark and board[6] == mark) or \
            (board[7] == mark and board[8] == mark and board[9] == mark) or \
            (board[1] == mark and board[4] == mark and board[7] == mark) or \
            (board[2] == mark and board[5] == mark and board[8] == mark) or \
            (board[3] == mark and board[6] == mark and board[9] == mark) or \
            (board[1] == mark and board[5] == mark and board[9] == mark) or \
            (board[3] == mark and board[5] == mark and board[7] == mark):
        return True
    else:
        return False


def board_check(board):
    '''
    Check if there are any empty boxes on the board.
    '''
    empty = 0
    for x in range(1, 10):
        if board[x] == ' ':
            empty += 1
    if empty != 0:
        return False
    else:
        return True


def player_choice(board, turn):
    '''
    The player chooses a box. Check if the box is already occupied.
    '''
    while True:
        move = input(turn + ' [ ' + marker[turn] + ' ]: Choose ' +
                     ' a box (1-9): ')
        if move.isdigit():
            move = int(move)
            if move in range(1, 10):
                if board[move] != ' ':
                    print('The box ' + str(move) + ' is already' +
                          ' occupied')
                    continue
                else:
                    break
            else:
                continue
        else:
            continue
    return move


def replay():
    '''
    Ask the player if he wants to play again.
    '''
    while True:
        a = input('Do you want play again? (yes/no): ')
        if a in ['yes', 'y']:
            return True
        elif a in ['no', 'n']:
            return False
        else:
            continue


def next_player(turn):
    '''
    Return the next player.
    '''
    if turn == 'Player 1':
        turn = 'Player 2'
    else:
        turn = 'Player 1'
    return turn


def main():
    score = {}  # Dictionary with the score
    print('Here we are! \nLottery in progress ', end='')
    for t in range(10):
        print(".", flush='True', end=' ')
        time.sleep(0.2)
    print()
    turn = choose_first()
    print(turn + ' plays first.')
    first = turn
    game_round = 1
    while True:
        theBoard = [' '] * 10
        game_on = True
        while game_on:
            display_board(theBoard)
            position = player_choice(theBoard, turn)
            place_marker(theBoard, marker[turn], position)
            if win_check(theBoard, marker[turn]):
                display_board(theBoard)
                print('The winner is ' + turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            elif board_check(theBoard):
                display_board(theBoard)
                print('Tie!')
                game_on = False
            else:
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round > 1:
                ending = 's'
            print("\nAfter {0} round{1}".format(game_round, ending))
            display_score(score)
            break
        else:
            game_round += 1
            turn = next_player(first)
            first = turn
            print('\nNew Game')


main()
