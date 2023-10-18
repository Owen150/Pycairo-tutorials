import cairo
import math

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw a complete circle
ctx.arc(300, 300, 100, 0, 2 * math.pi)
ctx.set_source_rgb(0, 0, 0)
ctx.fill_preserve()
ctx.set_line_width(10)
ctx.stroke()

# Draw an Arc
ctx.arc(300, 300, 100, 0, math.pi/2)
ctx.set_source_rgb(0, 1, 0)
ctx.line_to(300, 300)
ctx.close_path()
ctx.stroke()

# Draw an arc that is 3/4 black and 1/4 green
# ctx.arc(300, 300, 100, -math.pi / 2, math.pi / 2)  # 3/4 black
# ctx.set_source_rgb(0, 0, 0)
# ctx.line_to(300, 300)  # Create a line back to the center
# ctx.close_path()
# ctx.fill()

# Draw a line to separate the green part
ctx.move_to(300, 300)
ctx.line_to(400, 300)

ctx.move_to(200, 300)
ctx.line_to(300, 300)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)

ctx.move_to(300, 200)
ctx.line_to(300, 300)
ctx.set_line_cap(cairo.LINE_CAP_SQUARE)

ctx.set_source_rgb(0, 1, 0)
ctx.stroke()

# Save the image to a file
surface.write_to_png("circle.png")

