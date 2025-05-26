from graphics import Canvas

def main():
    # Create an object type Canvas
    canvas = Canvas(400, 400)
    
    # draw the first car at coordinates (10, 10)
    x = 10
    y = 10
    draw_car(canvas, x, y)  # you should add canvas, and coordinates to the parameters inside the function

    # draw the second car at coordinates (100, 100)
    x = 100
    y = 100
    draw_car(canvas, x, y)  # same parameters within the function

def draw_car(canvas, x, y):  # Add the parameters that this function is going to receive
    # It will draw a car at the location x, y
    #Offsets to where to draw the cars are given by the program
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
