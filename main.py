import os
def clear_screen():
    os.system("cls")
class Player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letters only) >>> ")
            if name.isalpha() == True:
                self.name = name
                break
            print("Please use letters only.")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name} choose single letter ")
            if symbol.isalpha() and len(symbol)==1:
                self.symbol=symbol.upper()
                break
            print("please choose single letter only")
class Menu:
    def display_main_menu(self):
        print('welcome to my x-o game!')
        print('1. Start game')
        print('2. Quit game')
        choice=input('Choice from menu>>> ')
        return choice
    def dispaly_endgame_menu(self):
        menu_text=f"""
        {game.players[game.current_player_index].name} is the winner!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2):"""
        choice=input(menu_text)
        return choice
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]
    def display_board(self):
        for i in range(0,9,3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-"*5)
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice -1] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]
    def is_valid_move(self, choice):
        return str(self.board[choice -1]).isdigit()
    
class Game:
    def __init__(self):
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        self.correction=[0,1,0,1,0,1,0,1,0,1,0,1,0]
        self.indexation=0
        self.current_player_index=self.correction[self.indexation]
    def start_game(self):
        choice= self.menu.display_main_menu()
        if choice =="1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number,player in enumerate(self.players, start=1):
            print(f'Player "{number}" enter your details:\n')
            player.choose_name()
            player.choose_symbol()
            clear_screen( )

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice=self.menu.dispaly_endgame_menu()
                if choice=="1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def quit_game(self):
        print("Thank you for Playing!")

    def play_turn(self):
        player = self.players[self.current_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:    
            try:
                cell_choice= int(input("Choice a cell (0~9): "))
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):
                    


                    break
                else:
                    print("invalid move, try again")
            except ValueError:
                print("Please enter a number between 1 and 9")
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)

    def check_win(self):
        win_combinations=[[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for combo in win_combinations:
            if (self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]):
                return True
        self.indexation+=1
        self.current_player_index=self.correction[self.indexation]
        return False
    def restart_game(self):
        self.board.reset_board()
        self.current_player_index=0
        self.play_game
game=Game()
game.start_game()
