import streamlit as st
import os

filepath = './samples/result.txt'


def save_uploaded_file(uploaded_file):
    with open(os.path.join("./samples", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())


def main():
    # Set page configuration
    st.set_page_config(
        page_title="Загрузка MP3 файла",
        page_icon="🎵",
        layout="wide",
        initial_sidebar_state="expanded")

    # Custom CSS for background image
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://example.com/background_image.jpg');
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True,)

    st.title("Конспектор ^_^")

    uploaded_file = st.file_uploader("Выберите MP3 файл", type=["mp3"])

    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success("Файл успешно загружен!")

    def run_file():
        """to start calculation"""
        import time
        import subprocess
        start_time = time.time()
        file_path = './model.py'
        subprocess.run(['python', file_path])

        end_time = time.time()
        execution_time = end_time - start_time
        hours = int(execution_time // 3600)
        minutes = int((execution_time % 3600) // 60)
        seconds = int(execution_time % 60)
        print(f"Время выполнения скрипта: {hours} часов, "
              f"{minutes} минут, {seconds} секунд")

    st.button('Запустить', on_click=run_file)

    print("Ещё секунду Вашего терпения :)")

    st.title("Загрузка и скачивание файла")

    if filepath:
        if os.path.isfile(filepath):
            # read the file
            with open(filepath, "r") as file:
                file_contents = file.read()

            # Sample of trunscribed speach to the screen
            st.text("Содержимое файла:")
            st.text(file_contents[0:1000])

            # download result-file
            st.download_button("Скачать файл",
                               data=file_contents,
                               file_name=os.path.basename(filepath))
        else:
            st.error("Файл не найден. Пожалуйста, проверьте путь к файлу.")


if __name__ == "__main__":
    main()
