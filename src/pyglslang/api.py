import subprocess
from test.test_glsl import test_glsl


def compile_shader(options: CompilerOptions) -> CompilerResults:
    """Compile shader."""
    params = options.get_executable_params()
    subprocess(test_glsl)
