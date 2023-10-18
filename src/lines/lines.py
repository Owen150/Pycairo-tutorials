import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw a red line
ctx.move_to(100, 100)
ctx.line_to(500, 300)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("lines.png")

# Clean up
ctx.show_page()
