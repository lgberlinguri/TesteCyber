import assemblyai as aai

# Configura a chave da API
aai.settings.api_key = "ef4f0ee3ed054842a2170984045bd0e1"

transcriber = aai.Transcriber()

# Usando um arquivo de áudio local na pasta Downloads
audio_file = r"C:\Users\Usuario\Downloads\Snaptik.app_7237866240608308482.mp4"  # Substitua pelo nome correto do seu arquivo

# Configurações para a transcrição, incluindo rótulos de falantes
config = aai.TranscriptionConfig(speaker_labels=True)

# Transcreve o arquivo de áudio
transcript = transcriber.transcribe(audio_file, config)

# Verifica se houve um erro na transcrição
if transcript.status == aai.TranscriptStatus.error:
    print(f"Transcrição falhou: {transcript.error}")
    exit(1)

# Exibe o texto da transcrição
print(transcript.text)

# Exibe cada fala e o respectivo falante
for utterance in transcript.utterances:
    print(f"Falante {utterance.speaker}: {utterance.text}")


