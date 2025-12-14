"""
LLM Client Unificado para Framework Tikun
Soporta Gemini, Claude, y DeepSeek
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
        """Genera respuesta de Gemini con timeout"""
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Gemini API timeout after 30 seconds")
        
        # Set 30 second timeout
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(30)
        
        try:
            response = self.client.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": 4096,
                },
                request_options={"timeout": 30}  # 30 second timeout
            )
            signal.alarm(0)  # Cancel timeout
            return response.text
        except TimeoutError:
            signal.alarm(0)
            raise TimeoutError("Gemini API took too long to respond (>30s)")
        except Exception as e:
            signal.alarm(0)
            raise


class ClaudeClient(LLMClient):
    """Cliente para Anthropic Claude"""

    def __init__(self, model: str = "claude-sonnet-4-20250514", api_key: Optional[str] = None):
        super().__init__(model, api_key or os.getenv("ANTHROPIC_API_KEY"))

        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError("anthropic not installed. Run: pip install anthropic")

    def generate(self, prompt: str, temperature: float = 0.5) -> str:
        """Genera respuesta de Claude"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text


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
        """Genera respuesta de DeepSeek con timeout"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=4096,
                timeout=30  # 30 second timeout
            )
            return response.choices[0].message.content
        except Exception as e:
            if "timeout" in str(e).lower():
                raise TimeoutError("DeepSeek API took too long to respond (>30s)")
            raise


class LLMClientFactory:
    """Factory para crear clientes LLM"""

    @staticmethod
    def create_client(provider: str, model: Optional[str] = None, api_key: Optional[str] = None) -> LLMClient:
        """
        Crea cliente LLM

        Args:
            provider: 'gemini', 'claude', o 'deepseek'
            model: Modelo específico (opcional)
            api_key: API key (opcional, usa .env si no se provee)

        Returns:
            LLMClient instance
        """
        if provider.lower() == 'gemini':
            return GeminiClient(model or "gemini-2.0-flash-exp", api_key)
        elif provider.lower() == 'claude':
            return ClaudeClient(model or "claude-sonnet-4-20250514", api_key)
        elif provider.lower() == 'deepseek':
            return DeepSeekClient(model or "deepseek-chat", api_key)
        else:
            raise ValueError(f"Unknown provider: {provider}. Use 'gemini', 'claude', or 'deepseek'")


# Default configurations per Sefira
SEFIROT_LLM_MAPPING = {
    'keter': ('gemini', 'gemini-2.0-flash-exp'),
    'chochmah': ('gemini', 'gemini-2.0-flash-exp'),
    'binah': ('gemini', 'gemini-2.0-flash-exp'),
    'chesed': ('gemini', 'gemini-2.0-flash-exp'),
    'gevurah': ('gemini', 'gemini-2.0-flash-exp'),
    'tiferet': ('gemini', 'gemini-2.0-flash-exp'),
    'netzach': ('gemini', 'gemini-2.0-flash-exp'),
    'hod': ('gemini', 'gemini-2.0-flash-exp'),
    'yesod': ('gemini', 'gemini-2.0-flash-exp'),
    'malchut': ('gemini', 'gemini-2.0-flash-exp'),
}


def get_llm_for_sefira(sefira_name: str) -> LLMClient:
    """Obtiene cliente LLM configurado para una Sefirá específica"""
    if sefira_name.lower() not in SEFIROT_LLM_MAPPING:
        raise ValueError(f"Unknown sefira: {sefira_name}")

    provider, model = SEFIROT_LLM_MAPPING[sefira_name.lower()]
    return LLMClientFactory.create_client(provider, model)