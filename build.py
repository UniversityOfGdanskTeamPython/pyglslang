"""Build script for epseon_backend package."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


class Builder:
    """Class responsible for building epseon_backend binaries."""

    def __init__(self) -> None:
        """Initialize builder object."""
        self.repo_path = Path(__file__).parent
        self.prepare_submodules()

    def prepare_submodules(self) -> None:
        """Prepare dependency submodules."""
        self.git("submodule", "init")
        self.git(
            "-C",
            f"{self.repo_path.as_posix()}/external/glslang",
            "fetch",
            "--tags",
        )
        self.git(
            "-C",
            f"{self.repo_path.as_posix()}/external/glslang",
            "checkout",
            "13.1.1",
        )
        self.python(
            "./update_glslang_sources.py",
            cwd=self.repo_path / "external" / "glslang",
        )

    def git(self, *arg: str) -> None:
        """Run git command."""
        try:
            r = subprocess.run(
                args=[
                    "git",
                    *arg,
                ],
                cwd=self.repo_path.as_posix(),
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            sys.stdout.write(e.stdout.decode("utf-8"))
            sys.stderr.write(e.stderr.decode("utf-8"))
            raise
        else:
            sys.stdout.write(r.stdout.decode("utf-8"))
            sys.stderr.write(r.stderr.decode("utf-8"))

    def python(self, *arg: str, cwd: Path) -> None:
        """Run python command."""
        try:
            r = subprocess.run(
                args=[
                    sys.executable,
                    *arg,
                ],
                executable=sys.executable,
                cwd=cwd.as_posix(),
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            sys.stdout.write(e.stdout.decode("utf-8"))
            sys.stderr.write(e.stderr.decode("utf-8"))
            raise
        else:
            sys.stdout.write(r.stdout.decode("utf-8"))
            sys.stderr.write(r.stderr.decode("utf-8"))

    def build(self) -> None:
        """Build extension module."""
        self.cmake("-S", ".", "-B", "build", "-DCMAKE_BUILD_TYPE=Release")
        self.cmake(
            "--build",
            "build",
            "--target",
            "glslang-standalone",
            "--config",
            "Release",
            "-j32",
        )
        shutil.copy("external/glslang/build/StandAlone/glslang", "src/pyglslang/_bin")

    def cmake(self, *arg: str) -> None:
        """Run cmake command. If fails, raises CalledProcessError."""
        try:
            r = subprocess.run(
                executable=sys.executable,
                args=[
                    sys.executable,
                    "-c",
                    "import cmake;cmake.cmake()",
                    *arg,
                ],
                cwd=(self.repo_path / "external" / "glslang").as_posix(),
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            sys.stdout.write(e.stdout.decode("utf-8"))
            sys.stderr.write(e.stderr.decode("utf-8"))
            raise
        else:
            sys.stdout.write(r.stdout.decode("utf-8"))
            sys.stderr.write(r.stderr.decode("utf-8"))


Builder().build()
