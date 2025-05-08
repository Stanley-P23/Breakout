
from blocks import *
import random


def get_blocks(game):

    sizes = []
    x_cors = []
    y_cors = []
    x_cor_init = -WIN_WIDTH / 2 + 70
    y_cor_init = WIN_HEIGHT / 2 - 340
    game.blocks = []


    aggregated = 0
    target = (WIN_WIDTH-200) / 20


    for row in range(0, 3):

        while 0 < abs(aggregated - target):
            size = random.randint(1, 10)
            print(f'aggregat: {aggregated}\tsize: {size}')

            if 6 >= target - aggregated:

                sizes.append(int(target -  aggregated))
                aggregated += target - aggregated

            elif 0 < target - aggregated - size - 1:

                sizes.append(size)
                aggregated += size + 1

            elif 0 == target - aggregated - size:

                sizes.append(size)
                aggregated += size

        game.block_sizes.append(sizes)

        sizes = []
        aggregated = 0

    for row in range(0, 3):

        for index, size in enumerate(game.block_sizes[row]):

            if index == 0:
                x_cor_init += 10 * size + 20
            else:
                x_cor_init += 10 * size + 10 * game.block_sizes[row][index-1] + 20

            x_cors.append(x_cor_init)
            y_cors.append(y_cor_init)

        game.x_cors.append(x_cors)
        game.y_cors.append(y_cors)
        x_cors = []
        y_cors = []
        y_cor_init += 90
        x_cor_init = -WIN_WIDTH / 2 + 70


    print(game.block_sizes)
    print(game.x_cors)
    print(game.x_cors)



    for row in range(game.rows):
        for block in range(0, len(game.block_sizes[row])):
            game.blocks.append(Block(row, (int(game.x_cors[row][block]), game.y_cors[row][block]), 
                                     game.block_sizes[
                row][
            block]))
            print(row, (int(game.x_cors[row][block]), game.y_cors[row][block]), game.block_sizes[row][
            block])

    game.points_to_get += len(game.blocks)
    print(f'ilosc punktow do zdobycia: {game.points_to_get}')