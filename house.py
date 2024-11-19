import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 1000)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

context.move_to(200,990)
context.line_to(20,900)
context.line_to(20,880)
context.line_to(200,970)
context.set_source_rgb(0.5,0.8,0.4)
context.fill()

context.move_to(200,970)
context.line_to(500,860)
context.line_to(500,880)
context.line_to(200,990)
context.set_source_rgb(0.5,1,0.4)
context.fill()

context.move_to(20,880)
context.line_to(200,970)
context.line_to(500,860)
context.line_to(320,780)
context.set_source_rgb(0.5,0.6,0.4)
context.fill()

surface.write_to_png("house.png")