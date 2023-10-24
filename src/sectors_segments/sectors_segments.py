import cairo
import math

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Setting the Line Width and Color
ctx.set_source_rgb(0, 0, 0.5)
ctx.set_line_width(10)

# Arc
ctx.arc(200, 200, 150, 3 * math.pi/4, 5 * math.pi/4)

# Segment
ctx.new_sub_path()
ctx.arc(350, 200, 150, 3 * math.pi/4, 5 * math.pi/4)
ctx.close_path()

# Sector
ctx.move_to(500, 200)
ctx.arc(500, 200, 150, 3 * math.pi/4, 5 * math.pi/4)
ctx.close_path()

ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("sectors_segments.png")

# Clean up code
ctx.show_page()
