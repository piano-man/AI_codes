#!/usr/bin/python
import random
board = []
bar = []
dice_rolls = []
player = 0


def can_bear_off():
    '''
    This function checks if we can actually bear
    off a player
    '''

    bear_off = (0 == bar[player])
    for i in range(1, 19):
        index = (25 - i) if (2 == player) else i
        if bear_off:
            bear_off = (len(board[index]) == 0) or (board[index][0] != player)

    return bear_off


def get_bear_off_move():
    '''
    1. Check if direct bear offs are possible
    2. Check if inside home moves are possible
    3. Now check if jumps are possible
    '''
    poss_moves = []

    # this calculates direct moves
    for i in range(1, 7):
        index = (25 - i) if (1 == player) else i
        end = 0 if (2 == player) else 25
        if i in dice_rolls and len(board[index]) != 0 and board[index][0] == player:
            poss_moves.append([index, end])

    # this calculates inside home moves
    for i in range(1, 6):
        index = 18 + i if (1 == player) else (7 - i)
        if 0 != len(board[index]) and board[index][0] == player:
            for j in range(1, 7 - i):
                index2 = index - j if (2 == player) else index + j
                if j in dice_rolls:
                    if (0 == len(board[index2])) or (1 == len(board[index2])) or (board[index2][0] == player):
                        poss_moves.append([index, index2])

    move = []
    if 0 != len(poss_moves):
        move = random.sample(poss_moves, 1)[0]
        dice_rolls.remove(abs(move[0] - move[1]))
    else:
        for i in range(1, 7):
            index = (25 - i) if (1 == player) else i
            end = 0 if (2 == player) else 25
            if len(board[index]) != 0 and board[index][0] == player:
                for dice_roll in dice_rolls:
                    if i < dice_roll:
                        move = [index, end]
                        dice_rolls.remove(dice_roll)
                        return move

    return move


def get_normal_moves():
    '''
    this gets one possible move
    '''

    poss_moves = []
    for i in range(1, 24):
        index = (25 - i) if (2 == player) else i
        if 0 != len(board[index]) and board[index][0] == player:
            for j in range(1, min(7, 25 - i)):
                index2 = (index - j) if (2 == player) else (index + j)
                if j in dice_rolls:
                    if len(board[index2]) <= 1 or board[index2][0] == player:
                        poss_moves.append([index, index2])

    if 0 == len(poss_moves):
        return poss_moves

    return random.sample(poss_moves, 1)[0]


def get_bar_move():
    '''
    If the bar is not empty, then I am forced
    to remove the checkers from the bar first
    '''

    poss_moves = []
    for i in range(1, 7):
        index = (25 - i) if 2 == player else i
        if i in dice_rolls:
            if len(board[index]) <= 1 or board[index][0] == player:
                poss_moves.append(index)

    if len(poss_moves) == 0:
        return poss_moves

    move = random.sample(poss_moves, 1)[0]
    return [-1, move]


def get_moves():
    '''
    as long as there are dice rolls present,
    one should make a move
    '''
    moves = []
    while 0 != len(dice_rolls):
        if 0 != bar[player]:
            move = get_bar_move()
            if len(move) == 0:
                break
            bar[player] -= 1
            dice_roll = (25 - move[1]) if (2 == player) else move[1]
            dice_rolls.remove(dice_roll)
            if len(board[move[1]]) == 1 and board[move[1]][0] != player:
                board[move[1]].pop()

            board[move[1]].append(player)
            moves.append(move)
        else:
            if can_bear_off():
                move = get_bear_off_move()
                if len(move) == 0:
                    break
            else:
                move = get_normal_moves()
                if 0 == len(move):
                    break
                dice_rolls.remove(abs(move[0] - move[1]))

            board[move[0]].pop()
            if len(board[move[1]]) == 1 and board[move[1]][0] != player:
                board[move[1]].pop()

            board[move[1]].append(player)
            moves.append(move)
    return moves


if __name__ == '__main__':
    player = input()
    for i in range(26):
        x = map(int, raw_input().strip().split())
        if 2 == len(x):
            board.append([x[1]] * x[0])
        else:
            board.append([])

    bar.append(0)
    bar.append(input())
    bar.append(input())

    rolls = input()
    for i in range(rolls):
        dice_rolls.append(input())

    dice_rolls.sort()
    moves = get_moves()
    print "\n".join(" ".join(str(m) for m in move) for move in moves)

