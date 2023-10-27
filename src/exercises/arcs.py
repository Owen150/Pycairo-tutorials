import cairo
import math

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0, 0, 0)
ctx.paint()

# Draw the Arcs
ctx.arc(300, 200, 100, 5 * math.pi/4, 7 * math.pi/4)
ctx.set_source_rgb(1, 0, 0)
ctx.set_line_width(5)
ctx.stroke()

surface.write_to_png("arcs_exercise.png")

ctx.show_page()
