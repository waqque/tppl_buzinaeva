import os
import runpy
import sys
import pytest
from main import eval_postfix, main


def test_eval_postfix_examples():
    # Примеры из условия задания
    assert eval_postfix("3 0 4 ~ 2 ~") == 47
    assert eval_postfix("2 2 + 4 - 4 ~ 2 3 * +") == 22


def test_eval_postfix_arithmetic():
    assert eval_postfix("5 3 +") == 8
    assert eval_postfix("10 4 -") == 6
    assert eval_postfix("3 7 *") == 21
    assert eval_postfix("8 2 /") == 4
    assert eval_postfix("7 2 /") == 3.5
    assert eval_postfix("2.5 1.5 +") == 4


def test_eval_postfix_tilde_operator():
    # Если оба операнда не равны 0 -> |x - y|
    assert eval_postfix("5 2 ~") == 3
    assert eval_postfix("2 5 ~") == 3

    # Если хотя бы один операнд равен 0 -> (sum(стек))^2
    assert eval_postfix("1 4 0 ~") == 25
    assert eval_postfix("0 0 ~") == 0


def test_eval_postfix_errors():
    assert eval_postfix("") is None
    assert eval_postfix("5 +") is None
    assert eval_postfix("2 abc +") is None
    assert eval_postfix("2 3 4 +") is None


def test_main_input(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py"])
    monkeypatch.setattr("builtins.input", lambda _: "3 0 4 ~ 2 ~")
    main()
    captured = capsys.readouterr()
    assert "3 0 4 ~ 2 ~ = 47" in captured.out


def test_main_valid_expression(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "3", "0", "4", "~", "2", "~"])
    main()
    captured = capsys.readouterr()
    assert "3 0 4 ~ 2 ~ = 47" in captured.out


def test_main_invalid_expression(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["main.py", "10", "0", "/"])
    main()
    captured = capsys.readouterr()
    assert "деление на ноль невозможно" in captured.out.lower()


def test_main_run_as_script(monkeypatch, capsys):
    main_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))
    monkeypatch.setattr(sys, "argv", ["main.py", "2", "3", "+"])
    runpy.run_path(main_path, run_name="__main__")
    captured = capsys.readouterr()
    assert "2 3 + = 5" in captured.out
