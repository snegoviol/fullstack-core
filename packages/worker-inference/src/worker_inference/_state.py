# ==================================================================================================
# 
# Copyright (c) 2026 Ilya Snegov
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Originally from Human Pose Estimation Service 
# (https://github.com/snegoviol/pose-estimation-service).
# Modified for Full-Stack Core to suit the needs of this project.
# 
# ==================================================================================================
# packages/worker-inference/src/worker_inference/_state.py
# ==================================================================================================

from transformers import Qwen3_5ForCausalLM, AutoTokenizer

# ==================================================================================================

model: Qwen3_5ForCausalLM | None = None
"""
Process-local model instance shared across all tasks in this worker.

Holds the eagerly loaded Qwen3_5ForCausalLM after successful worker startup.
None until main() in main.py completes initialization. Each worker process
maintains its own isolated instance of this module; no model state is shared
across processes. All tasks in this process read from this reference via
get_model().
"""

# ==================================================================================================

tokenizer: AutoTokenizer | None = None
"""
Process-local tokenizer instance shared across all tasks in this worker.

Loaded from the same model_path as the model during worker startup and held
for the lifetime of the process. None until main() in main.py completes
initialization.
"""

# ==================================================================================================
