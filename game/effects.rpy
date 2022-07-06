## effects.rpy

# This file defines all the effects in this game

init python:
    class ParticleBurst(object):
        def __init__(self, displayable, explode_time=0, particles_num=20, total_time=0.5, x_speed=3, y_speed=5):
            self.sm = SpriteManager(update=self.update)

            self.stars = []
            self.displayable = displayable
            self.explode_time = explode_time
            self.total_time = total_time
            self.x_speed = x_speed
            self.y_speed = y_speed
            self.gravity = 240
            
            for i in range(particles_num):
                self.add(self.displayable, 1)
        
        def add(self, d, speed):
            s = self.sm.create(d)
            speed = renpy.random.random()
            angle = renpy.random.random() * math.pi * 2
            x_speed = speed * math.cos(angle) * self.x_speed
            y_speed = speed * math.sin(angle) * self.y_speed - 1
            s.x = x_speed * 24
            s.y = y_speed * 24
            self.stars.append((s, y_speed, x_speed, self.total_time))
        
        def update(self, st):
            for i in range(len(self.stars)):
                star, y_speed, x_speed, time = self.stars[i]
                if st < time:
                    star.x = x_speed * 120 * (st + 0.2)
                    star.y = y_speed * 120 * (st + 0.2) + (self.gravity * st * st)
                else:
                    star.destroy()
                    self.stars.pop(i)
            return 0