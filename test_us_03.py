from us_03 import prompt_course_count


def test_prompt_course_count_accepts_positive_integer(monkeypatch):
    responses = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    assert prompt_course_count(["CS101", "CS102", "CS103"]) == 3


def test_prompt_course_count_retries_on_invalid_input(monkeypatch, capsys):
    responses = iter(["0", "abc", "2"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    assert prompt_course_count(["CS101", "CS102"]) == 2
    captured = capsys.readouterr()
    assert "positive integer" in captured.out.lower()
