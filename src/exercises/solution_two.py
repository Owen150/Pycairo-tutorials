import cairo
import math

WIDTH, HEIGHT = 800, 800


def arcs(width: int, height: int) -> None:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)
    context.set_source_rgb(0.8, 0.8, 0.8)
    context.paint()

    context.rectangle(200, 200, 400, 400)
    context.set_source_rgb(0, 0, 0)
    context.fill()

    context.set_source_rgb(1, 0, 0)
    context.arc(200, 400, 200, (3 * math.pi / 2), (math.pi / 2))
    context.stroke()

    context.set_source_rgb(1, 0, 0)
    context.arc(400, 200, 200, 0, math.pi)
    context.stroke()

    context.set_source_rgb(0, 0, 1)
    context.arc(600, 400, 200, (math.pi / 2), (3 * math.pi / 2))
    context.stroke()

    context.set_source_rgb(0, 0, 1)
    context.arc(400, 600, 200, math.pi, 0)
    context.stroke()

    surface.write_to_png("curve.png")


if __name__ == '__main__':
    arcs(WIDTH, HEIGHT)
