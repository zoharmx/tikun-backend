"""
LLM Client Unificado para Framework Tikun
Soporta Gemini, DeepSeek y Mistral
"""

import os
import json
import re
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()


class LLMClient:
    """Cliente base para LLMs"""

    def __init__(self, model: str, api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key

    def generate(self, prompt: str, temperature: float = 0.5) -> str:
        """Genera respuesta del LLM"""
        raise NotImplementedError

    def parse_json_response(self, response: str) -> Dict[str, Any]:
        """Parse JSON de respuesta del LLM"""
        # Remove markdown code blocks if present
        response = re.sub(r'```json\s*', '', response)
        response = re.sub(r'```\s*$', '', response)
        response = response.strip()

        # Remove control characters that break JSON parsing
        response = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', response)

        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            # Try to extract JSON from text
            json_match = re.search(r'\{.*\}', response, re.DOTALL)
            if json_match:
                cleaned = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', json_match.group())
                return json.loads(cleaned)
            raise ValueError(f"Failed to parse JSON: {e}\nResponse: {response[:500]}")


class GeminiClient(LLMClient):
    """Cliente para Google Gemini"""

    def __init__(self, model: str = "gemini-2.0-flash-exp", api_key: Optional[str] = None):
        super().__init__(model, api_key or os.getenv("GEMINI_API_KEY"))

        try:
            import google.generativeai as genai
            genai.configure(api_key=self.api_key)
            self.client = genai.GenerativeModel(model)
        except ImportError:
            raise ImportError("google-generativeai not installed. Run: pip install google-generativeai")

    def generate(self, prompt: str, temperature: float = 0.5) -> str:
        """Genera respuesta de Gemini"""
        response = self.client.generate_content(
            prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": 4096,
            }
        )
        return response.text


class DeepSeekClient(LLMClient):
    """Cliente para DeepSeek (compatible con OpenAI API)"""

    def __init__(self, model: str = "deepseek-chat", api_key: Optional[str] = None):
        super().__init__(model, api_key or os.getenv("DEEPSEEK_API_KEY"))

        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.deepseek.com"
            )
        except ImportError:
            raise ImportError("openai not installed. Run: pip install openai")

    def generate(self, prompt: str, temperature: float = 0.5) -> str:
        """Genera respuesta de DeepSeek"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=4096
        )
        return response.choices[0].message.content


class MistralClient(LLMClient):
    """Cliente para Mistral (compatible con OpenAI API)"""

    def __init__(self, model: str = "mistral-large-latest", api_key: Optional[str] = None):
        super().__init__(model, api_key or os.getenv("MISTRAL_API_KEY"))

        try:
            from openai import OpenAI
            self.client = OpenAI(
                api_key=self.api_key,
                base_url="https://api.mistral.ai/v1"
            )
        except ImportError:
            raise ImportError("openai not installed. Run: pip install openai")

    def generate(self, prompt: str, temperature: float = 0.5) -> str:
        """Genera respuesta de Mistral"""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=4096
        )
        return response.choices[0].message.content


class LLMClientFactory:
    """Factory para crear clientes LLM"""

    @staticmethod
    def create_client(provider: str, model: Optional[str] = None, api_key: Optional[str] = None) -> LLMClient:
        """
        Crea cliente LLM

        Args:
            provider: 'gemini', 'deepseek' o 'mistral'
            model: Modelo específico (opcional)
            api_key: API key (opcional, usa .env si no se provee)

        Returns:
            LLMClient instance
        """
        provider_lower = provider.lower()

        if provider_lower == 'gemini':
            return GeminiClient(model or "gemini-2.0-flash-exp", api_key)
        elif provider_lower == 'deepseek':
            return DeepSeekClient(model or "deepseek-chat", api_key)
        elif provider_lower == 'mistral':
            return MistralClient(model or "mistral-large-latest", api_key)
        else:
            raise ValueError(f"Unknown provider: {provider}. Use 'gemini', 'deepseek' or 'mistral'")


# Default configurations per Sefira
# Distribución optimizada: Principalmente Gemini (gratis), Mistral y DeepSeek para módulos específicos
SEFIROT_LLM_MAPPING = {
    'keter': ('gemini', 'gemini-2.0-flash-exp'),          # Alineación inicial - GEMINI
    'chochmah': ('mistral', 'mistral-large-latest'),      # Análisis profundo - MISTRAL
    'binah_occidente': ('gemini', 'gemini-2.0-flash-exp'), # BinahSigma Occidente - GEMINI
    'binah_oriente': ('deepseek', 'deepseek-chat'),       # BinahSigma Oriente - DEEPSEEK
    'binah': ('gemini', 'gemini-2.0-flash-exp'),          # Binah default - GEMINI
    'chesed': ('gemini', 'gemini-2.0-flash-exp'),         # Expansión - GEMINI
    'gevurah': ('gemini', 'gemini-2.0-flash-exp'),        # Restricción - GEMINI
    'tiferet': ('gemini', 'gemini-2.0-flash-exp'),        # Balance - GEMINI
    'netzach': ('gemini', 'gemini-2.0-flash-exp'),        # Estrategia - GEMINI
    'hod': ('gemini', 'gemini-2.0-flash-exp'),            # Análisis social - GEMINI
    'yesod': ('gemini', 'gemini-2.0-flash-exp'),          # Decisión - GEMINI
    'malchut': ('gemini', 'gemini-2.0-flash-exp'),        # Reporte final - GEMINI
}


def get_llm_for_sefira(sefira_name: str) -> LLMClient:
    """Obtiene cliente LLM configurado para una Sefirá específica"""
    if sefira_name.lower() not in SEFIROT_LLM_MAPPING:
        raise ValueError(f"Unknown sefira: {sefira_name}")

    provider, model = SEFIROT_LLM_MAPPING[sefira_name.lower()]
    return LLMClientFactory.create_client(provider, model)
