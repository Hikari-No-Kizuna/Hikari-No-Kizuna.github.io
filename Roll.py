import random

def getInt(s):
    length = len(s)
    return random.randint(1,length + length * length * length)

def main():
    make = []
    make.append("name generator")
    make.append("HiLo Game")
    make.append("name generator")
    make.append("age calculator")
    make.append("encryption/decryption algorithm")
    make.append("an innovative fizzbuzz program")
    make.append("rock paper scissors AI - Bonus if you can use Markov Chains")
    make.append("hangman game")
    make.append("love calculator")
    make.append("psuedorandom sentence generator")
    make.append("password generator")
    make.append("clock that utilizes atomically correct time from an internet clock")
    make.append("haiku generator")
    make.append("string reverser")
    make.append("Minesweeper game")
    make.append("Connect Four game")
    make.append("BMI calculator")
    make.append("4chan image thread downloader - Bonus if you use the API")
    make.append("Sudoku generator and solver - Bonus for not dying in the process")
    make.append("maze generator and solver - Bonus for using either BFS, DFS, and A*")
    make.append("decimal to binary converter")
    make.append("picross solver")
    make.append("program that can calculate and print out 100 factorial")
    make.append("cipher encrpter and decrypter")
    make.append("blackjack simulator")
    make.append("Dungeons & Dragons game that uses an AI")
    make.append("program that generates and ASCII tree with height based on input")
    make.append("currency converter")
    make.append("website generator")
    make.append("crossword game")
    make.append("scientific calculator")
    make.append("image viewer - Bonus for supporting a shitton of formats")
    make.append("ASCII digital clock")
    make.append("text to morse code translator")
    make.append("tic-tac-toe game")
    make.append("snake game")
    make.append("FTP client")
    make.append("Telnet Server")
    make.append("IMP interpreter")
    make.append("Tetris game")
    make.append("")
    make.append("image viewer - Bonus for supporting a shitton of formats")
    make.append("ASCII digital clock")
    make.append("text to morse code translator - Bonus for using sound as the output")
    make.append("tic-tac-toe game")
    make.append("snake game")
    make.append("FTP client")
    make.append("Telnet Server")
    make.append("IMP interpreter")
    make.append("web crawler")
    make.append("text editor")
    make.append("RSS feed creator")
    make.append("RPN calculator")
    make.append("markup to HTML converter")
    make.append("credential validator e.g. Phone#, email address")
    make.append("Mastermind game")
    make.append("random image generator")
    make.append("Klingon translator")
    make.append("graphical analog clock and GUI")
    make.append("program that sends strings between two separate langauges e.g. C++ & Java, Python & LISP")
    make.append("triangle number calculator")
    make.append("name art ASCII generator")
    make.append("Tower of Hanoi solver")
    make.append("IRC bot")
    make.append("brainfuck interpreter")
    make.append("sorting algorithm visualization - Bonus for adding in sound")
    make.append("Chip-8 emulator")
    make.append("Geekcode generator")
    make.append("program that can define, translate, and rotate a polygon")
    make.append("pong game with variable vectors")
    make.append("battleships game with an AI")
    make.append("simple paint program")
    make.append("TCP based chat program that utilizes basic XOR encryption")
    make.append("economy simulator")
    make.append("text to image encrypter/decrypter")
    make.append("sine wave generator based on pseudorandom numbers")
    make.append("HTML web browser")
    make.append("Flappy Bird copypasta")
    make.append("vector dot and cross calculator")
    make.append("little man computer simulator")
    make.append("Basic LISP interpreter")
    make.append("Enigma machine simulator with settings.conf - Bonus for decryption without knowing rotor settings")
    learn = []
    learn.append("the Collatz Conjecture")
    learn.append("Eulerian paths")
    learn.append("fibonacci sequences - Bonus for making a generator that can utilize both memoization and tabling")
    learn.append("genetic algorithms ")
    learn.append("Benford's law")
    learn.append("the Perlin Noise algorithm")
    learn.append("Djikstra's algorithm - Bonus for learning both the N^2 and NlogN variants")
    learn.append("Conway's Game of Life")
    learn.append("the evalulation of binomial coefficients")
    learn.append("the Mandlebrot Set")
    learn.append("sorting algorithms - Bonus for learning about the cool ones like Bogo and Sleep sort")
    learn.append("the N-Queens problem")
    learn.append("linked lists")
    learn.append("Ulam Spiral - Bonus for creating a visualization")
    learn.append("a prime number sieve")
    learn.append("Markov Chains")
    learn.append("Quines")
    learn.append("Pascal's Triangle")
    learn.append("the Sierpinski triangle generator")
    print "So you're bored and need a programming project to do?"
    print "Well thankfully, tripfags !LiNuXCQGns and !Hikari1cFu are here to help"
    print "Just type in roll, rollarino, roller coaster, or whatever the fuck you want and you'll be given a brand new project to work on"
    kek = getInt(str(raw_input()))
    random.seed(kek)
    totallen = len(make) + len(learn)
    ind = random.randint(0,totallen-1)
    ans = ''
    if ind > len(make)-1:
        print "Learn about and implement " + learn[ind - len(make)]
    else:
        print "Make a " + make[ind]
    print "\nThere's your new project anon. You better do it, since you've clearly got the time to run this shitty program "
if __name__ == '__main__':
    main()
