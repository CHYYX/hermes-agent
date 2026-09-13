"""Lanseq provider profile."""

from providers import register_provider
from providers.base import ProviderProfile


lanseq = ProviderProfile(
    name="lanseq",
    display_name="Lanseq",
    description="OpenAI-compatible inference for open-weight models from Hong Kong / APAC",
    signup_url="https://api.lanseq.cloud/docs",
    env_vars=("LANSEQ_API_KEY", "LANSEQ_BASE_URL"),
    base_url="https://api.lanseq.cloud/v1",
    auth_type="api_key",
    fallback_models=("qwen3.8-27b-int4",),
    default_max_tokens=8192,
)

register_provider(lanseq)
