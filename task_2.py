import sys
import turtle


def draw_koch_curve(pen, size, rec_level):
    if rec_level == 0:
        pen.forward(size)
        return

    for angle in [60, -120, 60, 0]:
        draw_koch_curve(pen, size / 3, rec_level - 1)
        pen.left(angle)


def draw_koch_snowflake(rec_level, size = 600):
    if rec_level < 0:
        raise ValueError("The recursion level must be zero or greater.")

    window = turtle.Screen()
    window.setup(width=size + 200, height=size + 200)
    window.title(f"Koch snowflake, recursion level {rec_level}")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.goto(-size / 2, size / 4)
    pen.pendown()

    for _ in range(3):
        draw_koch_curve(pen, size, rec_level)
        pen.right(120)

    pen.hideturtle()
    window.mainloop()

def main():
    args = sys.argv[1:]
    if not args:
        rec_level = 3
    else:
        rec_level = int(args[0])

    draw_koch_snowflake(rec_level)


if __name__ == "__main__":
    main()