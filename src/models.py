from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pathlib import Path
import os

class ModelManager:
    def __init__(self, cache_dir="/app/models"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.models = {}
        self.tokenizers = {}

    async def load_model(self, model_id: str):
        """Load an AI model and its tokenizer."""
        if model_id not in self.models:
            tokenizer = AutoTokenizer.from_pretrained(
                model_id,
                cache_dir=self.cache_dir / model_id
            )
            model = AutoModelForCausalLM.from_pretrained(
                model_id,
                cache_dir=self.cache_dir / model_id,
                torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
                device_map="auto"
            )
            
            self.models[model_id] = model
            self.tokenizers[model_id] = tokenizer
            
        return self.models[model_id], self.tokenizers[model_id]

    async def get_model(self, model_id: str):
        """Get a loaded model or load it if not present."""
        if model_id not in self.models:
            await self.load_model(model_id)
        return self.models[model_id], self.tokenizers[model_id]

    def list_models(self):
        """List all currently loaded models."""
        return list(self.models.keys())

# Global model manager instance
model_manager = ModelManager()
