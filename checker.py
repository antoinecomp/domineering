offset_x = 10      # Distance from left edge.
offset_y = 10      # Distance from top.
cell_size = 10     # Height and width of checkerboard squares.

for i in range(8):             # Note that i ranges from 0 through 7, inclusive.
    for j in range(8):           # So does j.
        if (i + j) % 2 == 0:       # The top left square is white.
            color = 'white'
        else:
            color = 'black'
        canvas.setFill(color)
        canvas.drawRect(offset_x + i * cell_size, offset_y + j * cell_size,
                        cell_size, cell_size)
