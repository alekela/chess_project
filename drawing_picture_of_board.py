from PIL import Image, ImageDraw


def drawing_picture(cell_size):
    picture = Image.new('RGB', (cell_size * 8, cell_size * 8))
    draw = ImageDraw.Draw(picture)
    white = '#F0d9b5'
    black = '#b58863'
    color = white
    for width in range(8):
        for height in range(8):
            draw.rectangle(
                ((cell_size * width, cell_size * height),
                 (cell_size * (width + 1), cell_size * (height + 1))),
                color
            )
            color = white if color == black else black
        color = white if color == black else black
    draw.line(((0, 0), (cell_size * 8 - 1, 0),
               (cell_size * 8 - 1, cell_size * 8 - 1), (0, cell_size * 8 - 1), (0, 0)),
              '#000000', width=4)
    picture.save('board.png')


drawing_picture(50)
