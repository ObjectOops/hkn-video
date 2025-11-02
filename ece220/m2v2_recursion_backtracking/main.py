from itertools import chain

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
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        )
        self.play(Transform(question, example_function, replace_mobject_with_target_in_scene=True))

        # Modifiers
        modifier_chars = example_function.code_lines.lines[0][0][0:6]
        modifier_highlight = SurroundingRectangle(modifier_chars, color=YELLOW)
        modifier_annotation = Text("Modifier", font_size=25, color=YELLOW).next_to(modifier_highlight, LEFT)
        
        # Return Type
        return_type_chars = example_function.code_lines.lines[0][0][7:10]
        return_type_highlight = SurroundingRectangle(return_type_chars, color=GREEN)
        return_type_annotation = Text("Return Type", font_size=25, color=GREEN).next_to(return_type_highlight, UP).shift(LEFT)
        
        # Name
        name_highlight = SurroundingRectangle(example_function.code_lines.lines[0][0][11:21], color=RED)
        name_annotation = Text("Name", font_size=25, color=RED).next_to(name_highlight, UP)
        
        # Parameters
        parameters_chars = example_function.code_lines.lines[0][0][22:-4]
        parameters_highlight = SurroundingRectangle(parameters_chars, color=ORANGE)
        parameters_annotation = Text("Parameters", font_size=25, color=ORANGE).next_to(parameters_highlight, UP)

        highlight_annotations = [
            (return_type_highlight, return_type_annotation), 
            (modifier_highlight, modifier_annotation), 
            (name_highlight, name_annotation), 
            (parameters_highlight, parameters_annotation)
        ]

        for highlight, annotation in highlight_annotations:
            self.play(Create(highlight), Write(annotation))
        
        # Section: Return Types
        self.play(FadeOut(
            modifier_highlight, modifier_annotation, 
            return_type_highlight, 
            name_highlight, name_annotation, 
            parameters_highlight, parameters_annotation
        ))
        self.play(Indicate(return_type_chars))
        
        example_function_void = Code(
            code_string=r"""
static void myFunction(int foo, int bar)
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        ).to_edge(UP)
        self.play(FadeIn(example_function_void))
        self.play(Indicate(example_function_void.code_lines.lines[0][0][7:11]))
        self.play(FadeOut(example_function_void))
        
        example_function_2 = Code(
            code_string=r"""
int myFunction2(int foo, int bar) {
    int number = foo + bar;
    if (number > 3) {
        return number; // We only return within this if block so 
    }                  // this will cause a compiler error
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        )
        self.play(FadeOut(example_function, return_type_annotation), Write(example_function_2))
        self.play(Indicate(example_function_2.code_lines.lines[0][3][8:14]))
        
        example_function_3 = Code(
            code_string=r"""
void divide(int* foo, int bar) {
    if (bar == 0) {
        return; // End the function to avoid division by 0
    }
    *foo = *foo/bar; // Pointer used here, don't worry about this rn
    // Note we do NOT need another return statement here because the 
    // return type is void. Though adding return is also fine
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        )
        self.play(Transform(example_function_2, example_function_3, replace_mobject_with_target_in_scene=True))
        
        # Section: Names and Parameters
        self.play(FadeOut(example_function_3), FadeIn(example_function, parameters_annotation))
        self.play(Indicate(parameters_chars[4:7]))
        self.play(Indicate(parameters_chars[13:16]))
        self.play(Indicate(parameters_chars[0:3]), Indicate(parameters_chars[9:12]))
        
        example_function_char = Code(
            code_string=r"""
static void myFunction(char foo, int bar)
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        ).to_edge(UP)
        self.play(FadeIn(example_function_char))
        self.play(Indicate(example_function_char.code_lines.lines[0][0][23:27]))
        self.play(FadeOut(example_function_char))
        
        # Section: Scope
        self.play(FadeOut(parameters_annotation))
        self.play(
            Indicate(example_function.code_lines.lines[0][0][-1]), 
            Indicate(example_function.code_lines.lines[0][-1][-1])
        )
        example_function_4 = Code(
            code_string=r"""
int main() {
    int var1 = 10; // declared in main scope
    {
        int var2 = 20; // declared in a new scope
        printf("%d\n", var1 + var2); // valid here
    }
    int sum = var1 + var2; // This will cause a compiler error
    return 0;
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        )
        self.play(FadeOut(example_function), Write(example_function_4))
        
        # Section: Static Modifier
        self.play(FadeOut(example_function_4), FadeIn(example_function, modifier_annotation))
        self.play(Indicate(modifier_chars))
        
        example_function_5 = Code(
            code_string=r"""
int count() {
    // running_count is persistent across function calls, it is 
    // NOT reset to 0 each time the function is called
    static int running_count = 0; 
    running_count++;
    return running_count;
}
int main() {
    count(); // set running_count to 0 and increment to 1
    count(); // now increment running_count to 2
    printf("%d\n", count()); // this will increment to 3 and print 3
    int rc = running_count; // this will cause an error from trying 
                            // to access a variable local to count()
	return 0;
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        )
        self.play(FadeOut(example_function, modifier_annotation), Write(example_function_5))
        self.play(example_function_5.animate.scale(0.5).to_edge(LEFT))
        
