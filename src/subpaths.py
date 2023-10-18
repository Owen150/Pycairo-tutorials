import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Sub-path 1
ctx.move_to(50, 50)
ctx.line_to(400, 200)
ctx.line_to(50, 350)
ctx.close_path()

# Sub-path 2
ctx.move_to(450, 100)
ctx.line_to(550, 100)
ctx.line_to(450, 300)

# Sub-path 3
ctx.move_to(100, 100)
ctx.line_to(200, 200)
ctx.line_to(100, 300)
ctx.close_path()

# Set path color and width
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("subpaths.png")

# Clean up
ctx.show_page()
