"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Zhengxiao Zou.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

a_ok_turtle = rg.SimpleTurtle('turtle')
a_ok_turtle.pen = rg.Pen('red',2)
a_ok_turtle.speed = 5
for  k in range (5):
    a_ok_turtle.right(144)
    a_ok_turtle.forward(400)

b_ok_turtle = rg.SimpleTurtle('turtle')
b_ok_turtle.pen = rg.Pen('blue',2)
b_ok_turtle.speed = 6
b_ok_turtle.pen_up()
b_ok_turtle.right(45)
b_ok_turtle.forward(10)
b_ok_turtle.left(45)
b_ok_turtle.pen_down()
for  k in range (5):
    b_ok_turtle.right(144)
    b_ok_turtle.forward(400)



window.close_on_mouse_click()
