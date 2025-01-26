from deep_translator import GoogleTranslator
from data_preparation import remove_html_tags
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
def split_text(text, max_length=5000):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

file_path = 'Data2.html'

try:
    # Read the HTML file
    logging.info(f"Reading file: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    logging.error(f"Error: File '{file_path}' not found.")
    exit(1)
except Exception as e:
    logging.error(f"An error occurred while reading the file: {e}")
    exit(1)

try:
    # Remove HTML tags
    logging.info("Removing HTML tags...")
    to_translate = remove_html_tags(content)
    
    # Translate text
    logging.info("Translating text to Malayalam...")
    chunks = split_text(to_translate)
    translated_chunks = [GoogleTranslator(source='auto', target='ml').translate(chunk) for chunk in chunks]
    translated = " ".join(translated_chunks)
    
    # Save translated output
    output_path = 'TranslatedText.txt'
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(translated)
    logging.info(f"Translated text saved to {output_path}")

except Exception as e:
    logging.error(f"An error occurred during translation: {e}")
