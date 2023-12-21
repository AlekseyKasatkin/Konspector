    Название проекта "Конспектор"
Целью данного проекта является разработка и реализация эффективного и точного сервиса транскрибации аудиозаписей 
с использованием искусственного интеллекта и машинного обучения. Этот сервис позволит студентам и другим пользователям 
преобразовывать аудиозаписи в текстовый формат. Наш сервис будет универсальным, легким в использовании и обеспечит 
высокое качество транскрибации, чтобы пользователи могли легко обрабатывать и анализировать информацию из аудиозаписей.

    За основу взята обученная модель "/whisper-large-v3"

    Описание:
    model.py:
    модуль загрузки модели, настройки параметров обработки.
    "sample" - путь до исходного аудио файла (mp3)  
    Результат сохраняется в result.txt в корне
    
    Voice - (опция) Запись голоса с микрофона с последующей конвертацией в mp3 и сохранения в файл output.mp3 в корень
    
    для больших файлов необходимо настроить параметры обработки по чанкам согласно используемого оборудования: 
    max_new_tokens=128,
    chunk_length_s=15,
    batch_size=16,
    
    На настоящий момент удалось запустить и получить результаты в примелимое время на небольших файлах (<= 5мин, 
    device = cpu). Планируем эксперименты с использованием gpu.

Команда: 
Касаткин Алексей (капитан команды): Менеджер проекта, Аналитик данных, Программист-разработчик 
Кондратьев Андрей: Full Stack-разработчик, Тестировщик-QA инженер, Документалист/технический писатель
    
В настоящее время в интернете доступно огромное количество информации в виде лекций, вебинаров и других аудиозаписей, 
которые могут быть использованы студентами в учебных целях. Однако часто у нас просто не хватает времени, чтобы прослушать 
или просмотреть все эти материалы.В целом, этот продукт предоставляет студентам удобный и эффективный способ преобразования 
аудиозаписей в текст, улучшая доступность, навигацию и анализ учебных материалов. Он поможет студентам сэкономить время и повысить 
эффективность своего обучения. Перевод аудиозаписей в текстовый формат позволяет нам: 
   
    Упростить навигацию по материалу. 
    Суммировать и конспектировать информацию автоматически. 
    Переводить текст на другой язык. 
    Предоставлять доступ к информации людям с нарушениями слуха. 
    Сравнивать и объединять информацию из разных источников. 
    Кроме того, некоторым людям проще воспринимать информацию в текстовом формате, чем в аудиоформате.  

