from canvas import Canvas
from figures import Rectangle, Square

print("\nWelcome in math painting app!\n")

print("Lets specify Canvas properties:)")
canvas_height = int(input("Canvas height (pixels): "))
canvas_width = int(input("Canvas width (pixels): "))
canvas_background = input("Canvas background (white/black): ")
canvas = Canvas(canvas_height, canvas_width, canvas_background)


print("\nLet's add some figures. Type quit to finish")

fig_numb = 1
while True:

    command = input("Choose figure rectangle / square: ")

    if command == 'rectangle':
        print("You have chosen a rectangle. Let's describe it!")
        upleft = input('Specify upleft coordinate (use backspace / x y): ').split(' ')
        upleft = list(map(int, upleft))
        RGB = input('Specify upleft coordinate (use backspace) / R G B: ').split(' ')
        RGB = list(map(int, RGB))
        height = int(input('Specify height: ' ))
        width = int(input('Specify width: ' ))
        Rectangle(upleft, RGB, height, width).draw(canvas)

        print(f'Figure {fig_numb}, type {command} has been drawn.\n')
        fig_numb += 1


    elif command == 'square':
        print("You have chosen a square. Let's describe it!")
        upleft = input('Specify upleft coordinate (use backspace / x y): ').split(' ')
        upleft = list(map(int, upleft))
        RGB = input('Specify upleft coordinate (use backspace) / R G B: ').split(' ')
        RGB = list(map(int, RGB))
        side = int(input('Specify side: ' ))
        Square(upleft, RGB, side).draw(canvas)
        print('Figure has been drawn.\n')
        
        print(f'Figure {fig_numb}, type {command} has been drawn.\n')
        fig_numb += 1


    elif 'quit' in command.lower():
        break

    else:
        print('Wrong command. Try again.')

filename = input("Choose the name for image: \n")
canvas.generate(filename)
print(f"Check the file {filename}. By!")




