from p1_util.tests.test_util import call_function, run_script

import pytest

@pytest.mark.parametrize(
    "grade",
    [0, 1, 10, 14, 19, 20]
)
def test_function(pytestconfig, grade):
    result = call_function(__file__, "ExamResult", ["Programming 1", grade])
    assert result.course == "Programming 1", f"Expected course 'Programming 1', got {result.course!r}"
    assert result.grade == grade, f"Expected grade {grade!r}, got {result.grade!r}"

@pytest.mark.parametrize(
    "grade",
    [-1, -3, 21, 25, 100]
)
def test_function_invalid_constructor(pytestconfig, grade):
    # call_function turns any error raised by the constructor into a test failure
    # (pytest.fail), so we check for that failure and make sure it was a ValueError
    with pytest.raises(pytest.fail.Exception) as error:
        call_function(__file__, "ExamResult", ["Programming 1", grade])
    assert "ValueError" in str(error.value), (
        f"Creating an ExamResult with grade {grade} should raise a ValueError, but got:\n{error.value}"
    )

@pytest.mark.parametrize(
    "grade",
    [0, 20, 16]
)
def test_function_setter_valid(pytestconfig, grade):
    result = call_function(__file__, "ExamResult", ["Programming 1", 10])
    result.set_grade(grade)
    assert result.grade == grade, f"Expected grade {grade!r} after set_grade({grade!r}), got {result.grade!r}"

@pytest.mark.parametrize(
    "grade",
    [-1, 21, 25]
)
def test_function_setter_invalid(pytestconfig, grade):
    result = call_function(__file__, "ExamResult", ["Programming 1", 10])
    with pytest.raises(ValueError):
        result.set_grade(grade)
    assert result.grade == 10, f"The grade should stay unchanged after an invalid set_grade, got {result.grade!r}"
