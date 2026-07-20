import ipywidgets as widgets
from IPython.display import display
import random
import json
from pathlib import Path
import frontmatter
from typing import cast

from .formatting import markdown_to_html

def parse_question(question_file):
    post = frontmatter.load(str(question_file))
    content = post.content
    yaml_data = cast(dict, post.metadata)
    question = {
        'multiple_choice': multiple_choice,
        'input': input_question,
    }[yaml_data['question-type']](markdown_to_html(content), **yaml_data['question-fields'])

def create_quiz(questions_dir):
    questions_dir = Path(questions_dir)
    for question_file in sorted(questions_dir.glob("*.md")):
        parse_question((question_file))

def multiple_choice(question_text, options, correct_answer):
    if len(set(options)) != len(options):
        raise ValueError("Duplicate options are not allowed")
    if correct_answer not in options:
        raise ValueError("The correct answer is not among the given options")

    shuffled_options = options[:]
    random.shuffle(shuffled_options)

    question_text_field = widgets.HTML(value=question_text)

    # Create the RadioButtons widget for the multiple-choice question
    question_widget = widgets.RadioButtons(
        options=shuffled_options,
    )

    feedback_field = widgets.HTML(value="")

    confirm_button = widgets.Button(description="Confirm Answer")
    # Function to check the answer
    def check_answer(choice):
        if choice == correct_answer:
            feedback_field.value = "Correct!"
        else:
            feedback_field.value = "Oops! That's not right. Try again."
    confirm_button.on_click(lambda button: check_answer(question_widget.value))

    show_answer_button = widgets.Button(description="Show Right Answer")
    def show_right_answer(b):
        feedback_field.value = f"The correct answer is: {correct_answer}"
    show_answer_button.on_click(show_right_answer)

    # Display the widgets
    display(question_text_field, question_widget, confirm_button, show_answer_button, feedback_field)


def input_question(question_text, correct_answers, strip_answer=True):

    question_text_field = widgets.HTML(value=f"{question_text}")

    question_widget = widgets.Textarea(
        placeholder='Type your answer here',
    )

    feedback_field = widgets.HTML(value="")

    confirm_button = widgets.Button(description="Confirm Answer")
    # Function to check the answer
    def check_answer(answer):
        if strip_answer:
            answer = answer.strip()
        if answer in correct_answers:
            feedback_field.value = "Correct!"
        else:
            feedback_field.value = "Oops! That's not right. Try again."
    confirm_button.on_click(lambda button: check_answer(question_widget.value))

    show_answer_button = widgets.Button(description="Show Right Answer")
    def show_right_answer(b):
        feedback_field.value = f'<pre>The correct answer is: \n{correct_answers[0]}</pre>'
    show_answer_button.on_click(show_right_answer)

    # Display the widgets
    display(question_text_field, question_widget, confirm_button, show_answer_button, feedback_field)


def multiple_choice_questions(questions):
    for index, q in enumerate(questions):
        multiple_choice(f"Question {index}", *q)
