"""Exercise the actual notebook helper with small, offline environment doubles."""

import ast
import json
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import Mock


def load_record_video():
    path = Path(__file__).resolve().parents[1] / "notebooks/unit2/unit2.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    functions = []
    for cell in notebook["cells"]:
        source = "".join(cell["source"])
        if cell["cell_type"] == "code" and source.startswith("def record_video("):
            functions.append(ast.parse(source))
    if len(functions) != 1:
        raise AssertionError("Expected exactly one record_video helper")
    writer = Mock()
    namespace = {
        "np": SimpleNamespace(argmax=lambda values: 0, array=lambda value: value),
        "random": SimpleNamespace(randint=lambda low, high: 0),
        "imageio": SimpleNamespace(mimsave=writer),
    }
    exec(compile(functions[0], str(path), "exec"), namespace)
    return namespace["record_video"], writer


class RecordVideoTests(unittest.TestCase):
    def test_stops_on_either_environment_end_signal(self):
        for terminated, truncated in [(True, False), (False, True), (True, True)]:
            with self.subTest(terminated=terminated, truncated=truncated):
                record_video, writer = load_record_video()
                env = Mock()
                env.reset.return_value = (0, {})
                env.render.return_value = "frame"
                # A second step after termination raises instead of hanging a test.
                env.step.side_effect = [(0, 1.0, terminated, truncated, {}),
                                        AssertionError("Stepped after episode ended")]
                record_video(env, [[0]], "replay.mp4", fps=2)
                self.assertEqual(env.step.call_count, 1)
                writer.assert_called_once_with("replay.mp4", ["frame", "frame"], fps=2)

    def test_continues_until_episode_ends(self):
        record_video, writer = load_record_video()
        env = Mock()
        env.reset.return_value = (0, {})
        env.render.return_value = "frame"
        env.step.side_effect = [(0, 0.0, False, False, {}), (0, 1.0, False, True, {})]
        record_video(env, [[0]], "replay.mp4")
        self.assertEqual(env.step.call_count, 2)
        writer.assert_called_once_with("replay.mp4", ["frame"] * 3, fps=1)
