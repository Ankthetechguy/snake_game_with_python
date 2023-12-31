from turtle import Turtle
STARTING_POSITION= [(0,0),(-20,0),(-40,0)]
up = 90
down = 270
right = 0
left = 180
move = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]
    
    def createsnake(self):
        for position in  STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self,position):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)     
        self.head.forward(move)
    
    def up(self):
        if self.head.heading()!=down:
          self.head.setheading(up)
    
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
    
    def right(self):
        if self.head.heading()!=left:
            self.head.setheading(right)
    
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)  


