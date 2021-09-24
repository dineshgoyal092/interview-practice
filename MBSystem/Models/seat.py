class Seat:
    id = 0
    def __init__(self, row, col_number):
        Seat.id += 1
        self.id = Seat.id
        self.row_number = row
        self.col_number = col_number