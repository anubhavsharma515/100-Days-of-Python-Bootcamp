from turtle import Turtle
STARTING = [
  (0, 0),
  (-20, 0),
  (-40, 0)
]
MOVING_DISTANCE = 20

class Snake:
  

  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for pos in STARTING:
      self.add_segment(pos)

  def add_segment(self, pos):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.penup()
    new_segment.goto(pos)
    self.segments.append(new_segment)
  

  def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x, new_y)

    self.segments[0].forward(MOVING_DISTANCE)

  def l(self):
    current_angle = self.head.heading()
    if current_angle in (90, 270):
      self.head.seth(180)

  def r(self):
    current_angle = self.head.heading()
    if current_angle in (90, 270):
      self.head.seth(0)

  def u(self):
    current_angle = self.head.heading()
    if current_angle in (0, 180):
      self.head.seth(90)

  def d(self):
    current_angle = self.head.heading()
    if current_angle in (0, 180):
      self.head.seth(270)

  def update(self):
    self.add_segment(self.segments[-1].pos())
    
  def crossed_boundary(self):

    crossed = False
    if abs(self.head.xcor()) > 300 or abs(self.head.ycor()) > 300:
      crossed = True

    for segment in self.segments[1:]:
      if self.head.distance(segment.pos()) < 15:
        crossed = True

    return crossed


