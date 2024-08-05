from datasets import load_dataset
from transformers import LlamaTokenizer, LlamaForCausalLM
from transformers import GPTNeoXForCausalLM
import os

i = int(os.environ.get("ID"))
# tokenizer = LlamaTokenizer.from_pretrained("LLM360/Amber", revision=f"ckpt_{i}", cache_dir=f"/om2/user/sunnyd/amber_cache/")
# model = LlamaForCausalLM.from_pretrained("LLM360/Amber", revision=f"ckpt_{i}", cache_dir=f"/om2/user/sunnyd/amber_cache/", device_map='cpu', low_cpu_mem_usage=True)


model = GPTNeoXForCausalLM.from_pretrained(
    f"EleutherAI/pythia-410M-deduped",
    revision = f'step{i}',
    cache_dir=f"/om2/user/sunnyd/pythia_cache"
)