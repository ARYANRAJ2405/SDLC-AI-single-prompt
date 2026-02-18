from __future__ import annotations

import argparse
from pathlib import Path
import sys

from dotenv import load_dotenv

# Load environment variables FIRST before importing other modules
load_dotenv()

# Add current directory to path so we can import local modules
_pkg_dir = Path(__file__).resolve().parent
if str(_pkg_dir) not in sys.path:
    sys.path.insert(0, str(_pkg_dir))

from config import Settings
from graph import build_graph
from models import BRDState


def parse_args() -> argparse.Namespace:
    settings = Settings()
    parser = argparse.ArgumentParser(description="Single-node BRD generation agent")
    parser.add_argument(
        "--inputs",
        nargs="+",
        required=True,
        help="Input files or directories containing transcripts and supporting documents",
    )
    parser.add_argument(
        "--output-md",
        default=str(Path(settings.default_output_dir) / "brd_single.md"),
        help="Path to save markdown BRD",
    )
    parser.add_argument(
        "--output-docx",
        default=str(Path(settings.default_output_dir) / "brd_single.docx"),
        help="Path to save BRD as .docx",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    graph = build_graph().compile()
    state = BRDState(
        inputs=args.inputs,
        output_markdown_path=args.output_md,
        output_docx_path=args.output_docx,
    )
    graph.invoke(state)


if __name__ == "__main__":
    main()
