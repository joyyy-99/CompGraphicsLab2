import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 1000)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

surface.write_to_png("house.png")