import os
# One-liner entry (122 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "I did not eat your sock. I was conducting a thorough inspection of the laundry, and the sock confessed to being delicious."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
