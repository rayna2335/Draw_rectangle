""" Drawing Rectangle: This program uses classes and objects to allow the user to input the dimensions of the rectangle and able to move the directions of the rectangle.
Written by: Ayar Maw, Rayna Maruyama (group 9)
Date: September 19, 2022
Functions:
display_grid(grid) - Displays the contents of the grid
reset_grid(grid) - Overwrites the content of all '.'
place_rect(grid, rect) - Passes in the grid and the rectangle. Place the rectangle on the grid by overwriting '.' with '*' with the width and the height of the rectangle according to the x & y coordinate.
"""

import rectangle
import check_input

def display_grid(grid):
    """Function that displays the contents of the grid
        Args:
            grid: A 20x20 2d list containg '.' or '*'
        Returns:
            N/A
    """
    #displays the 20 x 20 grid
    for i in range(20):
        for j in range(20):
            print(grid[i][j], end=" ")
        print()


def reset_grid(grid):
    """Function that resets and overwrites the grid
        Args:
            grid: A 20x20 2d list
        Returns:
            N/A
    """
    #resets grid with '.' in each spot
    for i in range(20):
        for j in range(20):
            grid[i][j] = '.'
    

def place_rect(grid, rect):
    """Function that passes in rectangle and grid
        Args:
            grid: A 20x20 2d list
            rect: a rectangle object
        Returns:
            N/A
    """
    loct = rect.get_coords()
    loct_x = loct[0]
    loct_y = loct[1]
    width = rect.get_width()
    height = rect.get_height()

    #gets the height and width and place with '*'
    for i in range(loct_y, loct_y + height):
        for j in range(loct_x, loct_x + width):
            grid[i][j] = '*'


def main():
    # a list comprehension for creating 20x20 2d list initilized with '.'
    grid = [["." for i in range(20)] for j in range(20)]

    # prompt user to enter width and heigh of the rectangle
    rect_height = check_input.get_int_range("Enter rectangle height(1-5): ", 1, 5)
    rect_width = check_input.get_int_range("Enter rectangle width(1-5): ", 1, 5)

    # create rectangle object
    rect = rectangle.Rectangle(rect_width, rect_height)

    # 1st time creating and displaying rectangle on the grid
    place_rect(grid, rect)
    display_grid(grid)
    
    direction = 0 # control varible for main menu

    #displays menu the allows user to choose direction to move the rectangle
    while direction != 5:
        direction = check_input.get_int_range("\nEnter Direction:\
                                           \n1. Up \
                                           \n2. Down\
                                           \n3. Left\
                                           \n4. Right\
                                           \n5. Quit\n", 1, 5)

        # variables for validating rectangle's movement
        loct = rect.get_coords()
        loct_x = loct[0]
        loct_y = loct[1]
        width = rect.get_width()
        height = rect.get_height()
        move_rect = False

        #moves the rectangle upward
        if direction == 1:
            if loct_y > 0:
                rect.move_up()
                move_rect = True
        #moves the rectangle downwards
        elif direction == 2:
            if loct_y + height < 20:
                rect.move_down()
                move_rect = True
        #moves the rectangle to the left
        elif direction == 3:
            if loct_x > 0:
                rect.move_left()
                move_rect = True
        #moves the rectangle to the right
        elif direction == 4:
            if loct_x + width < 20:
                rect.move_right()
                move_rect = True
        # move the grid
        if move_rect == True:
            reset_grid(grid)
            place_rect(grid, rect)

        # display the grid
        display_grid(grid)

main()
