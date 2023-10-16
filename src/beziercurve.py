import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Bezier Curve
ctx.move_to(100, 200)
ctx.curve_to(200, 100, 400, 300, 500, 200)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("bezier.png")

# Clean up
ctx.show_page()
