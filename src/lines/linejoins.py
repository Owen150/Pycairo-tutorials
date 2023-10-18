import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Set the line color and width
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(20)

# Miter Join
ctx.move_to(50, 100)
ctx.line_to(180, 300)
ctx.line_to(50, 300)
ctx.set_line_join(cairo.LINE_JOIN_MITER)
ctx.stroke()

# Round Join
ctx.move_to(240, 100)
ctx.line_to(370, 300)
ctx.line_to(240, 300)
ctx.set_line_join(cairo.LINE_JOIN_ROUND)
ctx.stroke()

# Bevel Join
ctx.move_to(430, 100)
ctx.line_to(560, 300)
ctx.line_to(430, 300)
ctx.set_line_join(cairo.LINE_JOIN_BEVEL)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("linejoins.png")

# Clean up
ctx.show_page()
