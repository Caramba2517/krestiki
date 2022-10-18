print('Добро пожаловать в игру Крестики/Нолики v.0.1 by Caramba\n ______')
print('Правила игры: \nДля выбора клетки, нужно указать ее адрес\n(Пример: 5 )\nНачинают крестики.\n')

board = list(range(1, 10))
code_win = [(1,2,3),(1,4,7),(7,8,9),(3,6,9),(1,5,9),(7,8,3),(4,5,6),(2,5,8)]


def game_board():
    print('_____________')
    for i in range(3):
        print('|', board[i*3], '|', board[i*3 + 1], '|', board[i*3 + 2], '|')
    print('_____________')

def cheack_win():
    for i in code_win:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
            return board[i[1]-1]
    else:
        return False

def point(token):
    while True:
        i = input('Выбери поле для ' + token + ': ')
        if i not in '123456789':
            print('Не-не, такого поля нет =(\nПопробуй еще раз.')
            continue
        i = int(i)
        if str(board[i - 1]) in 'XO':
            print('Слепой? Поле занято, давай заново.')
            continue
        board[i - 1] = token
        break

def game():
    step = 0
    while True:
        game_board()
        if step % 2 == 0:
            point('X')
        else:
            point('O')
        if step >3:
            win = cheack_win()
            if win:
                game_board()
                print(win, '- это победа!')
                break
        step +=1
        if step >8:
            game_board()
            print('Ничья, расходимся.')
            break




game()

