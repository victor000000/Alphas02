# Alphas02

Version 0.0.3 is a preserved reinforcement-learning course notebook collection: LunarLander, FrozenLake/Taxi Q-learning and Unity ML-Agents/Huggy. It is not a BRAIN alpha engine or a deployable trained model. Notebook exercises and original course material remain intact.

## Validate without training

Use Python 3.10 or 3.12, the versions in hosted CI:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-ci.txt
.venv/bin/python scripts/check_docs.py
.venv/bin/python scripts/check_notebooks.py
.venv/bin/python -m unittest discover -s tests -v
```

Installation downloads validation tools, not training dependencies. Validation does not execute whole notebooks, use credentials, contact model hubs or create videos. Run from the repository root. CI runs these checks on pushes, pull requests and manual dispatch.

## What is checked

The notebook checker reads original notebooks without rewriting/upgrading them, validates schema and compiles transformed Python cells. Eight intentionally incomplete exercises and two ML-Agents YAML cells are inventoried by path and Colab metadata ID. Completing an exercise requires removing its exemption. Missing/stale exemptions and duplicate code-cell metadata IDs fail validation. Video-helper tests extract the actual function and use synthetic environments to verify termination/truncation handling.

See [Design and maintenance](DESIGN.md) for source/data contracts and limitations, [release review](RELEASE_REVIEW.md) for the dated 0.0.3 change, and [license](LICENSE) for repository licensing.

## Running the educational material

Notebooks contain Colab shell commands, runtime restarts, package pins, external downloads, long training, display/GPU setup and optional Hugging Face login/uploads. Do not use import or whole-notebook execution as a health check. A current training environment must be reviewed separately per notebook; `requirements-ci.txt` deliberately does not claim to reproduce it. This documentation phase did not run training, authentication, downloads or uploads.

No CI deployment/model publication or standing schedule is configured. Checkpoint/Q-table files produced by training are model data, not source-validation evidence. Keep tokens and personal credentials out of notebooks, saved outputs and Git.
