import random
import os
from colorama import Fore


class LengthError(Exception):
    pass


class Game:

    GAME_ATTEMPTS = 6
    WORD_LENGTH = 5

    def __init__(self, wordle_word) -> None:
        self.wordle_word = wordle_word
        self.underscores = ["_" for _ in range(len(wordle_word))]
        self.attempts = 1

    def check_word_length(self, word):
        if len(word) > self.WORD_LENGTH:
            raise LengthError(
                f'{space*30}Your word has more than 5 letters')
        elif len(word) < self.WORD_LENGTH:
            raise LengthError(
                f'{space*30}Your word has less than 5 letters')

    def game_over(self, status):
        if (status):
            print(f'{space*50}Congratulations you won the game ')
        else:
            print(f'{space*60} Sorry you lost {space*60}')
            print(
                f'{space*55}The corect word was {self.wordle_word.upper()}')

    def output(self, guess_word, green_letters, yellow_letters):

        output_color = []
        for i, g in enumerate(guess_word):
            pair = i, g
            # (0,a) -> [(0,a),(1,b)]
            if pair in green_letters:
                color = Fore.GREEN + " " + g + " " + Fore.RESET
                output_color.append(color)
            elif pair in yellow_letters:
                color = Fore.YELLOW + " " + g + " " + Fore.RESET

                output_color.append(color)
            else:
                color = Fore.CYAN + " _ " + Fore.RESET

                output_color.append(color)

        return "".join(output_color)

    def guess(self):

        while True:

            if (self.attempts > self.GAME_ATTEMPTS):
                self.game_over(False)
                return False

            guess = input(f'{space * 60}{self.attempts} :: ').strip()

            try:
                self.check_word_length(guess)
            except LengthError as e:
                print(f'{space*20}{e}{space*20}')
                print(f'{space*50} Try with exactly five letters ')
                continue

            self.attempts = self.attempts + 1

            # pairs of solution letter
            solution_letter = set(enumerate(self.wordle_word))
            guess_letter = set(enumerate(guess))

            # common between solution and guess
            green_letter = solution_letter & guess_letter

            solution_letter -= green_letter
            guess_letter -= green_letter

            # yellow letter-> is in guess but not on that index
            yellow_letter = set()
            for g in guess_letter:
                for solution in solution_letter:
                    if g[1] == solution[1]:
                        solution_letter.remove(solution)
                        yellow_letter.add(g)
                        break

            # grey_letter-> guess not in solution
            # grey_letters = guess_letter - yellow_letter

            output = self.output(guess, green_letter, yellow_letter)
            print(f'{space * 60}{output}\n')

            if len(green_letter) == 5:
                self.game_over(True)
                return False


def random_word_from_file():
    line = open("words.txt", "r").readlines()
    wordle = random.choice(line)
    return wordle.strip()


def start_window():
    os.system("cls" if os.name == "nt" else "clear")
    global space
    space = " "

    print(f' {space*55} Welcome to Wordle game ')
    print(f'{space*45} Try guessing the word with in six tries\n')


def exit_window():
    print(f'\n{space*50}THANK YOU FOR PLAYING THE GAME')
    input(f'{space*55}PRESS ANY KEY TO CONTINUE\n')
    os.system("cls" if os.name == "nt" else "clear")


def main():

    # select random word from a file
    word = random_word_from_file()

    # start
    start_window()

    # game initialization
    game = Game(word)
    game.guess()

    # exit
    exit_window()


if __name__ == "__main__":
    main()
