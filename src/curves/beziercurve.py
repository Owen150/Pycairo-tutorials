import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Bezier Curve
ctx.move_to(100, 100)
ctx.curve_to(200, 0, 400, 200, 500, 100)
ctx.line_to(500, 300)
ctx.curve_to(400, 400, 200, 200, 100, 300)
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("polycurve.png")

# Clean up
ctx.show_page()
