from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path = 'test.pdf', language = 'en'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file = file_path, mode = 'rb')) as file:
            pages = [page.extract_text() for page in file.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text = text, lang = language, slow = False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!\n---Good day!---'

    else:
        return 'File doesnt exist, check the path!'

def main():
    tprint('PDF>>TO>>MP3', font = 'bulbhead')
    file_path = input('\nEnter file`s path: ')
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path = file_path, language = language))


if __name__ == '__main__':
    main()