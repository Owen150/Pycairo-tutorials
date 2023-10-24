import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Red Rectangle - fill
ctx.rectangle(100, 50, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

# Green Rectangle - stroke
ctx.rectangle(250, 50, 100, 240)
ctx.set_source_rgb(0, 1, 0)
ctx.set_line_width(5)
ctx.stroke()

# Blue Square - fill & stroke
ctx.rectangle(400, 50, 100, 100)
ctx.set_source_rgb(0, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0)
ctx.set_line_width(10)
ctx.stroke()

# Save the result as a PNG image
surface.write_to_png("fill_stroke.png")

# Clean up
ctx.show_page()
