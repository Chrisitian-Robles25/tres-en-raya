def check_winner(board):
    # Combinaciones ganadoras
    winning_combinations = [
        [0, 1, 2],  # Fila 1
        [3, 4, 5],  # Fila 2
        [6, 7, 8],  # Fila 3
        [0, 3, 6],  # Columna 1
        [1, 4, 7],  # Columna 2
        [2, 5, 8],  # Columna 3
        [0, 4, 8],  # Diagonal 1
        [2, 4, 6],  # Diagonal 2
    ]

    # Verificar combinaciones ganadoras
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]  # Retorna el ganador ('X' o 'O')

    # Verificar empate
    if all(cell != "" for cell in board):
        return "Empate"

    return None  # Juego en curso