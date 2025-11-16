import inspect

from manim import *

class SectionalizedScene(Scene):
    def __init__(self):
        super().__init__()
        self.skip_section_animations = False
    
    def next_section(self, *args, **kwargs):
        super().next_section(*args, **kwargs, skip_animations=self.skip_section_animations)
    
    def play(self, *args, **kwargs):
        if inspect.stack()[1].function != "wait":
            self.next_section()
        super().play(*args, **kwargs)
