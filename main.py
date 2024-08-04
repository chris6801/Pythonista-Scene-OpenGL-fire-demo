from scene import *
import sound
import random
import math
A = Action

tile_size = 32

torches = [
    'ooooooooox',
    'ooooooooxo',
    'oooooooxoo',
    'ooooooxooo',
    'oooooxoooo',
    'ooooxooooo',
    'oooxoooooo',
    'ooxooooooo',
    'oxoooooooo',
    'oooooooooo']
    
torches.reverse()

fragment_shader_code = '''

varying highp vec2 v_tex_coord;
uniform lowp float progress;
uniform sampler2D u_texture;

void main() {
    lowp vec4 texColor = texture2D(u_texture, v_tex_coord);
    
    lowp vec4 orange = vec4(1.0, 0.5, 0.0, 1.0);
    lowp vec4 black = vec4(0.0, 0.0, 0.0, 1.0 );
    
    lowp vec4 transitionColor = mix(orange, black, progress);
    gl_FragColor = texColor *
    transitionColor;
}

'''
#gl_FragColor = mix(orange, black, progress);


class Particle(ShapeNode):
    def __init__(self, xpos, ypos, r, col, shdr):
        ShapeNode.__init__(self, ui.Path.oval(0,0,r,r),stroke_color='clear',fill_color=col,position=(xpos,ypos))
        self.x = xpos
        self.y = ypos
        self.dx = random.uniform(-.2,.2)
        self.dy = random.uniform(1,2)
        self.c = col
        self.cidx = 0
        self.cols = ['#ffece5','#ffdfb5','#ffce8c', '#ffbc63','#ffae42','#ff6021','#ff0000','#7d0000']
        self.a = math.atan2(self.dy, self.dx)
        self.t = 0
        self.r = r
        self.l = 60
        self.progress = 0.0
        self.increment = 0.05
        self.shader = shdr
    def update(self):
        #self.a = math.atan2(self.dy, self.dx)
        #self.dx = math.cos(self.a+(self.t*.05))
        self.scale *= 1 - (self.t*.005)
        
        self.position += self.dx, self.dy
        
        self.t +=1
        
        if self.a % math.pi == 0:
            self.t = 0
        
        if self.l < 0 or self.scale < .1:
            self.remove_from_parent()
            
        self.l -= 1
     
        
        self.c = self.cols[self.cidx]
        
        if self.t % 3 == 0 and self.cidx < len(self.cols) - 1:
            self.cidx += 1
        
        
        self.progress += self.increment
        if self.progress >= 1.0:
            self.increment = 0

        self.shader.set_uniform('progress', self.progress)
        #print(f"Progress: {self.progress}")
        
    
    def draw(self):
        pass
        #self.fill_color = (self.c)
        #self.stroke_color = self.c
        #canvas.set_stroke_color(255,0,0)
        #canvas.fill_pixel(self.x,self.y)
        #canvas.fill_ellipse(self.x,self.y,self.r,self.r)
        
def make_parts(particles,x,y,s):
    
    for i in range(1):
        p = Particle(x,y,25,(.9,.9,0),s)
        fade = A.fade_to(0)
        #change_c = A.set_uniform()
        
        #p.run_action(fade)
        particles.add_child(p)
        #print(p.a)

class MyScene (Scene):
    def setup(self):
        #self.s = Shader(fragment_shader_code)
        self.shdr = fragment_shader_code
        self.particles = Node(parent=self)
        
        self.progress = 0.0
        self.increment = 0.01
        
        self.logs = Node(parent=self)
        self.background_color = 'cyan'
        #self.log.shader=self.s
        self.t_list = []
        for i, line in enumerate(torches):
            for j, char in enumerate(line):
                if char == 'x':
                    l = SpriteNode('plf:Tile_TorchOff',position=(j*tile_size,i*tile_size-20),parent=self.logs)
                    
                    self.t_list.append((j*tile_size,i*tile_size ))
    
    def did_change_size(self):
        pass
    
    def update(self):
        #print(f"Progress: {self.progress}")
        
        for torch in self.t_list:
            make_parts(self.particles,torch[0],torch[1],Shader(fragment_shader_code))
            make_parts(self.particles,torch[0], torch[1]+100,Shader(fragment_shader_code))
            make_parts(self.particles,torch[0], torch[1]+200,Shader(fragment_shader_code))
            #make_parts(self.particles,torch[0], torch[1]+300,Shader(fragment_shader_code))
        
        for p in self.particles.children:
            p.update()
            p.draw()
            
        print(len(self.particles.children))
    
    def touch_began(self, touch):
        pass
    
    def touch_moved(self, touch):
        pass
    
    def touch_ended(self, touch):
        pass

if __name__ == '__main__':
    run(MyScene(), show_fps=True, frame_interval=1)