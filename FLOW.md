# FLOW.md

1. `python3 main.py` validates the entry text against the gate
   (UTF-8, 1–60 characters, not only whitespace).
2. The program writes the single deterministic job title to
   `/output/entry.txt` (no trailing newline).
3. Verify: read `/output/entry.txt` back, count characters, sha256.
4. A blind judge compares the title two at a time against other
   entries and picks the weirder, funnier one; best win rates take
   the reward.
