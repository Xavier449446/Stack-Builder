import pymunk
from pyglet.window import Window,mouse,key
import pyglet
from Boxes import Box,Base
from pymunk.pyglet_util import DrawOptions
import sys

size=25

class MainWindow(Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.space=pymunk.Space()
        self.set_caption("Bouncy Stack")
        self.space.gravity=0,-500
        self.add=False
        self.draw_options=DrawOptions()
        self.ground=Base(self.space)
        self.ground.draw()
        self.game_complete=False
        self.counter=0
        self.comp_lbl=pyglet.text.Label(text="Game Completed",font_size=40,bold=True,italic=True,color=(100,100,100,100),x=400,y=400,anchor_x='center',anchor_y='center')


    def all_remove(self):
        rem_shapes=list(filter(lambda x: (x.body.body_type==pymunk.Body.DYNAMIC),self.space.shapes))
        rem_bodies=list(filter(lambda x: (x.body_type==pymunk.Body.DYNAMIC),self.space.bodies))
        self.space.remove(rem_shapes,rem_bodies)
    
    
    def on_key_press(self,symbol,modifiers):
        if symbol==key.R:
            self.all_remove()
            self.game_complete=False

    def game_timer(self,dt):
        if self.game_complete:
            self.comp_lbl.draw()
            self.counter+=1
            if self.counter>=3:
                self.close()
                sys.exit()


    
    def on_mouse_press(self,x,y,button,modifiers):
        global size
        if button==mouse.LEFT:
            Box(verts=((x-size,y-size),(x+size,y-size),(x+size,y+size),(x-size,y+size)),space=self.space).draw()
    
    
    def on_mouse_drag(self,x,y,dx,dy,button,modifiers):
        global size
        if button==mouse.LEFT:
            if x%3==0 and y%3==0:
                Box(verts=((x-size,y-size),(x+size,y-size),(x+size,y+size),(x-size,y+size)),space=self.space).draw()
    
    def game_end_check(self):
        for shape in self.space.shapes:
            if isinstance(shape,pymunk.Segment):
                pass
            else:
                for x,y in shape.get_vertices():
                    if y > 850:
                        self.game_complete=True
    
    def on_draw(self):
        if self.game_complete:
            self.comp_lbl.draw()
        self.space.debug_draw(self.draw_options)
    
    
    def update(self,dt):
        self.clear()
        self.game_end_check()
        self.space.step(dt)
        print(self.space.bodies)
        

if __name__=="__main__":
    win=MainWindow(800,800)
    pyglet.clock.schedule_interval(win.update,1/60)
    pyglet.clock.schedule_interval(win.game_timer,1.0)
    pyglet.app.run()
