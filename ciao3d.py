class Vect3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

class Pixel:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

class Line:
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2

class World:
    def __init__(self, world, canvas) -> None:
        self.world = world
        self.canvas = canvas        
        self.screenw = 1920
        self.screenh = 1080

    def render(self,offx):
        for line in self.world:
            #self.canvas.create_line(line.v1.x+offx,line.v1.y,line.v2.x+offx,line.v2.y, fill="black", width=2)
            vv1 = Vect3(line.v1.x - offx * 5, line.v1.y + offx * 0.5, line.v1.z)
            vv2 = Vect3(line.v2.x - offx * 5, line.v2.y + offx * 0.5, line.v2.z)
            self.canvas.create_line(projectPoint(vv1).x,projectPoint(vv1).y,projectPoint(vv2).x,projectPoint(vv2).y, fill="black", width=2)
            pass

def projectPoint(pp, ox = 0, oy = 50, oz = 50):
    dist = 10
    screenw = 1920
    screenh = 1080
    zoom = 50
    p = Pixel()
    deltax = (pp.y - oy) * dist / (pp.x - ox) * zoom
    deltay = (pp.z - oz) * dist / (pp.x - ox) * zoom
    p.x=screenw/2+deltax
    p.y=screenh/2-deltay
    print (p.x, p.y)
    return p

def spawnCube(list,x,y,z,side):
    v1 = Vect3(x,y,z)
    v2 = Vect3(x,y+side,z)
    v3 = Vect3(x,y+side,z+side)
    v4 = Vect3(x,y,z+side)
    v5 = Vect3(x+side,y,z)
    v6 = Vect3(x+side,y+side,z)
    v7 = Vect3(x+side,y+side,z+side)
    v8 = Vect3(x+side,y,z+side)
    list.append(Line(v1, v2))
    list.append(Line(v2, v3))
    list.append(Line(v3, v4))
    list.append(Line(v4, v1))

    list.append(Line(v5, v6))
    list.append(Line(v6, v7))
    list.append(Line(v7, v8))
    list.append(Line(v8, v5))

    list.append(Line(v1, v5))
    list.append(Line(v2, v6))
    list.append(Line(v3, v7))
    list.append(Line(v4, v8))
