import streamlit as st
import os
import time
import subprocess


def save_uploaded_file(uploaded_file):
    with open(os.path.join("./samples", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())


def set_page_configuration():
    st.set_page_config(
        page_title="Загрузка MP3 файла",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        """
        <style>
        body {{
            background-image: url('https://example.com/background_image.jpg');
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def load_mp3_file():
    uploaded_file = st.file_uploader("Выберите MP3 файл", type=["mp3"])
    return uploaded_file


def run_file(file_path):
    start_time = time.time()
    subprocess.run(['python', file_path])
    end_time = time.time()
    execution_time = end_time - start_time
    hours = int(execution_time // 3600)
    minutes = int((execution_time % 3600) // 60)
    seconds = int(execution_time % 60)
    return f"Время выполнения скрипта: {hours} часов, {minutes} минут, {seconds} секунд"


def main():
    set_page_configuration()

    st.title("Конспектор ^_^")

    uploaded_file = load_mp3_file()

    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success("Файл успешно загружен!")

    def on_run_file_click():
        script_execution_time = run_file('./model.py')
        print(script_execution_time)

    if st.button('Запустить'):
        on_run_file_click()

    st.title("Загрузка и скачивание файла")
    result_file_path = './samples/result.txt'

    if os.path.isfile(result_file_path):
        with open(result_file_path, "r") as file:
            file_contents = file.read()

        st.text("Содержимое файла:")
        st.text(file_contents[0:1000])

        st.download_button("Скачать файл", data=file_contents, file_name=os.path.basename(result_file_path))
    else:
        st.error("Файл не найден. Пожалуйста, проверьте путь к файлу.")


if __name__ == "__main__":
    main()
