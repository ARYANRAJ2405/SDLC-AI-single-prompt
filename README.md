# BRD Agent Single Node

Run:

```bash
python brd_agent_single\brd_agent_single.py --inputs "brd_agent_2\meeting_transcript_short.txt"
```

Optional outputs:

```bash
python brd_agent_single\brd_agent_single.py --inputs "brd_agent_2\meeting_transcript_short.txt" --output-md "brd_agent_single\brd_single.md" --output-docx "brd_agent_single\brd_single.docx"
```

Required environment variables:

- `CLIENT_ID`
- `CLIENT_SECRET`
- Optional: `MODEL_AS_A_SERVICE_MODEL` (default: `gpt-5`)
