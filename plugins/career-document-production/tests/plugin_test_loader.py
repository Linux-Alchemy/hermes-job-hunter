"""Load the plugin package under an import-safe test name."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

PLUGIN = Path(__file__).resolve().parents[1]
PACKAGE = "career_document_production_testpkg"


def load_tools() -> ModuleType:
    if PACKAGE not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            PACKAGE,
            PLUGIN / "__init__.py",
            submodule_search_locations=[str(PLUGIN)],
        )
        if spec is None or spec.loader is None:
            raise RuntimeError("Could not load plugin package")
        module = importlib.util.module_from_spec(spec)
        sys.modules[PACKAGE] = module
        spec.loader.exec_module(module)
    return sys.modules[f"{PACKAGE}.tools"]
