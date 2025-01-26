import librosa
from transformers import pipeline
import numpy as np
def emotion(chunk):
    """Detect the predominant emotion for a text chunk."""
    classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
    
    model_outputs = classifier(chunk)
    highest_labels = [max(model_output, key=lambda x: x['score']) for model_output in model_outputs]
    
    # Return the emotion label with the highest score
    return highest_labels[0]['label'] if highest_labels else 'neutral'

def add_emotional_inflection(audio, emotion, sr):
    """Apply emotional inflection to audio based on emotion."""
    emotion_params = {
        'happy': {'pitch_shift': 4, 'speed_factor': 1.2, 'volume_factor': 1.5},
        'sad': {'pitch_shift': -4, 'speed_factor': 0.8, 'volume_factor': 0.7},
        'angry': {'pitch_shift': 5, 'speed_factor': 1.3, 'volume_factor': 2.0},
        'disappointment': {'pitch_shift': -2, 'speed_factor': 0.9, 'volume_factor': 0.8}
    }
    
    # Use default parameters for unknown emotions
    params = emotion_params.get(emotion, {'pitch_shift': 0, 'speed_factor': 1.0, 'volume_factor': 1.0})
    
    # Apply adjustments
    audio = librosa.effects.pitch_shift(audio, sr=sr, n_steps=params['pitch_shift'])
    audio = librosa.effects.time_stretch(audio, rate=params['speed_factor'])
    audio = np.clip(audio * params['volume_factor'], -1.0, 1.0)
    return audio