import cairo

# Create a dictionary to store shapes with their respective vertices
shapes = {
    "rectangle": [(50, 50), (250, 50), (250, 150), (50, 150)],
    "square": [(200, 200), (300, 200), (300, 300), (200, 300)],
    "triangle": [(100, 250), (150, 350), (50, 350)]
}

# Create a new surface and context
width, height = 400, 400
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
ctx = cairo.Context(surface)

# Clear the background (optional)
ctx.set_source_rgb(1, 1, 1)  # White background
ctx.paint()

# Define colors for each shape
colors = {
    "rectangle": (1, 0, 0),  # Red
    "square": (0, 0, 1),  # Blue
    "triangle": (0, 1, 0)  # Green
}

# Draw shapes based on the provided vertices
for shape, vertices in shapes.items():
    ctx.set_source_rgb(*colors[shape])
    ctx.move_to(*vertices[0])

    for x, y in vertices[1:]:
        ctx.line_to(x, y)

    ctx.close_path()
    ctx.fill()

# Save the result as a PNG image
surface.write_to_png("polygons.png")

# Clean up
ctx.show_page()
