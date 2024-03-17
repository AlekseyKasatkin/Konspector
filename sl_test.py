import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))
from sl_2 import run_file


def test_run_file(monkeypatch):
    test_file_name = "sl_test.py"
    test_file_path = os.path.join(os.path.dirname(__file__), test_file_name)

    # Создаем контекст для виртуальной сессии Streamlit
    with st.empty():
        # Заменяем функцию set_option,
        # чтобы устанавливать параметры перед запуском
        monkeypatch.setattr(st, 'set_option', lambda key, value: None)

        # Загружаем и запускаем файл в Streamlit, используя функцию main
        result = run_file(test_file_path)

    # Убедимся, что результат выполнения файла соответствует ожидаемому
    assert "Время выполнения скрипта:" in result, \
        (f"Ожидаемая подстрока 'Время выполнения скрипта:'"
         f" не найдена в строке '{result}'")
