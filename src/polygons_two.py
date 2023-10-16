import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Closed Polygon
ctx.move_to(50, 100)    # A
ctx.line_to(200, 50)    # B
ctx.line_to(250, 300)   # C
ctx.line_to(100, 200)   # D
ctx.close_path()
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("polygons_two.png")

# Clean up
ctx.show_page()
