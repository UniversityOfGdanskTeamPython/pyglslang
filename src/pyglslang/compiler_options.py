from typing import Optional


class CompilerOptions:
    def __init__(self,first_glslang_option: Optional[bool]) -> None:
        pass
    def get_executable_params(self) -> list[str]:
        """Get parameters that will be executed."""
        params: list[str] = []
        if self.first_glslang_option is not None:
            params.append("--first-glslang-option")
        return params