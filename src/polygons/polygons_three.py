import cairo

# Setting up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


# Save the result as a PNG image
surface.write_to_png("polygons_three.png")

# Clean up
ctx.show_page()
