'''
Snake game.
Authors:
<Sheena Williams and Damilola Kazeem  >
'''

import pygame
import random
import sys

# The game grid contains this many cells in the x direction. A piece of food or a segment of the snake takes up one cell.
GRID_WIDTH = 30
# The game grid contains this many cells in the y direction. A piece of food or a segment of the snake takes up one cell.
GRID_HEIGHT = 30
# The height and width of each square cell in pixels.
PIXELS_IN_CELL = 20
# The width of the game grid in pixels.
GRID_WIDTH_PIXELS = PIXELS_IN_CELL * GRID_WIDTH
# The height of the game grid in pixels.
GRID_HEIGHT_PIXELS = PIXELS_IN_CELL * GRID_HEIGHT
# The initial length of the snake. Before eating any food, the snake contains this many segments.
INITIAL_SNAKE_LENGTH = 10

# Each of these directions contains a 2-tuple representing delta-x and delta-y for moving in that direction.
DIRECTION_LEFT = (-1, 0)
DIRECTION_RIGHT = (1, 0)
DIRECTION_UP = (0, -1)
DIRECTION_DOWN = (0, 1)

# Background color of the snake grid.
COLOR_BACKGROUND = (255, 255, 255)  # rgb color for white
# This is the color of the snake's head. 
COLOR_SNAKE_HEAD = (69, 139, 204)      # rgb color for red
# This is the color of the rest of the snake.
COLOR_SNAKE = (248, 147, 47)           # rgb color for green
# This is the color for the snake's food.
COLOR_FOOD = (255, 200, 0)          # rgb color for orange
# This is the color for the game over text.
COLOR_GAME_OVER_TEXT = (0, 0, 0)    # rgb color for black

def get_direction(previous_direction, event_key):
    """Return the new direction of the snake: one of DIRECTION_{LEFT,RIGHT,UP,DOWN}.
    previous_direction - the previous direction of the snake; one of DIRECTION_{LEFT,RIGHT,UP,DOWN} 
    event_key - the event that the user pressed; one of https://www.pygame.org/docs/ref/key.html
    If event_key does not correspond with any of the arrows keys, return previous_direction.
    """
    if event_key == pygame.K_LEFT:
        return DIRECTION_LEFT
    elif event_key == pygame.K_UP:
        return DIRECTION_UP
    elif event_key == pygame.K_RIGHT:
        return DIRECTION_RIGHT
    else:
        return DIRECTION_DOWN
    return previous_direction

def create_food_position():
    """Returns a random 2-tuple in the grid where the food should be located.
    The first element is the x position. Must be an int between 0 and GRID_WIDTH - 1, inclusively.
    The second element is the y position. Must be an int between 0 and GRID_HEIGHT - 1, inclusively.
    """
    food_x = random.randint(0, 29)
    food_y = random.randint(0, 29)
    return (food_x, food_y)

def snake_ate_food(snake, food):
    """Returns whether food was eaten by the snake.
    snake - list of 2-tuples representing the positions of each snake segment
    food - 2-tuple representing the position in the grid of the food
    This function should return True if the head of the snake is in the same position as food.
    """
    if snake[0] == food:
        return True
    return False

def snake_ran_out_of_bounds(snake):
    """Returns whether the snake has ran off one of the four edges of the grid.
    snake - list of 2-tuples representing the positions of each snake segment
    Note that the grid is GRID_WIDTH cells wide and GRID_HEIGHT cells high.
    """
    if snake[0][0] > GRID_WIDTH or snake[0][0] < 0 or snake[0][1] > GRID_HEIGHT or snake[0][1] < 0 :
        return True
    return False

def snake_intersected_body(snake):
    """Returns whether the snake has ran into itself.
    snake - list of 2-tuples representing the positions of each snake segment
    The snake ran into itself if the position of the head is the same as the position
    of any of its body segments.
    """
    for i in range (1, len(snake)):
        if snake[i] == snake[0]:
            return True
    return False

def get_score(snake):
    """Returns the current score of the game.
    snake - list of 2-tuples representing the positions of each snake segment
    The user earns 10 points for each of the segments in the snake.
    For example, if the snake has 25 segments, the score is 250.
    """
    return len(snake) * 10

def get_game_over_text(score):
    """Returns the text to draw on the screen after the game is over.
    This text should contain 'Game Over' as well as the score.
    score - integer representing the current score of the game.
    """
    return 'Game Over. ' + 'Score: 
