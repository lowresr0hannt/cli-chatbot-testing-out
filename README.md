# CLI Chatbot Testing Out

A simple Python terminal chatbot that talks to a local [Ollama](https://ollama.com/) server.

The default model is `mistral`, which is a strong general-purpose local chatbot model.

## Requirements

- Python 3.10 or newer
- Ollama installed and running
- The `mistral` model downloaded locally

## Setup

Install Ollama from the Ollama website, then pull the default model:

```bash
ollama pull mistral
```

You can test Ollama directly with:

```bash
ollama run mistral
```

## Run the chatbot

From this project folder, run:

```bash
python3 chatbot.py
```

Type a message and press Enter. Type `exit` or `quit` to stop.

## Use a different model

Set `OLLAMA_MODEL` before running the script:

```bash
OLLAMA_MODEL=gemma:2b python3 chatbot.py
```

Other local model ideas:

- `mistral` — general use, recommended default
- `gemma:2b` — lighter model for lower-RAM machines
- `llama3.2` — fast responses on many systems

## Troubleshooting

If you see a connection error, make sure Ollama is running and the model is installed:

```bash
ollama pull mistral
```
