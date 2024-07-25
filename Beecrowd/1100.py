#Movimentos do Cavalo

def knight_moves(start, end):
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]

    start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
    end_x, end_y = ord(end[0]) - ord('a'), int(end[1]) - 1

    min_moves = [[float('inf')] * 8 for _ in range(8)]
    min_moves[start_x][start_y] = 0

    queue = [(start_x, start_y)]
    while queue:
        x, y = queue.pop(0)
        if x == end_x and y == end_y:
            return min_moves[x][y]
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if min_moves[new_x][new_y] == float('inf'):
                    min_moves[new_x][new_y] = min_moves[x][y] + 1
                    queue.append((new_x, new_y))

def format_output(start, end, moves):
    if moves == 1:
        return "To get from {} to {} takes 1 knight moves.".format(start, end)
    else:
        return "To get from {} to {} takes {} knight moves.".format(start, end, moves)

def main():
    while True:
        try:
            start, end = input().split()
            moves = knight_moves(start, end)
            print(format_output(start, end, moves))
        except EOFError:
            break

if __name__ == "__main__":
    main()
