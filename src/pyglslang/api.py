import subprocess
from test.test_glsl import test_glsl
import tempfile


def compile_shader(options: CompilerOptions) -> CompilerResults:
    """Compile shader."""
    params = options.get_executable_params()
    result = subprocess.run(params, capture_output=True)
    temp = tempfile.NamedTemporaryFile(name="temp_result", dir="~/pyglslang/src/pyglslang")
    try:
        temp.write(result)
    finally:
        temp.close()

