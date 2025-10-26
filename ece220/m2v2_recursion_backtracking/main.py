from manim import *

from manim_hkn.utils import *
from manim_hkn import *

class Intro(Scene):
    def construct(self):
        hkn_emblem = ImageMobject("../../assets/hkn_alpha_emblem.png", z_index=1)

        self.play(FadeIn(hkn_emblem))
        self.wait(0.75)
        self.play(hkn_emblem.animate.scale(0.3).to_corner(UR), run_time = 1.5)
        
        self.play(Write(Title("Recursion and Backtracking")))
        self.play(Write(Tex(r"""
            \begin{itemize}
                \item Functions in C
                \item Recursion
                \begin{itemize}
                    \item Base cases
                    \item Recursive cases
                \end{itemize}
                \item Backtracking
                \item Recursion vs backtracking vs loops
            \end{itemize}""", font_size=40
        ).center()))
        
        self.play(FadeOut(*self.mobjects))
