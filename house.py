import cairo

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 600, 1000)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

#Green Base
context.move_to(250,990)
context.line_to(20,870)
context.line_to(20,850)
context.line_to(250,970)
context.set_source_rgb(0.5,0.8,0.4)
context.fill()

context.move_to(250,970)
context.line_to(550,860)
context.line_to(550,880)
context.line_to(250,990)
context.set_source_rgb(0.5,1,0.4)
context.fill()

context.move_to(20,850)
context.line_to(250,970)
context.line_to(550,860)
context.line_to(320,780)
context.set_source_rgb(0.686, 0.816, 0.408)
context.fill()

#Grey House Base
context.move_to(130, 860)
context.line_to(130,840)
context.line_to(260,910)
context.line_to(450,840)
context.line_to(450,860)
context.line_to(260,930)
context.set_source_rgb(0.66,0.66,0.66)
context.fill()

#House
context.move_to(130,840)
context.line_to(130,550)
context.line_to(200,510)
context.line_to(260,610)
context.line_to(260,910)
context.set_source_rgb(0.8,0.8,0.8)
context.fill()

context.move_to(260,910)
context.line_to(260,630)
context.line_to(450,560)
context.line_to(450,840)
context.set_source_rgb(0.7,0.7,0.7)
context.fill()

context.move_to(260,630)
context.line_to(260,610)
context.line_to(450,540)
context.line_to(450,560)
context.set_source_rgb(0.66,0.66,0.66)
context.fill()

#Roof(Left Part)
context.move_to(200,530)
context.line_to(90,560)
context.line_to(320,460)
context.line_to(400,450)
context.set_source_rgb(0.231, 0.282, 0.341)
context.fill()

#Roof(Right Part)
context.move_to(250,620)
context.line_to(200,530)
context.line_to(400,450)
context.line_to(470,540)
context.set_source_rgb(0.231, 0.282, 0.341)
context.fill()

# Stairs Code
# Adjust these values to align the stairs with the house door
base_x = 380  # Aligned with the center of the door
base_y = 910  # Just below the base of the house

cuboid_width = 80  # Adjusted to fit house proportions
cuboid_height = 10
cuboid_depth = 10

# Draw the bottom step
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

# Draw the top step
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

surface.write_to_png("house.png")