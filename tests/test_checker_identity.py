"""An exercise exemption must not be reusable by duplicate cell identity."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import nbformat


class CheckerIdentityTests(unittest.TestCase):
    def test_duplicate_exercise_id_is_rejected(self):
        path = Path(__file__).resolve().parents[1] / "scripts/check_notebooks.py"
        spec = importlib.util.spec_from_file_location("notebook_checker_test", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            notebooks = root / "notebooks"
            notebooks.mkdir()
            cells = [nbformat.v4.new_code_cell("x =", metadata={"id": "exercise"}) for _ in range(2)]
            (notebooks / "exercise.ipynb").write_text(
                json.dumps(nbformat.v4.new_notebook(cells=cells)), encoding="utf-8"
            )
            with patch.object(module, "ROOT", root), patch.object(module, "EXERCISES", {
                "exercise.ipynb": {"exercise"}
            }), patch.object(module, "YAML_CELLS", {}):
                with self.assertRaisesRegex(ValueError, "Duplicate code-cell metadata id"):
                    module.main()
