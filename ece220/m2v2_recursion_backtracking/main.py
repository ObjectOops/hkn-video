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

class Functions(Scene):
    def construct(self):
        question = Text("?")
        self.play(Write(question))
        
        example_function = Code(
            code_string=r"""
static int myFunction(int foo, int bar) { 
    int number = foo + bar;
    return number;
}
""",
            language="py",
            add_line_numbers=False
        )
        self.play(Transform(question, example_function))

        # Modifiers
        modifier_highlight = SurroundingRectangle(example_function.code_lines.lines[0][0][0:6], color=YELLOW)
        modifier_annotation = Text("Modifier", font_size=25, color=YELLOW).next_to(modifier_highlight, LEFT)
        
        # Return Type
        return_type_highlight = SurroundingRectangle(example_function.code_lines.lines[0][0][7:10], color=GREEN)
        return_type_annotation = Text("Return Type", font_size=25, color=GREEN).next_to(return_type_highlight, UP).shift(LEFT)
        
        # Name
        name_highlight = SurroundingRectangle(example_function.code_lines.lines[0][0][11:21], color=RED)
        name_annotation = Text("Name", font_size=25, color=RED).next_to(name_highlight, UP)
        
        # Parameters
        parameters_highlight = SurroundingRectangle(example_function.code_lines.lines[0][0][22:-4], color=ORANGE)
        parameters_annotation = Text("Parameters", font_size=25, color=ORANGE).next_to(parameters_highlight, UP)

        self.play(
            Create(modifier_highlight), Write(modifier_annotation), 
            Create(return_type_highlight), Write(return_type_annotation), 
            Create(name_highlight), Write(name_annotation), 
            Create(parameters_highlight), Write(parameters_annotation)
        )
