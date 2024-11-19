import cairo

# Image dimensions
WIDTH, HEIGHT = 400, 400

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Coordinates for the cuboid
# Front face
front_top_left = (150, 150)
front_top_right = (200, 150)
front_bottom_left = (150, 250)
front_bottom_right = (200, 250)

# Back face (shifted diagonally)
back_top_left = (180, 120)
back_top_right = (230, 120)
back_bottom_left = (180, 220)
back_bottom_right = (230, 220)

# Draw the front face
context.set_source_rgb(0.8, 0.8, 0.8)  # Light grey
context.move_to(front_top_left[0], front_top_left[1])
context.line_to(front_bottom_left[0], front_bottom_left[1])
context.line_to(front_bottom_right[0], front_bottom_right[1])
context.line_to(front_top_right[0], front_top_right[1])
context.close_path()
context.fill()

# Draw the side face
context.set_source_rgb(0.6, 0.6, 0.6)  # Medium grey
context.move_to(front_top_right[0], front_top_right[1])
context.line_to(back_top_right[0], back_top_right[1])
context.line_to(back_bottom_right[0], back_bottom_right[1])
context.line_to(front_bottom_right[0], front_bottom_right[1])
context.close_path()
context.fill()

# Draw the top face
context.set_source_rgb(0.9, 0.9, 0.9)  # Lighter grey
context.move_to(front_top_left[0], front_top_left[1])
context.line_to(back_top_left[0], back_top_left[1])
context.line_to(back_top_right[0], back_top_right[1])
context.line_to(front_top_right[0], front_top_right[1])
context.close_path()
context.fill()

# Save the image
surface.write_to_png("chimney.png")
