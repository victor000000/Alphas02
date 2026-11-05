# Alphas02

Legacy reinforcement-learning course notebooks for LunarLander, Q-learning
(FrozenLake and Taxi), and Unity ML-Agents/Huggy.

Run the credential-free checks locally with Python 3.10 or 3.12:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-ci.txt
.venv/bin/python scripts/check_notebooks.py
.venv/bin/python -m unittest discover -s tests -v
```

GitHub Actions runs the same checks on pushes and pull requests. It validates
the notebook schema, compiles Python cells after IPython syntax transformation,
validates the two embedded ML-Agents YAML configurations, and tests the video
helper's termination behavior. Eight intentionally incomplete exercise cells
are explicitly inventoried in `scripts/check_notebooks.py`; their solution
cells are syntax checked. Remove an exercise exemption when completing it.

These checks do not execute whole notebooks or verify training results. The
original notebooks use Colab shell commands, runtime restarts, GPU/display
setup, external downloads, historical package/API versions, long training
runs, and optional Hugging Face authentication/uploads. Their runtime setup
requires a separate compatibility review before use on a current environment.
CI dependencies are validation tools, not a training environment. There is no
deployment or model publication pipeline; Hub uploads remain manual.
