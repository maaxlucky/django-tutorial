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

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[:-3:-1])
