import os
import glob
import subprocess
import argparse
from pathlib import Path

def check_ffmpeg():
    """Проверяет наличие ffmpeg в системе."""
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def process_audio(input_file, output_file):
    """
    Обрабатывает аудиофайл через ffmpeg для СВ диапазона (NRSC-подобный фильтр).
    
    Цепочка обработки (ffmpeg filters):
    1. aresample=16000 - Понижаем частоту дискретизации до 16кГц (хватит для АМ с запасом).
    2. equalizer=f=3500:width_type=h:width=2000:g=8 - Pre-emphasis: поднимаем высокие частоты (2.5-4.5 кГц) на 8 дБ.
    3. lowpass=f=5000:p=2 - Жесткий фильтр: отрезаем все что выше 5 кГц (чтобы не было радиопомех соседним каналам).
    4. acompressor=threshold=-15dB:ratio=4:attack=5:release=50:makeup=5 - Компрессор: вытягиваем тихие звуки, жмем пики.
    5. volume=1.5 - Общее усиление громкости (лимитирование пиков сделает компрессор).
    """
    
    # Сложный фильтр ffmpeg
    audio_filter = "aresample=16000,equalizer=f=3500:width_type=h:width=2000:g=8,lowpass=f=5000:p=2,acompressor=threshold=-15dB:ratio=4:attack=5:release=50:makeup=5,volume=1.5"
    
    cmd = [
        'ffmpeg',
        '-y',               # Перезаписывать выходной файл
        '-i', input_file,   # Входной файл
        '-af', audio_filter,# Аудиофильтр
        '-ac', '1',         # Моно (АМ радио все равно моно, экономим место)
        '-c:a', 'libmp3lame',# Кодек MP3 (DFPlayer его отлично читает)
        '-b:a', '64k',      # Битрейт 64 kbps (для 5 кГц моно этого за глаза)
        '-ar', '16000',     # Частота дискретизации 16 кГц
        output_file
    ]
    
    try:
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(f"[УСПЕХ] Обработан: {Path(input_file).name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ОШИБКА] Не удалось обработать {Path(input_file).name}: {e.stderr.decode('utf-8', errors='ignore')}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Скрипт психоакустической обработки музыки для АМ-радиовещания (СВ диапазон).")
    parser.add_argument('-i', '--input', default='./music_in', help='Папка с исходными файлами (MP3, WAV, FLAC, M4A).')
    parser.add_argument('-o', '--output', default='./music_out', help='Папка для готовых файлов (для загрузки на MicroSD DFPlayer).')
    
    args = parser.parse_args()
    
    input_dir = Path(args.input)
    output_dir = Path(args.output)
    
    print("="*60)
    print(" АМ-РАДИО ВТВ: Аудиопроцессор (NRSC Pre-emphasis & Compression)")
    print("="*60)
    
    if not check_ffmpeg():
        print("[ОШИБКА] FFMPEG не найден в системе!")
        print("Скачайте его с https://ffmpeg.org/download.html и добавьте в системную переменную PATH.")
        print("Или установите через пакетный менеджер (apt install ffmpeg / choco install ffmpeg).")
        return

    if not input_dir.exists():
        print(f"Создаю входную папку: {input_dir}")
        input_dir.mkdir(parents=True, exist_ok=True)
        print("Положите в эту папку вашу музыку и запустите скрипт снова.")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Ищем аудиофайлы
    extensions = ('*.mp3', '*.wav', '*.flac', '*.m4a', '*.ogg')
    files = []
    for ext in extensions:
        files.extend(input_dir.rglob(ext))
        
    if not files:
        print(f"В папке {input_dir} не найдено аудиофайлов.")
        return
        
    print(f"Найдено файлов для обработки: {len(files)}\n")
    
    success_count = 0
    # DFPlayer любит имена файлов вида 0001.mp3, 0002.mp3 в корне, либо 01/001.mp3
    # Для простоты будем нумеровать файлы по порядку
    for idx, input_path in enumerate(files, start=1):
        # Генерируем имя вида 0001.mp3
        out_filename = f"{idx:04d}.mp3"
        out_path = output_dir / out_filename
        
        if process_audio(str(input_path), str(out_path)):
            success_count += 1
            
    print("="*60)
    print(f"Готово! Успешно обработано: {success_count}/{len(files)}")
    print(f"Готовые файлы лежат в папке: {output_dir.absolute()}")
    print("Теперь вы можете скопировать их в корень вашей MicroSD карты (FAT32) для DFPlayer.")
    print("="*60)

if __name__ == "__main__":
    main()
