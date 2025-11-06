import assemblyai as aai


def get_transcription(audio):
    config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.universal)

    transcript = aai.Transcriber(config=config).transcribe(audio)

    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")

    return transcript.text