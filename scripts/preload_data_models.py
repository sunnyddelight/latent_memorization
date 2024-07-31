from datasets import load_dataset
from transformers import LlamaTokenizer, LlamaForCausalLM
import os

i = int(os.environ.get("ID"))
tokenizer = LlamaTokenizer.from_pretrained("LLM360/Amber", revision=f"ckpt_{i}", cache_dir=f"/om/user/sunnyd/amber_cache/")
model = LlamaForCausalLM.from_pretrained("LLM360/Amber", revision=f"ckpt_{i}", cache_dir=f"/om/user/sunnyd/amber_cache/", device_map='cpu', low_cpu_mem_usage=True)
