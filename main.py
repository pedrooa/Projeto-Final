#Head Soccer Game - Vitor, Gabriel, Pedro e Manzanna
import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('head.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)

pyglet.app.run()
