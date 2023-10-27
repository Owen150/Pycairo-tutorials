import cairo


def draw_ace_of_diamonds_with_diamonds(filename, width, height):
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    # Set the background color (white)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, width, height)
    ctx.fill()

    # Draw the diamond shape
    ctx.set_source_rgb(1, 0, 0)  # Set the color to red
    ctx.move_to(width / 2, 20)
    ctx.line_to(width - 20, height / 2)
    ctx.line_to(width / 2, height - 20)
    ctx.line_to(20, height / 2)
    ctx.close_path()
    ctx.fill()

    # Draw a diamond symbol in each card corner
    ctx.set_source_rgb(0, 0, 0)  # Set the color to black

    diamond_side = 20  # Size of the corner diamonds
    diamond_positions = [
        (20, 20),
        (width - 20 - diamond_side, 20),
        (width - 20 - diamond_side, height - 20 - diamond_side),
        (20, height - 20 - diamond_side)
    ]

    for x, y in diamond_positions:
        ctx.move_to(x + diamond_side / 2, y)
        ctx.line_to(x, y + diamond_side / 2)
        ctx.line_to(x + diamond_side / 2, y + diamond_side)
        ctx.line_to(x + diamond_side, y + diamond_side / 2)
        ctx.close_path()
        ctx.fill()

    surface.write_to_png(filename)


if __name__ == "__main__":
    width, height = 300, 450  # Adjust the dimensions as needed
    draw_ace_of_diamonds_with_diamonds("ace_of_diamonds_with_diamonds.png", width, height)
