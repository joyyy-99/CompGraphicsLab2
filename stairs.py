import cairo

# Image dimensions
WIDTH, HEIGHT = 400, 400

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Background
context.set_source_rgb(1, 1, 1)  # White background
context.paint()

# Dimensions for the cuboids
cuboid_width = 150
cuboid_height = 50
cuboid_depth = 30
base_x = 200
base_y = 300

# Draw the bottom step (cuboid)
# Front face
context.set_source_rgb(0.7, 0.7, 0.7)  # Medium grey
context.rectangle(base_x, base_y - cuboid_height, cuboid_width, cuboid_height)
context.fill()

# Top face
context.set_source_rgb(0.9, 0.9, 0.9)  # Light grey
context.move_to(base_x, base_y - cuboid_height)
context.line_to(base_x - cuboid_depth, base_y - cuboid_height - cuboid_depth)
context.line_to(base_x - cuboid_depth + cuboid_width, base_y - cuboid_height - cuboid_depth)
context.line_to(base_x + cuboid_width, base_y - cuboid_height)
context.close_path()
context.fill()

# Side face
context.set_source_rgb(0.6, 0.6, 0.6)  # Dark grey
context.move_to(base_x, base_y - cuboid_height)
context.line_to(base_x - cuboid_depth, base_y - cuboid_height - cuboid_depth)
context.line_to(base_x - cuboid_depth, base_y - cuboid_depth)
context.line_to(base_x, base_y)
context.close_path()
context.fill()

# Draw the top step (cuboid)
# Front face
context.set_source_rgb(0.7, 0.7, 0.7)  # Medium grey
context.rectangle(base_x - cuboid_depth, base_y - cuboid_height * 2 - cuboid_depth, cuboid_width, cuboid_height)
context.fill()

# Top face
context.set_source_rgb(0.9, 0.9, 0.9)  # Light grey
context.move_to(base_x - cuboid_depth, base_y - cuboid_height * 2 - cuboid_depth)
context.line_to(base_x - cuboid_depth * 2, base_y - cuboid_height * 2 - cuboid_depth * 2)
context.line_to(base_x - cuboid_depth * 2 + cuboid_width, base_y - cuboid_height * 2 - cuboid_depth * 2)
context.line_to(base_x - cuboid_depth + cuboid_width, base_y - cuboid_height * 2 - cuboid_depth)
context.close_path()
context.fill()

# Side face
context.set_source_rgb(0.6, 0.6, 0.6)  # Dark grey
context.move_to(base_x - cuboid_depth, base_y - cuboid_height * 2 - cuboid_depth)
context.line_to(base_x - cuboid_depth * 2, base_y - cuboid_height * 2 - cuboid_depth * 2)
context.line_to(base_x - cuboid_depth * 2, base_y - cuboid_depth * 2 - cuboid_height)
context.line_to(base_x - cuboid_depth, base_y - cuboid_depth - cuboid_height)
context.close_path()
context.fill()

# Save the image
surface.write_to_png("stairs.png")
