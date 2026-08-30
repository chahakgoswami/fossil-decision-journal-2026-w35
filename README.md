# Fossil — A Personal Decision Journal CLI

A CLI tool to log decisions, predict outcomes, and later review how accurate your forecasts were.

**Language:** python

## 7-day build plan

- [ ] Day 1: Scaffold the project with a SQLite database and a `fossil log` command that accepts a decision description and stores it with a timestamp and unique ID.
- [ ] Day 2: Add a `--prediction` flag to `fossil log` so users can attach an expected outcome and a confidence percentage (0-100) to each decision.
- [ ] Day 3: Implement `fossil list` to display all logged decisions in a readable table using the `rich` library, showing ID, date, description, and prediction.
- [ ] Day 4: Add `fossil review <id>` to mark a past decision as resolved by recording the actual outcome and whether the prediction was correct.
- [ ] Day 5: Build `fossil stats` that computes and prints calibration metrics: overall accuracy rate and a breakdown of accuracy grouped by confidence bucket (e.g. 60-70%, 70-80%).
- [ ] Day 6: Add `fossil export --format csv` and `--format json` to dump all decisions and outcomes to a file for use in spreadsheets or further analysis.
- [ ] Day 7: Implement `fossil reflect` which uses a local template to print a weekly digest of unreviewed decisions older than 7 days, reminding the user to follow up.


