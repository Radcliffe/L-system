import turtle


def jump_forward(t, distance):
    t.penup()
    t.forward(distance)
    t.pendown()

def jump_to(t, xpos, ypos):
    t.penup()
    t.setpos(xpos, ypos)
    t.pendown()


class Lsystem:
    def __init__(self, start, rules, moves=None):
        self.start = start
        self.rules = rules
        if moves is None:
            moves = dict(L='L', R='R', F='F', M='M')
        self.moves = moves
    
    def gen(self, n):
        if n == 0:
            for char in self.start:
                yield char
        else:
            for char in self.gen(n-1):
                for ch in self.rules.get(char, char):
                    yield ch
        
    def draw(self, t, n, step=10, moves=None):
        if moves is None:
            moves = self.moves
        for char in self.gen(n):
            action = moves.get(char)
            if action is None: return
            verb = action[0]
            
            if verb in 'MF':
                distance = step
                if len(action) > 1:
                    distance *= float(action[1:])
                if verb == 'M':
                    jump_forward(t, distance)
                else:
                    t.forward(distance)
                distance = step
              
            elif verb in 'LR':
                angle = 90
                if len(action) > 1:
                    angle = float(action[1:])
                if verb == 'L':
                    t.left(angle)
                else:
                    t.right(angle)
    
        
def flowsnake():
    rules = dict(A = 'A-B--B+A++AA+B-',
                 B = '+A-BB--B-A++A+B')
    moves = {'A': 'F',
             'B': 'F',
             '+': 'R60',
             '-': 'L60'}
    return Lsystem('A', rules, moves)
       
if __name__ == '__main__':
    curve = flowsnake()
    t = turtle.Turtle()
    jump_to(t, 40, -240)
    t.speed(0)
    curve.draw(t, 4, step=8)
    t.hideturtle()
    input("Press Enter to exit.")
