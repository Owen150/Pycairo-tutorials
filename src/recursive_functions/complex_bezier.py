import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 1000, 200)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()


def draw(n: int):
    """This function takes a variable n of type int and recursively draws a complex
    shape out of it. This shape is created using cubic bezier curves
    """
    ctx.move_to(100, 30)
    ctx.line_to(100, 100)
    end = 100
    for x in range(n):
        m = 100 * x
        ctx.curve_to(m + 250, 50, m + 50, 50, m + 200, 100)
        end = m + 200
    ctx.line_to(end, 30)

    ctx.close_path()
    ctx.set_source_rgb(1, 1, 1)
    ctx.fill_preserve()
    ctx.set_source_rgb(1, 0, 0)
    ctx.set_line_width(5)
    ctx.stroke()


draw(4)
surface.write_to_png("recursive_shapes.png")
