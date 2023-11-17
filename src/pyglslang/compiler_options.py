from typing import Optional

class CompilerOptions:
    def __init__(self,first_glslang_option: Optional[bool]) -> None:
        pass
    def get_executable_params(self) -> list[str]:
        """Get parameters that will be executed."""
        params: list[str] = ["glslang"]
        if self.cascading_errors is not None:
            params.append("-C")
        if self.define_preprocessor_macro is not None:
            params.append("-D")
        if self.preprocessed_glsl is not None:
            params.append("-E")
        if self.opengl is not None:
            params.append("-G")
        if self.human_readable is not None:
            params.append("-H")
        if self.dir_to_search_path is not None:
            params.append("-I")
        if self.optimization_disabled is not None:
            params.append("-Od")
        if self.optimize_spirv is not None:
            params.append("-Os")
        if self.specify_stage is not None:
            params.append("-S")
        if self.undefine_preprocessor_macro is not None:
            params.append("-U")
        if self.vulkan is not None:
            params.append("-V")
        if self.configuration_dump is not None:
            params.append("-c")
        if self.desktop is not None:
            params.append("-d")
        if self.entrypoint is not None:
            params.append("-e")
        if self.debug is not None:
            params.append("-g")
        if self.usage_message is not None:
            params.append("-h")
        if self.intermediate_tre is not None:
            params.append("-i")
        if self.link_input is not None:
            params.append("-l")
        if self.memory_leak is not None:
            params.append("-m")
        if self.binary_to_file is not None:
            params.append("-o")
        if self.dump_reflection_query is not None:
            params.append("-q")
        if self.silence_syntax is not None:
            params.append("-s")
        if self.multi_threaded is not None:
            params.append("-t")
        if self.version is not None:
            params.append("-v")
        if self.binary_to_hexadecimal is not None:
            params.append("-x")
        if self.auto_map_binding is not None:
            params.append("--amb")
        if self.auto_map_locations is not None:
            params.append("--aml")
        if self.client is not None:
            params.append("--client")
        if self.flatten_uniform_arrays is not None:
            params.append("--fua")
        if self.hlsl_offsets is not None:
            params.append("--hlsl-offsets")
        if self.hlsl_iomap is not None:
            params.append("--hlsl-iomap")
        if self.keep_uncalled is not None:
            params.append("--ku")
        if self.no_storage_format is not None:
            params.append("--nsf")
        if self.relaxed_errors is not None:
            params.append("--r")
        if self.resource_set_binding is not None:
            params.append("--rsb")
        if self.shift_image_binging is not None:
            params.append("--sib")
        if self.shift_sampler_binding is not None:
            params.append("--ssb")
        if self.shift_ssbo_binding is not None:
            params.append("--sbb")
        if self.shift_texture_binding is not None:
            params.append("--stb")
        if self.shift_uav_binding is not None:
            params.append("--suavb")
        if self.shift_ubo_binding is not None:
            params.append("--sub")
        if self.source_entrypoint is not None:
            params.append("--sep")
        if self.standard_input is not None:
            params.append("--stdin")
        if self.suppress_warnings is not None:
            params.append("-w")
        if self.target_env is not None:
            params.append("--target-env")
        if self.variable_name is not None:
            params.append("--vn")
        return params
