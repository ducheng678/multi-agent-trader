"""Market agent modules split out from the legacy unified entrypoint."""

from pathlib import Path

from dotenv import load_dotenv




load_dotenv(Path(__file__).resolve().parents[1] / ".env")
