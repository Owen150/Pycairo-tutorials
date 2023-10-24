import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


# Defining the arrow function
def arrow(ctx, x, y, width, height, a, b):
    ctx.move_to(x, y + b)
    ctx.line_to(x, y + height - b)
    ctx.line_to(x + a, y + height - b)
    ctx.line_to(x + a, y + height)
    ctx.line_to(x + width, y + height/2)
    ctx.line_to(x + a, y)
    ctx.line_to(x + a, y + b)
    ctx.close_path()


# Drawing different arrows
ctx.set_source_rgb(0, 0, 0.5)
arrow(ctx, 20, 20, 150, 150, 75, 50)
ctx.fill()

arrow(ctx, 220, 20, 150, 150, 50, 30)
ctx.fill()

arrow(ctx, 420, 20, 150, 150, 25, 20)
ctx.fill()

arrow(ctx, 70, 220, 75, 150, 0, 50)
ctx.fill()

arrow(ctx, 220, 220, 150, 150, 75, 0)
ctx.fill()

arrow(ctx, 420, 270, 150, 50, 100, 0)
ctx.fill()

# Save the result as a PNG image
surface.write_to_png("arrows.png")

# Clean up
ctx.show_page()
