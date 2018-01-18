from psychopy import visual, event
import ratcave as rc

camera_speed = 2

# Create Window and Add Keyboard State Handler to it's Event Loop
window = visual.Window()

# Insert filename into WavefrontReader.
obj_filename = rc.resources.obj_primitives
obj_reader = rc.WavefrontReader(obj_filename)

# Create Mesh
monkey = obj_reader.get_mesh("Monkey", position=(0, 0, -1.5), scale=.6)
torus = obj_reader.get_mesh("Torus", position=(-1, 0, -1.5), scale=.4)

# Create Scene
scene = rc.Scene(meshes=[monkey, torus])
scene.bgColor = 1, 0, 0

while True:

    dt = .016

    keys_pressed = event.getKeys()
    if 'escape' in keys_pressed:
        window.close()
        break

    # Move Camera
    for key in keys_pressed:
        if key == 'left':
            scene.camera.x -= camera_speed * dt
        elif key == 'right':
            scene.camera.x += camera_speed * dt

    # Rotate Meshes
    monkey.rotation.y += 15 * dt  # dt is the time between frames
    torus.rotation.x += 80 * dt

    # Draw Scene and Flip to Window
    scene.draw()
    window.flip()