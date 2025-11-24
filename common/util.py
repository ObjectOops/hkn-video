import inspect

from manim import *


class SectionalizedScene(Scene):
    
    def __init__(self):
        super().__init__()
        self.hkn_emblem = ImageMobject("../../assets/hkn_alpha_emblem.png", z_index=1)
        self.skip_section_animations = False
    
    def hkn_emblem_animation(self):
        self.play(FadeIn(self.hkn_emblem))
        self.wait(0.75)
        self.play(self.hkn_emblem.animate.scale(0.3).to_corner(UR), run_time = 1.5)
    
    def hkn_emblem_add(self):
        self.add(self.hkn_emblem.scale(0.3).to_corner(UR))
    
    def next_section(self, *args, **kwargs):
        super().next_section(*args, **kwargs, skip_animations=self.skip_section_animations)
    
    def play(self, *args, **kwargs):
        if inspect.stack()[1].function != "wait":
            self.next_section()
        super().play(*args, **kwargs)
    
    def end_scene(self):
        self.play(FadeOut(mobject) for mobject in self.mobjects if mobject != self.hkn_emblem)
