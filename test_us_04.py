from us_04 import collect_course_selections


def test_collect_course_selections_ignores_invalid_and_duplicate_entries(monkeypatch):
    responses = iter(["cs101", "CS102", "cs101", "CS103", "CS102", "CS104"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    assert collect_course_selections(["CS101", "CS102", "CS103", "CS104"], 3) == ["CS101", "CS102", "CS103"]


def test_collect_course_selections_stops_after_required_count(monkeypatch):
    responses = iter(["CS101", "CS102", "CS103", "CS104"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(responses))

    assert collect_course_selections(["CS101", "CS102", "CS103", "CS104"], 2) == ["CS101", "CS102"]
