import cairo
import math

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)

# Relative Drawing function
a = 0.523599
r = 200
ctx.move_to(300, 200)
ctx.rel_line_to(r*math.cos(a), r*math.sin(a))
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("lineangles.png")

# Clean up
ctx.show_page()
