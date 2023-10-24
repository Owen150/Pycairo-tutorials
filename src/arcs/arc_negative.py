import cairo
import math

# Setting up the Surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Set Line Color and Width
ctx.set_source_rgb(0, 0, 0.5)
ctx.set_line_width(10)

# Arc
ctx.arc(150, 200, 100, 3 * math.pi/4, 5 * math.pi/4)
ctx.stroke()

# Arc Negative
ctx.arc_negative(400, 200, 100, 3 * math.pi/4, 5 * math.pi/4)
ctx.stroke()

surface.write_to_png("arc_negative.png")

ctx.show_page()
