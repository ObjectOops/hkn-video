import numpy as np

from manim import *
from manim.mobject.text.text_mobject import remove_invisible_chars

from manim_hkn.utils import *
from manim_hkn import *

from common.util import *

class Intro(SectionalizedScene):
    def construct(self):
        # self.skip_section_animations = True

        self.hkn_emblem_animation()
        
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
        
        self.end_scene()

class Functions(SectionalizedScene):
    def construct(self):
        # self.skip_section_animations = True
        
        self.hkn_emblem_add()
        
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
        self.play(ReplacementTransform(question, example_function))

        # Specifiers
        specifier_chars = example_function.code_lines.lines[0][0][0:6]
        specifier_highlight = SurroundingRectangle(specifier_chars, color=YELLOW)
        specifier_annotation = Text("Specifier", font_size=25, color=YELLOW).next_to(specifier_highlight, LEFT)
        
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
            (specifier_highlight, specifier_annotation), 
            (name_highlight, name_annotation), 
            (parameters_highlight, parameters_annotation)
        ]

        for highlight, annotation in highlight_annotations:
            self.play(Create(highlight), Write(annotation))
        
        # Section: Return Types
        self.play(FadeOut(
            specifier_highlight, specifier_annotation, 
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
        self.play(ReplacementTransform(example_function_2, example_function_3))
        
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
            Circumscribe(remove_invisible_chars(example_function.code_lines.lines[0][0])[-1]), 
            Circumscribe(remove_invisible_chars(example_function.code_lines.lines[0][-1])[-1])
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
        
        # Section: Static Specifier
        self.play(FadeOut(example_function_4), FadeIn(example_function, specifier_annotation))
        self.play(Indicate(specifier_chars))
        
        example_function_5 = Code(
            code_string=r"""
int count() {
    // runningCount is persistent across function calls, it is 
    // NOT reset to 0 each time the function is called
    static int runningCount = 0; 
    runningCount++;
    return runningCount;
}
int main() {
    count(); // set runningCount to 0 and increment to 1
    count(); // now increment runningCount to 2
    printf("runningCount: %d\n", count()); // this will increment to 3 and print 3
    int rc = runningCount; // this will cause an error from trying 
                            // to access a variable local to count()
	return 0;
}
""",
            language="c",
            add_line_numbers=True, 
            formatter_style="dracula"
        ).scale(0.75)
        self.play(FadeOut(example_function, specifier_annotation), Write(example_function_5))
                
        labels_5 = ["runningCount", "rc"]
        example_table_5 = Table(
            col_labels=[monospace(label) for label in labels_5], 
            table=[["0", "-"]]
        ).scale(0.5).to_edge(RIGHT)
        self.play(example_function_5.animate.scale(0.5 / 0.75).to_edge(LEFT), Create(example_table_5))

        run_start_5 = (9, {}, None, [])
        code_highlight = SurroundingRectangle(
            remove_invisible_chars(example_function_5.code_lines.lines[0][run_start_5[0] - 1]), buff=0, stroke_width=1
        ).stretch_to_fit_width(example_function_5.background.width).align_to(example_function_5.background, LEFT)
        self.play(Create(code_highlight))
        run_5 = [
            run_start_5, 
            (4, {}, None, []), 
            (5, {"runningCount": "0"}, None, []), 
            (6, {"runningCount": "1"}, None, []), 
            (10, {}, None, []), 
            (4, {}, None, []), 
            (5, {}, None, []), 
            (6, {"runningCount": "2"}, None, []), 
            (11, {}, None, []), 
            (4, {}, None, []), 
            (5, {}, None, []), 
            (6, {"runningCount": "3"}, None, []), 
            (11, {}, None, []), 
            (12, {}, "runningCount: 3", [Succession(Wiggle(code_highlight), Indicate(code_highlight, scale_factor=1, color=RED))]), 
            (14, {}, None, [])
        ]
        current_output = None
        for line, vals, out, other in run_5:
            code_line = remove_invisible_chars(example_function_5.code_lines.lines[0][line - 1])
            value_update_animations = []
            for key, val in vals.items():
                text_cell = example_table_5.get_entries_without_labels((1, labels_5.index(key) + 1))
                text_cell_updated = Paragraph(val).match_width(text_cell).move_to(text_cell)
                value_update_animations.append(Transform(text_cell, text_cell_updated))
                value_update_animations.append(Circumscribe(text_cell))
            if current_output is not None and out is not None:
                self.remove(current_output)
            if out is not None:
                current_output = Text(out).to_edge(DOWN)
            self.play(
                code_highlight.animate.match_y(code_line), 
                *value_update_animations, 
                TypeWithCursor(current_output) if out is not None else Wait()
            )
            if (len(other) > 0):
                self.play(*other)
            self.wait(0.25)
                
        self.play(FadeOut(example_function_5, code_highlight, example_table_5, current_output))
        
        example_function_6 = Code(
            code_string=r"""
static int myFunctionStatic(int foo, int bar) { 
    int number = foo + bar;
    return number;
}  

int mySecondFunction() {
    int firstNum = 3;
    int secondNum = 4;
    // Here the function call is valid and we return 7 
    return myFunctionStatic(firstNum, secondNum);
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula", 
            background="window"
        ).scale(0.75)
        example_title_6 = monospace("file_1.c").scale(0.4).align_to(example_function_6.background.get_top(), UP).shift(0.1 * DOWN)
        self.play(Create(example_function_6), Write(example_title_6))
        
        example_chars_6 = example_function_6.code_lines.lines[0]
        self.play(Succession(
            Indicate(example_title_6), 
            Indicate(example_chars_6[0][11:27]), 
            Indicate(example_chars_6[0][0:6]), 
            Indicate(example_chars_6[5][4:20])
        ))
        example_caption_6 = Text("Inside same translation unit: ✔️", color=GREEN).scale(0.5).align_to(example_function_6.background.get_bottom(), UP).shift(0.1 * DOWN)
        self.play(Write(example_caption_6))
        
        example_group_6 = VGroup(example_function_6, example_title_6, example_caption_6)
        question_2 = Text("Another translation unit / file...")
        self.play(example_group_6.animate.scale(0.75).to_edge(UP), Write(question_2))
        
        example_function_7 = Code(
            code_string=r"""
int multiplier(int foo, int bar){ 
    int number = 0;
    for (int i = 0; i < bar; i++){
        // This will throw an error because myFunctionStatic is 
        // static inside file_1.c
        number += myFunctionStatic(foo, number); 
    }
    return number;
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula", 
            background="window"
        ).scale(0.75).align_to(example_group_6.get_bottom(), UP).shift(0.1 * DOWN)
        example_title_7 = monospace("file_2.c").scale(0.4).align_to(example_function_7.background.get_top(), UP).shift(0.1 * DOWN)
        example_chars_7 = example_function_7.code_lines.lines[0]
        example_caption_7 = Text("Inside same translation unit: ✖️", color=RED).scale(0.5).align_to(example_function_7.background.get_bottom(), UP).shift(0.1 * DOWN)
        example_group_7 = VGroup(example_function_7, example_title_7, example_caption_7)
        example_group_7.scale(0.75)
        
        self.play(ReplacementTransform(question_2, example_function_7), Write(example_title_7))
        self.play(Succession(
            Indicate(example_title_7), 
            Indicate(example_chars_7[5][18:34], color=RED)
        ))
        self.play(Write(example_caption_7))
        
        self.end_scene()

class Recursion(SectionalizedScene):
    def construct(self):
        # self.skip_section_animations = True
        
        self.hkn_emblem_add()
        
        question = Text("Recursion")
        notes = Tex(r"""
            \begin{itemize}
                \item A programming method which involves a function calling itself
                \item Makes implementing algorithms easier
                \item All recursive functions can be implemented iteratively
                \item Often produce simple and elegant solutions
            \end{itemize}""", font_size=40
        ).center()
        self.play(Write(question))
        self.play(ReplacementTransform(question, notes))

        self.end_scene()
        self.fibonacci_visualization()
        self.end_scene()
        
        example_fibonacci = Code(
            code_string=r"""
int fibonacci(int n) {
    // Base Case: returns itself for 0 or 1
	if (n == 0 || n == 1) { 
        return n;
    }
    
    // Recursive Case: Calls itself using the fibonacci definition
    return fibonacci(n - 1) + fibonacci(n - 2); 
}
""",
            language="c",
            add_line_numbers=False, 
            formatter_style="dracula"
        ).scale(0.75)
        example_fibonacci_chars = example_fibonacci.code_lines.lines[0]
        base_case_outline = SurroundingRectangle(remove_invisible_chars(example_fibonacci_chars[1:5]), color=ORANGE)
        recursive_case_outline = SurroundingRectangle(remove_invisible_chars(example_fibonacci_chars[6:10]), color=GREEN)
        self.play(Succession(
            Write(example_fibonacci), 
            Create(base_case_outline), 
            Create(recursive_case_outline)
        ))
        
        tips_fibonacci = [
            "All recursive functions must have a base case and recursive case.", 
            "The base case is what allows the function to actually stop and return something.", 
            "Stack overflow, segmentation fault: runtime stack grows too large.", 
            "Check to make sure you eventually reach your base case!"
        ]
        current_tip = None
        for tip in tips_fibonacci:
            self.play(
                FadeOut(current_tip) if current_tip is not None else Wait(), 
                FadeIn(current_tip := Text(tip).scale(0.5).align_to(example_fibonacci, DOWN).shift(DOWN))
            )
                
        self.play(FadeOut(current_tip, base_case_outline, recursive_case_outline), example_fibonacci.animate.scale(0.5).to_corner(UL))
                
        fibonacci = lambda n: n if n == 0 or n == 1 else fibonacci(n - 1) + fibonacci(n - 2)
        def fibonacci_tree(n):
            fib = monospace(f"fibonacci({n}) == {fibonacci(n)}").scale(0.3)
            fib_center = fib.get_edge_center(DOWN)
            if n == 0 or n == 1:
                return fib, VGroup(fib)
            fib_sub_1 = fibonacci_tree(n - 2)
            fib_sub_2 = fibonacci_tree(n - 1)
            fib_left, fib_left_group = fib_sub_1 if n % 2 == 0 else fib_sub_2
            fib_right, fib_right_group = fib_sub_2 if n % 2 == 0 else fib_sub_1
            fib_left_group.shift(fib_center + DOWN * 0.25 + LEFT * 1.25 - fib_left.get_edge_center(UP))
            fib_right_group.shift(fib_center + DOWN * 0.25 + RIGHT * 1.25 + DOWN * (fibonacci(n) / 2.5 - 1 / 2.5) + RIGHT * (fibonacci(n) - 1) - fib_right.get_edge_center(UP))
            return fib, VGroup(
                fib, fib_left_group, fib_right_group, 
                Line(fib_left.get_edge_center(UP), fib_center, buff=0.1), 
                Line(fib_right.get_edge_center(UP), fib_center, buff=0.1)
            )
        
        # Base Cases
        fib_base = VGroup(fibonacci_tree(0), fibonacci_tree(1)).arrange()
        self.play(Create(fib_base))
        
        # fibonacci(2)
        fib_2 = fibonacci_tree(2)[1]
        self.play(FadeOut(fib_base), FadeIn(fib_2))
        fib_base = fib_2
        
        # fibonacci(3)
        self.play(Transform(fib_base, fibonacci_tree(3)[1]))
        
        # fibonacci(4)
        self.play(Transform(fib_base, fibonacci_tree(4)[1].shift(UP)))
        
        # fibonacci(5)
        self.play(Transform(fib_base, fibonacci_tree(5)[1].shift(UP * 2)))
        
        # fibonacci(6)
        self.play(Transform(fib_base, fibonacci_tree(6)[1].scale_to_fit_width(config.frame_width).scale(0.9).to_corner(UL)), example_fibonacci.animate.shift(LEFT * 7))
        
        self.end_scene()

    # NOTE: Generated by GitHub Copilot
    def fibonacci_visualization(self):
        # Fibonacci visualization
        fib = [0, 1]
        boxes = []

        # create initial two boxes
        for v in fib:
            r = RoundedRectangle(corner_radius=0.08, width=0.75, height=0.75, stroke_width=2)
            lbl = Text(str(v), font_size=36).move_to(r.get_center())
            boxes.append(VGroup(r, lbl))

        self.play(*[FadeIn(b) for b in boxes])

        # equation / explanation area
        eq = MathTex(r"F_n = F_{n-1} + F_{n-2}").to_edge(UP)
        self.play(Write(eq))

        # build sequence up to N
        N = 8
        for n in range(2, N):
            a = boxes[-2]
            b = boxes[-1]
            # highlight the two previous terms
            self.play(Circumscribe(a, fade_out=True), Circumscribe(b, fade_out=True))
            # placeholder for new box (appears to the right)
            new_rect = RoundedRectangle(corner_radius=0.08, width=0.75, height=0.75, stroke_width=2)
            new_lbl = Text("?", font_size=36).move_to(new_rect.get_center())
            new_group = VGroup(new_rect, new_lbl).next_to(boxes[-1], RIGHT, buff=0.5)
            self.play(FadeIn(new_group))

            # arrows from the two contributors
            arr1 = Arrow(a.get_right() - UP * 0.25, new_group.get_left() - UP * 0.25, buff=0.1, stroke_width=2)
            arr2 = Arrow(b.get_right() + UP * 0.25, new_group.get_left() + UP * 0.25, buff=0.1, stroke_width=2)
            self.play(GrowArrow(arr1), GrowArrow(arr2))

            # compute and display the sum in the equation area
            next_val = fib[-1] + fib[-2]
            expr = MathTex(
                rf"F_{{{n}}}=F_{{{n-1}}}+F_{{{n-2}}}={fib[-1]}+{fib[-2]}={next_val}"
            ).to_edge(UP)
            self.play(Transform(eq, expr))
            # reveal the computed value in the new box
            new_value = Text(str(next_val), font_size=36).move_to(new_rect.get_center())
            self.play(Transform(new_lbl, new_value))
            # tidy arrows (fade) and append new term
            self.play(FadeOut(arr1), FadeOut(arr2))
            fib.append(next_val)
            boxes.append(new_group)

            # self.wait(0.5)

        # final flourish: highlight full sequence and show numeric list
        self.play(*[Indicate(b) for b in boxes])
        list_tex = MathTex(r"\{ " + ", ".join(str(x) for x in fib) + r" \}").to_edge(UP)
        self.play(Transform(eq, list_tex))
        # self.wait(1)

class Backtracking(SectionalizedScene):
    def construct(self):
        # self.skip_section_animations = True
        
        self.hkn_emblem_add()
        
        question = Text("Backtracking")
        notes = Tex(r"""
            \begin{itemize}
                \item A technique using recursion
                \item Backtracking is often used to search solution spaces, such as trees or graphs
                \item Time complexity isn't very good (more in CS 225)
            \end{itemize}""", font_size=40
        ).center()
        self.play(Write(question))
        self.play(ReplacementTransform(question, notes))
        
        self.play(FadeOut(notes))
        
        example_maze = Code(
            code_string=r"""
mazeSolver(path) {
    // Base Cases: solution has been reached or dead end

    if (path reached dead end) { return invalidPath }
    if (path reached maze end) { return path }

    // Recursive Case: Check the possible paths from the 
    // current point and backtrack to pick the best one

    for (all directions) {
        newPath = mazeSolver(currPath + stepInDirection)
        if (newPath is valid) {
            return newPath
        }
    }
    return invalidPath
}

mazeSolver(startPoint)
""",
            language=None,
            add_line_numbers=False, 
            formatter_style="dracula"
        ).scale(0.75)
        self.play(Write(example_maze))
        
        example_maze_chars = example_maze.code_lines.lines[0]
        self.play(Indicate(example_maze_chars[17]))
        self.play(Indicate(example_maze_chars[3]))
        self.play(Indicate(example_maze_chars[4]))
        
        maze = np.array([
            ["S", "1", "1", "1", "1", "1", "0", "1"], 
            ["0", "1", "0", "0", "0", "0", "0", "1"], 
            ["0", "1", "0", "1", "1", "0", "1", "1"], 
            ["0", "0", "0", "0", "1", "0", "0", "0"], 
            ["1", "0", "1", "0", "1", "1", "0", "1"], 
            ["1", "0", "1", "0", "1", "1", "0", "1"], 
            ["0", "0", "1", "0", "1", "0", "0", "0"], 
            ["1", "1", "1", "E", "1", "0", "1", "1"]
        ])
        example_table = Table(table=maze).scale(0.3).to_edge(RIGHT)
        for coord, val in np.ndenumerate(maze):
            match val:
                case "S":
                    example_table.add_highlighted_cell((coord[0] + 1, coord[1] + 1), color=GREEN)
                case "E":
                    example_table.add_highlighted_cell((coord[0] + 1, coord[1] + 1), color=RED)
                case "1":
                    example_table.add_highlighted_cell((coord[0] + 1, coord[1] + 1), color=GREY)
                case _:
                    pass
        self.play(example_maze.animate.scale(0.5 / 0.75).to_edge(LEFT), Create(example_table))

        code_highlight = SurroundingRectangle(
            remove_invisible_chars(example_maze.code_lines.lines[0][18]), buff=0, stroke_width=1
        ).stretch_to_fit_width(example_maze.background.width).align_to(example_maze.background, LEFT)
        self.play(Create(code_highlight))

        visited = np.zeros_like(maze)
        def goto_line(line):
            code_line = remove_invisible_chars(example_maze.code_lines.lines[0][line - 1])
            code_highlight.match_y(code_line)
            self.wait(duration=0.1)
        def solve_maze(row, col):
            goto_line(1)
            out_of_bounds = row < 0 or row >= maze.shape[1] or col < 0 or col >= maze.shape[0]
            if not out_of_bounds:
                focus_cell = SurroundingRectangle(example_table.get_entries((row + 1, col + 1)))
                self.add(focus_cell)
                self.wait(duration=0.1)
            
            goto_line(4)
            if out_of_bounds or visited[row][col] or maze[row][col] == "1":
                if not out_of_bounds:
                    self.remove(focus_cell)
                return False
            goto_line(5)
            if maze[row][col] == "E":
                self.remove(focus_cell)
                return True
            
            # print(row, col)
            self.remove(focus_cell)
            highlight = example_table.get_highlighted_cell((row + 1, col + 1), color=ORANGE)
            example_table.add_to_back(highlight)
            self.wait(duration=0.1)
            visited[row][col] = 1
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for direction in directions:
                goto_line(11)
                path = solve_maze(row + direction[0], col + direction[1])
                goto_line(12)
                if path:
                    goto_line(13)
                    return True
            goto_line(16)
            example_table.remove(highlight)
            self.wait(duration=0.1)
            return False
                
        solve_maze(0, 0)
        
        self.end_scene()
