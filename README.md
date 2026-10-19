# Voipy

A Python library for connecting telephony systems to real-time AI voice agents.

> **Status: pre-alpha.** Nothing works end to end yet. The first target is a single path:
> **Asterisk (ARI) → OpenAI Realtime**. Other PBXs and providers come after that path works.

## Target API

This is the API voipy is being built toward. It is the spec for the code, **not implemented yet**.

```python
from voipy import Voipy
from voipy.telephony.asterisk import AsteriskAdapter
from voipy.providers.openai import OpenAIRealtime

app = Voipy(
    adapter=AsteriskAdapter(
        url="http://localhost:8088",
        app="voipy",
        user="asterisk",
        password="secret",
    ),
    # One provider per call, so each call gets its own AI session.
    provider_factory=lambda: OpenAIRealtime(
        api_key="sk-...",
        instructions="You are a friendly support agent.",
    ),
)


@app.on_call
async def handle(call):
    await call.answer()
    await call.run_agent()  # returns when the call ends


app.run()
```

What this implies for the design:

- `Voipy` owns the adapter's event loop and starts one session per incoming call.
- `call` wraps one channel: `answer()`, `hangup()`, `transfer(destination)`, `run_agent()`.
- `run_agent()` streams audio both ways and stops AI playback when the caller interrupts.
- Hanging up from either side cleans up every task and connection for that call.

## Roadmap

1. Foundation: packaging, lint, type-check, tests, CI.
2. Core contracts: audio frame type, `TelephonyAdapter` / `MediaTransport` / `VoiceProvider` protocols, events, session state machine.
3. Audio pipeline, tested with fake adapters and providers.
4. First real path: Asterisk ARI + OpenAI Realtime, with a runnable example.
5. Hardening: timeouts, reconnects, latency metrics.
6. Later: more providers, FreeSWITCH.

## Development

Requires Python 3.11+.

```bash
pip install -e ".[dev]"
ruff check . && ruff format --check . && mypy && pytest
```
