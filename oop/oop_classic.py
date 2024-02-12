# chess game in 11 lines
# import chess
#
# board = chess.Board()
# while True:
#     print(board)
#     legal_moves = [x.uci() for x in list(board.legal_moves)]
#     move = input(f">> Legal moves: {legal_moves}")
#     if move in legal_moves:
#         board.push_uci(move)
#     else:
#         print(f"'{move}' is not a legal move, Please enter another one!")

# clarify Simple class presentation
class Dog:
    # class attribute
    attr1 = 'mammal'

    # Instance attribute
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('My name is {}'.format(self.name))


# Driver code
# Object instantiation
Rodger = Dog('Rodger')
Tommy = Dog('Tommy')

# Accessing class attributes
# print('Rodger is a {}'.format(Rodger.__class__.attr1))
# print("Tommy is a {}".format(Tommy.__class__.attr1))
#
# # Accessing instance attributes
# print('My name is {}'.format(Rodger.name))
# print('My name is {}'.format(Tommy.name))

# Acessing class methods
Rodger.speak()
Tommy.speak()

