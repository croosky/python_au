from math import sqrt
import sys

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Triangle:
    def __init__(self,A,B,C):
        def length(x1,y1,x2,y2):
            return sqrt((x1-x2)**2+(y1-y2)**2)
        self.a=length(B.x,B.y,C.x,C.y)
        self.b=length(A.x,A.y,C.x,C.y)
        self.c=length(B.x,B.y,A.x,A.y)

        self.Ax = A.x
        self.Ay = A.y
        self.Bx = B.x
        self.By = B.y
        self.Cx = C.x
        self.Cy = C.y
    def isTriangle(self):
        if self.a+self.b>self.c or self.a+self.c>self.b or self.b+self.c>self.a: return True
        return False
    def isIsosceles(self):
        if self.a==self.b or self.b==self.c or self.a==self.c: return True
        return False
    def Area(self):
        p=(self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

class File:
    def __init__(self,name):
        self.name=name
    def getLines(self):
        file=open(self.name)
        lines=file.readlines()
        file.close()
        return lines
    def writeTriangle(self,coordinates):
        file=open(self.name,'w')
        string_coord=" ".join(coordinates)
        file.write(string_coord)
        file.close()
    def Error(self):
        file=open(self.name,'w')
        file.write("Что-то пошло не так.")
        file.close()

def getTriangles(lines):
    triangles=[]
    for line in lines:
        coords=line.split()
        if len(coords)==6:
            triangles.append(Triangle(Point(int(coords[0]),int(coords[1])),Point(int(coords[2]),int(coords[3])),Point(int(coords[4]),int(coords[5]))))
    return triangles

def main():
    in_file=File(sys.argv[1])
    lines=in_file.getLines()
    max_area= -1
    coords_max=[]
    triangles=getTriangles(lines)
    for triangle in triangles:
        if triangle.isTriangle() and triangle.isIsosceles():
            area=triangle.Area()
            if area>max_area:
                max_area=area
                coords_max=[str(triangle.Ax),str(triangle.Ay),str(triangle.Bx),str(triangle.By),str(triangle.Cx),str(triangle.Cy)]
    out_file=File(sys.argv[2])
    if max_area==-1 and lines:
        out_file.Error()
    out_file.writeTriangle(coords_max)

if __name__=='__main__':
    main()