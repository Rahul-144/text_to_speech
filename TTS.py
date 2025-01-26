
import torch
import soundfile as sf
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import numpy as np
import re
from nltk.tokenize import sent_tokenize
from data_preparation import convert_year_range_to_words, remove_html_tags
from process import emotion, add_emotional_inflection
def text_to_speech(text, processor, model, vocoder, speaker_embeddings, sr, max_length=200):
    """Convert text to speech with emotional inflection."""
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_length:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    # Detect emotion for each chunk
    detected_emotions = [emotion(chunk)[0] for chunk in chunks]
    
    speech_segments = []
    for chunk, chunk_emotion in zip(chunks, detected_emotions):
        # Replace year ranges with words
        chunk_text = re.sub(r'\d+(-\d+)?', convert_year_range_to_words, chunk)
        
        # Prepare input
        inputs = processor(text=chunk_text, return_tensors="pt")
        
        with torch.no_grad():
            # Generate speech
            segment = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)
            segment_np = segment.numpy().squeeze()
            
            # Apply emotional inflection
            adjusted_segment = add_emotional_inflection(segment_np, chunk_emotion, sr)
            speech_segments.append(adjusted_segment)
    
    return np.concatenate(speech_segments, axis=0)
def main():
    # Load text file
    file_path = "/content/Data.html"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    
    # Preprocess text
    clean_text = remove_html_tags(content)
    
    # Load TTS models
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    
    # Load speaker embeddings
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embeddings = torch.tensor(embeddings_dataset[7266]["xvector"]).unsqueeze(0)
    
    # Generate speech with emotional inflection
    speech = text_to_speech(clean_text, processor, model, vocoder, speaker_embeddings, sr=vocoder.config.sampling_rate)
    
    # Save the speech file
    sf.write("speech.wav", speech, samplerate=vocoder.config.sampling_rate)
    print("Speech generation complete. Output saved as speech.wav")

if __name__ == "__main__":
    main()