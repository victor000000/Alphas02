# 0.0.3 local release review — November 7, 2026

No previous declared version; establish 0.0.3 for this owned educational-notebook
deliverable. It is not a brain_work runtime dependency.

Design/self-review: notebook exercise exemptions are keyed by Colab metadata id.
Duplicate ids previously reused one exemption and collapsed into the inventory
set. Reject repeated code-cell metadata ids per notebook. Allow missing metadata
ids for ordinary cells, preserve notebook bytes and existing exercise inventory.

Implement a synthetic duplicate-exercise regression and retain the existing video
termination tests. Run `.venv/bin/python scripts/check_notebooks.py` and
`.venv/bin/python -m unittest discover -s tests -v`. Final results are recorded in
the brain_work release report. No notebook execution, downloads, training or
Hub uploads are part of validation. Full historical runtime compatibility remains
unverified. No deployment or publication is performed.
