# Text-to-Speech (TTS), Language Translation, and YouTube Audio Analysis

This project integrates several key functionalities:
1. **Text-to-Speech (TTS)**: Converts text into speech with emotional inflection.
2. **Language Translation (LT)**: Translates text from one language to another (e.g., from English to Malayalam).
3. **YouTube Audio Analysis (Youtube)**: Downloads audio from YouTube, transcribes it, translates the transcribed text, and analyzes the audio features.

## Project Overview

The project is divided into three main components:

### 1. Text-to-Speech (TTS) - `TTS.py`

The `TTS.py` script converts given text into speech using the **SpeechT5** model with emotional inflection.

- **Key Features**:
  - Text chunking for long text inputs.
  - Emotion detection and inflection application to each chunk of text.
  - Use of `SpeechT5Processor` and `SpeechT5ForTextToSpeech` from the Hugging Face library.
  - Uses **Hifi-GAN** as a vocoder for generating high-quality audio.
  
- **How it works**:
  1. Text is split into smaller chunks if it exceeds the maximum length.
  2. Each chunk is processed to detect the emotion and convert it to speech.
  3. Emotional inflection is applied, and the speech is generated.
  4. The generated speech is saved as a `.wav` file.

### 2. Language Translation (LT) - `LT.py`

The `LT.py` script translates text from any source language to a target language (default: Malayalam) using **GoogleTranslator** from the `deep_translator` package.

- **Key Features**:
  - Reads HTML content, removes HTML tags.
  - Splits large texts into smaller chunks for efficient translation.
  - Saves the translated text to a `.txt` file.

- **How it works**:
  1. Text is extracted from an HTML file by removing all HTML tags.
  2. The text is split into chunks of manageable size (default: 5000 characters).
  3. Each chunk is translated to the target language using **GoogleTranslator**.
  4. The translated content is saved to `TranslatedText.txt`.

### 3. YouTube Audio Analysis - `Youtube.py`

The `Youtube.py` script performs several tasks:
- Downloads audio from a given YouTube video.
- Uses **Whisper** for transcription of the audio to text.
- Translates the transcribed text into a target language.
- Analyzes various features of the audio such as prosody, clarity, and technical features.

- **Key Features**:
  - Downloads audio from YouTube using `yt-dlp`.
  - Transcribes audio to text using **Whisper**.
  - Translates the transcription using **GoogleTranslator**.
  - Analyzes audio features such as pitch, energy variation, and signal-to-noise ratio.
  - Generates a detailed audio analysis report.

- **How it works**:
  1. Downloads the audio from YouTube and saves it as a `.wav` file.
  2. Transcribes the audio using **Whisper**.
  3. Translates the transcription into the target language.
  4. Analyzes the audio for pitch range, energy variation, speech clarity, and technical features.
  5. Generates and saves a comprehensive report with scores for prosody, clarity, and technical features.

## Data and Models Used

### Text-to-Speech (TTS) Model

- **Model**: The TTS system uses **SpeechT5**, a pre-trained model from Hugging Face’s `transformers` library.
- **Emotion Detection**: The text is analyzed for emotions using custom methods and adjusted to add emotional inflection during speech synthesis.
  
#### Data Used for Training

- **Data Source**: (Explain the dataset you used to train or fine-tune the model, if applicable.)
- **Preprocessing**: (Describe any preprocessing done on the data before training.)

### Whisper Model for Audio Transcription

- **Model**: **Whisper**, an automatic speech recognition (ASR) model from OpenAI, is used to transcribe the downloaded audio from YouTube.
- **Language Support**: Whisper supports transcription in multiple languages, which is useful for audio analysis and translation.

#### Data Used for Training

- **Data Source**: (Explain the dataset used to train or fine-tune the Whisper model, if applicable.)
- **Preprocessing**: (Describe any preprocessing done on the data before training.)

### GoogleTranslator for Language Translation

- **Model**: **GoogleTranslator** from the `deep_translator` package is used for text translation.
- **Languages Supported**: The default target language is Malayalam (`ml`), but you can customize it to any other language supported by Google Translate.

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rahul-144/audio_translation_analysis.git
   cd audio_translation_analysis
2. **Install Dependencies**: Ensure you have Python 3.x installed. Create a virtual environment and install the dependencies:

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # For Linux/macOS
  .\venv\Scripts\activate  # For Windows
  pip install -r requirements.txt

3. **Run Text-to-Speech (TTS)**:

  ```bash
  python TTS.py
  
4. **Run Language Translation (LT)**:

  ```bash
  python LT.py

5. ** Run YouTube Audio Analysis**: Modify the video_url in the main() function and run:

  ```bash
  python Youtube.py

6.The results will be saved in the appropriate output files:

speech.wav for TTS.
TranslatedText.txt for language translation.
audio_analysis_report.txt for YouTube audio analysis.
License
This project is licensed under the MIT License.
