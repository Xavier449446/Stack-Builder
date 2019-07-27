import pymunk
import pyglet

class Box:
    def __init__(self,verts,space):
        self.mass=100
        self.space=space
        self.vertices=verts
        self.moment=pymunk.moment_for_poly(self.mass,vertices=self.vertices)
        self.body=pymunk.Body(self.mass,self.moment,pymunk.Body.STATIC)
        self.shape=pymunk.Poly(self.body,self.vertices)
        self.shape.friction=0.15
        self.shape.density=100
        self.shape.elasticity=0.7
        self.addes=[self.body,self.shape]
    def draw(self):
        self.space.add(self.addes)

class Base(Box):
    def __init__(self,space):
        self.mass=0
        self.space=space
        self.vertices=((0,50),(800,50))
        self.moment=pymunk.moment_for_segment(self.mass,*self.vertices,3)
        self.body=pymunk.Body(self.mass,self.moment,pymunk.Body.STATIC)
        self.shape=(pymunk.Segment(self.body,*self.vertices,3))
        self.shape.density=10000000
        self.shape.friction=1
        self.shape.elasticity=0.7
        self.addes=[self.body,self.shape]
