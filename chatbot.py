#!/usr/bin/env python3
"""A simple terminal chatbot powered by Ollama."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "mistral")


def ask_ollama(messages: list[dict[str, str]]) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "messages": messages,
        "stream": False,
    }
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as error:
        raise RuntimeError(
            "Could not reach Ollama. Make sure Ollama is running and try: ollama pull mistral"
        ) from error

    message = result.get("message", {})
    return message.get("content", "").strip()


def main() -> int:
    print(f"CLI Chatbot Testing Out — using Ollama model: {OLLAMA_MODEL}")
    print("Type 'exit' or 'quit' to stop.\n")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful, concise terminal chatbot.",
        }
    ]

    while True:
        try:
            user_text = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return 0

        if not user_text:
            continue
        if user_text.lower() in {"exit", "quit"}:
            print("Goodbye!")
            return 0

        messages.append({"role": "user", "content": user_text})

        try:
            reply = ask_ollama(messages)
        except RuntimeError as error:
            print(f"Error: {error}")
            return 1

        if not reply:
            reply = "I did not receive a response from Ollama."

        print(f"Bot: {reply}\n")
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    sys.exit(main())
