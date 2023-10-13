import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Drawing the image
ctx.rectangle(150, 100, 100, 240)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()
