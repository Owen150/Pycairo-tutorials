import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0, 0, 0)
ctx.paint()


def draw_ace_of_diamonds(ctx, width, height):
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

    # Draw the "A" symbol in the middle of the diamond
    ctx.set_source_rgb(0, 0, 0)  # Set the color to black
    ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(40)
    ctx.move_to(width / 2 - 20, height / 2 + 15)  # Adjust the position for centering
    ctx.show_text("A")

    surface.write_to_png("ace_of_diamonds.png")
    surface.finish()


# Adjust the dimensions as needed
draw_ace_of_diamonds(ctx, 300, 450)

ctx.show_page()
