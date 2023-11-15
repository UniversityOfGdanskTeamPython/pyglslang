from pathlib import Path

THIS_DIR = Path(__file__).parent

def get_glslang_executable_path() -> Path:
    """Get files starting with glslang."""
    all_files_starting_with_glslang = THIS_DIR.glob("glslang*")
    return next(all_files_starting_with_glslang)