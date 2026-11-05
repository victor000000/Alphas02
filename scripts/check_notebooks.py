"""Validate notebook structure and cell syntax without executing notebook code."""

import json
from pathlib import Path

import nbformat
import yaml
from IPython.core.inputtransformer2 import TransformerManager

ROOT = Path(__file__).resolve().parents[1]
# Existing course exercises intentionally contain incomplete Python assignments.
# Keys are stable Colab cell identifiers, not positional cell numbers.
EXERCISES = {
    "unit1/unit1.ipynb": {"nxI6hT1GE4-A", "yRpno0glsADy", "JPG7ofdGIHN8"},
    "unit2/unit2.ipynb": {
        "y3ZCdluj3k0l", "rCddoOXM3UQH", "E3SCLmLX5bWG",
        "6Bj7x3in3_Pq", "paOynXy3aoJW",
    },
}
YAML_CELLS = {"bonus-unit1/bonus-unit1.ipynb": {"loQ0N5jhXW71", "jXte_A1OQ8Be"}}


def main():
    paths = sorted((ROOT / "notebooks").rglob("*.ipynb"))
    if not paths:
        raise ValueError("No notebooks found")
    transformer = TransformerManager()
    total = 0
    seen_exercises, seen_yaml = set(), set()
    for path in paths:
        # Validate original v4.0 documents without upgrading or rewriting them.
        notebook = nbformat.from_dict(json.loads(path.read_text(encoding="utf-8")))
        nbformat.validate(notebook)
        relative = path.relative_to(ROOT / "notebooks").as_posix()
        for index, cell in enumerate(notebook.cells):
            if cell.cell_type != "code":
                continue
            total += 1
            source = "".join(cell.source)
            cell_id = cell.metadata.get("id")
            location = f"{relative}:cell {index + 1} ({cell_id})"
            if cell_id in YAML_CELLS.get(relative, set()):
                config = yaml.safe_load(source)
                if not isinstance(config, dict) or "Huggy" not in config.get("behaviors", {}):
                    raise ValueError(f"Invalid ML-Agents configuration: {location}")
                seen_yaml.add((relative, cell_id))
                continue
            try:
                compile(transformer.transform_cell(source), location, "exec")
            except SyntaxError:
                if cell_id not in EXERCISES.get(relative, set()):
                    raise
                seen_exercises.add((relative, cell_id))
            else:
                if cell_id in EXERCISES.get(relative, set()):
                    raise ValueError(f"Completed exercise: remove its exemption: {location}")
    expected_exercises = {(path, cell) for path, cells in EXERCISES.items() for cell in cells}
    expected_yaml = {(path, cell) for path, cells in YAML_CELLS.items() for cell in cells}
    if seen_exercises != expected_exercises or seen_yaml != expected_yaml:
        raise ValueError("A declared exercise/YAML cell is missing; update the explicit inventory")
    print(f"Validated {len(paths)} notebooks, {total} code cells: "
          f"{len(seen_exercises)} incomplete exercises, {len(seen_yaml)} YAML configurations")


if __name__ == "__main__":
    main()
