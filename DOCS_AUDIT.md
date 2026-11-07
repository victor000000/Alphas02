# Documentation audit — November 7, 2026

Version remains 0.0.3; documentation changes do not imply a new trained model or deployed service. README and DESIGN.md are current guides; RELEASE_REVIEW.md preserves dated 0.0.3 evidence unchanged. The docs checker validates owned Markdown inline local links/heading fragments without network or snippet execution. It excludes third-party/env/cache docs and does not check external URL availability, HTML/reference links or notebook Markdown automatically. A synthetic unittest covers missing target/anchor failures.

## Inventory and source review

All four standalone owned Markdown documents (README, DESIGN, release review and this audit) are covered. Instructional notebook Markdown was separately inventoried/reviewed: unit1 48 cells, unit2 60 cells, bonus-unit1 33 cells, **141 total**. All three notebooks remain byte-unchanged in this phase. They attribute Hugging Face Deep RL course material and discuss GPU/Colab, runtime crashes/restarts, historical Gymnasium/Stable-Baselines3 environments, package installation, virtual screens, Hub login/upload and Unity ML-Agents Python compatibility. README qualifies these as historical educational instructions, not verified current setup, performance, training duration or certification availability.

The bonus notebook's suggestion to rerun a first failing --resume command is retained as original teaching content, not endorsed as a safe recovery policy. Review actual checkpoint/error state first. Course certification reward thresholds, quoted training times and external model/game links were not refreshed. No historical student exercises/results were silently rewritten. Source schema/exemption/video-helper contracts were checked against scripts/check_notebooks.py and tests. There is no server/API, account configuration or CD pipeline to invent.

## Verification and limitations

Run `python scripts/check_docs.py`, `.venv/bin/python scripts/check_notebooks.py` and `.venv/bin/python -m unittest discover -s tests -v`. Final counts/results are in the publication manifest. Existing CI runs these on Python3.10/3.12. Validation dependencies are not a complete training environment. No notebook execution, package setup cell, GPU/Unity game, credential use or Hub upload was exercised. Notebook embedded HTML/external links and numerical learning quality remain unverified.
