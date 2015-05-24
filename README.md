lsystem
=======

This is a Python class for generating and drawing L-system. An L-system is a
formal grammar that generates fractal curves, such as the *flowsnake* shown below.

![flowsnake](flowsnake.png)

## Requirements

This program runs in Python 3.x. It will also run in Python 2.7, if you
substitute `raw_input` for `input` in the last line. The program requires the 
`tkinter` and `turtle` packages.

## Usage

To see a demo, just type

    $ python3 lsystem.py

The class `Lsystem` constructs a curve from an L-system. The constructor takes
three parameters.

1. `start` is the starting string (also called the *axiom*).
2. `rules` is a dictionary that contains the rules for rewriting a string.
3. `moves` (optional) is a dictionary that converts the string into turtle commands.

The draw command understands the following turtle commands:

1.  `Rn` : turn right *n* degrees (default = 90)
2.  `Ln` : turn left *n* degrees (default = 90)
3.  `Fn` : move and draw forward *n* steps (default = 1)
4.  `Mn` : move forward *n* steps without drawing (default = 1)
5.  `[`  : push the current position and heading onto the stack.
6.  `]`  : pop the position and heading from the stack.

The instance method `gen(n)` is a generator that yields the *n*th level of the
curve, one character at a time.

The instance method `draw` is used to draw the curve. It takes three parameters:

1.  `t` is the turtle object.
2.  `n` is the number of iterations.
3.  `step` is the step size in pixels (default value is 10).
4.  `moves` overrides the instance variable of the same name.


