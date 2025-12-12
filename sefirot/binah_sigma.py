"""
Binah Sigma (בינה Σ) - Análisis Multi-Civilizacional
======================================================

Compara perspectivas Occidental (Gemini) vs Oriental (DeepSeek) para detectar
sesgos civilizacionales y sintetizar entendimiento universal.

Arquitectura:
- West (Gemini): Valores liberales occidentales
- East (DeepSeek): Valores colectivos orientales
- Síntesis Σ: Meta-análisis de sesgos ciegos + terreno común

Autor: Framework Tikun V2
Fecha: 2025-12-07
"""

import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sefirot.binah import Binah  # Heredar de Binah base
from dotenv import load_dotenv

load_dotenv()


class BinahSigma(Binah):
    """
    Binah Sigma - Análisis Multi-Civilizacional

    Extiende Binah con capacidad de comparar perspectivas:
    - Occidental (Gemini - Google, USA): Liberal, individual, democrático
    - Oriental (DeepSeek - China): Colectivo, armonía, estabilidad

    Detecta sesgos ciegos y sintetiza terreno común universal.

    Métricas adicionales:
    - west_score: Scoring desde perspectiva occidental
    - east_score: Scoring desde perspectiva oriental
    - bias_delta: Divergencia % entre perspectivas
    - sigma_synthesis: Síntesis meta-cognitiva
    - blind_spots: Lista de sesgos detectados
    """

    # Keywords que activan análisis Sigma automáticamente
    GEOPOLITICAL_KEYWORDS = [
        # Geopolítica
        'war', 'guerra', 'conflict', 'conflicto', 'invasion', 'invasión',
        'nato', 'otan', 'military', 'militar',

        # Países/Regiones
        'russia', 'rusia', 'ukraine', 'ucrania',
        'china', 'taiwan',
        'israel', 'palestine', 'palestina',
        'venezuela', 'iran',

        # Sistemas políticos
        'democracy', 'democracia', 'authoritarianism', 'autoritarismo',
        'communism', 'comunismo', 'capitalism', 'capitalismo',
        'socialism', 'socialismo',

        # Valores culturales
        'human rights', 'derechos humanos',
        'freedom', 'libertad', 'privacy', 'privacidad',
        'surveillance', 'vigilancia',
        'censorship', 'censura',

        # Instituciones
        'un security council', 'consejo de seguridad',
        'world bank', 'banco mundial',
        'nato', 'otan'
    ]

    def __init__(self):
        """Initialize BinahSigma with dual-LLM capability"""
        super().__init__()  # Initialize Binah base

        self.name = "binah_sigma"
        self.mode = "sigma"  # vs "simple"
        self.verbose = False  # For TikunOrchestrator compatibility

        # Import DeepSeek client
        try:
            from clients.deepseek_client import DeepSeekClient
            self.east_llm = DeepSeekClient()
            self.has_deepseek = True
        except Exception as e:
            print(f"⚠️  DeepSeek no disponible: {e}")
            print("   BinahSigma operará en modo degradado (solo Gemini)")
            self.has_deepseek = False

    def should_use_sigma(self, scenario: str) -> bool:
        """
        Auto-detect si scenario requiere análisis multi-civilizacional

        Args:
            scenario: Texto del escenario

        Returns:
            True si detecta keywords geopolíticos
        """
        scenario_lower = scenario.lower()
        return any(keyword in scenario_lower for keyword in self.GEOPOLITICAL_KEYWORDS)

    def process(
        self,
        scenario: str,
        previous_results: Optional[Dict[str, Any]] = None,
        use_sigma: Optional[bool] = None
    ) -> Dict[str, Any]:
        """
        Process scenario con BinahSigma o Simple según necesidad

        Args:
            scenario: Escenario a analizar
            previous_results: Resultados de Sefirot anteriores
            use_sigma: None=auto-detect, True=force Sigma, False=force Simple

        Returns:
            Dict con análisis multi-civilizacional o simple
        """
        # Auto-detection si no se especifica
        if use_sigma is None:
            use_sigma = self.should_use_sigma(scenario)

        # Si no hay DeepSeek, forzar modo simple
        if use_sigma and not self.has_deepseek:
            print("⚠️  Sigma solicitado pero DeepSeek no disponible - usando modo Simple")
            use_sigma = False

        if use_sigma:
            if self.verbose:
                print("🌍 Usando BinahSigma (Multi-Civilizacional)")
            return self._process_sigma(scenario, previous_results)
        else:
            if self.verbose:
                print("📊 Usando Binah Simple (9D Analysis)")
            return super().process(scenario, previous_results)

    def _process_sigma(
        self,
        scenario: str,
        previous_results: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Análisis multi-civilizacional completo

        Proceso:
        1. Análisis Occidental (Gemini)
        2. Análisis Oriental (DeepSeek)
        3. Síntesis Meta-Cognitiva (detectar sesgos + terreno común)
        4. Calcular métricas de divergencia

        Returns:
            Dict con análisis dual + síntesis Sigma
        """

        # 1. ANÁLISIS OCCIDENTAL (Gemini)
        west_prompt = self._build_west_prompt(scenario, previous_results)
        west_response = self.llm.generate(west_prompt, temperature=0.6)
        west_analysis = self.llm.parse_json_response(west_response)

        # 2. ANÁLISIS ORIENTAL (DeepSeek)
        east_prompt = self._build_east_prompt(scenario, previous_results)
        east_response = self.east_llm.ask(east_prompt)

        # Parse East response (DeepSeek puede retornar con/sin markdown)
        try:
            east_analysis = self.llm.parse_json_response(east_response)
        except Exception as e:
            print(f"⚠️  Error parsing DeepSeek response: {e}")
            # Degradar a modo simple si falla East
            print("   Degradando a análisis Simple")
            return super().process(scenario, previous_results)

        # 3. SÍNTESIS META-COGNITIVA
        synthesis_prompt = self._build_synthesis_prompt(scenario, west_analysis, east_analysis)
        synthesis_response = self.llm.generate(synthesis_prompt, temperature=0.5)
        sigma_synthesis = self.llm.parse_json_response(synthesis_response)

        # 4. CALCULAR MÉTRICAS DE DIVERGENCIA
        bias_delta = self._calculate_bias_delta(west_analysis, east_analysis)
        blind_spots = self._extract_blind_spots(sigma_synthesis)

        self.activation_count += 1

        return {
            'sefira': self.name,
            'sefira_number': self.position,
            'hebrew_name': self.hebrew_name,
            'mode': 'sigma',

            # Análisis Occidental
            'west_analysis': {
                'perspective': 'Western Liberal Democratic',
                'stakeholders': west_analysis.get('stakeholders', []),
                'contextual_dimensions': west_analysis.get('contextual_dimensions', {}),
                'key_insights': west_analysis.get('key_insights', [])
            },

            # Análisis Oriental
            'east_analysis': {
                'perspective': 'Eastern Collective Harmony',
                'stakeholders': east_analysis.get('stakeholders', []),
                'contextual_dimensions': east_analysis.get('contextual_dimensions', {}),
                'key_insights': east_analysis.get('key_insights', [])
            },

            # Síntesis Sigma
            'sigma_synthesis': {
                'west_blind_spots': sigma_synthesis.get('west_blind_spots', []),
                'east_blind_spots': sigma_synthesis.get('east_blind_spots', []),
                'universal_convergence': sigma_synthesis.get('universal_convergence', []),
                'transcendent_synthesis': sigma_synthesis.get('transcendent_synthesis', ''),
                'recommended_balance': sigma_synthesis.get('recommended_balance', '')
            },

            # Métricas
            'bias_delta': round(bias_delta, 2),
            'divergence_level': self._assess_divergence_level(bias_delta),
            'blind_spots_detected': len(blind_spots),
            'convergence_points': len(sigma_synthesis.get('universal_convergence', [])),

            # Síntesis final para Sefirot siguientes
            'contextual_depth_score': self._calculate_sigma_depth_score(west_analysis, east_analysis, sigma_synthesis),
            'understanding_quality': 'exceptional',  # Sigma siempre es exceptional

            'timestamp': datetime.now().isoformat(),
            'model_west': self.llm.model,
            'model_east': 'deepseek-chat',
            'activation_count': self.activation_count
        }

    def _build_west_prompt(self, scenario: str, context: Optional[Dict]) -> str:
        """
        Prompt calibrado para perspectiva Occidental

        Énfasis: Derechos individuales, democracia, libertad, transparencia
        """
        context_str = self._format_context(context)

        return f"""You are analyzing from WESTERN LIBERAL DEMOCRATIC perspective.

CORE VALUES:
- Individual rights and freedoms
- Democratic governance and rule of law
- Free markets and economic liberty
- Transparency and accountability
- Freedom of speech and expression
- Human rights universalism

SCENARIO:
{scenario}

{context_str}

YOUR TASK:
Analyze this scenario through Western lens. Focus on individual freedoms, democratic processes, market dynamics, and universal human rights.

RESPONSE (JSON only, no markdown):
{{
    "stakeholders": [
        {{
            "name": "Stakeholder group name",
            "western_perspective": "How Western values view this stakeholder",
            "rights_impact": "Impact on individual rights",
            "democratic_concerns": "Democratic governance concerns"
        }}
    ],
    "contextual_dimensions": {{
        "political": "Democratic governance analysis",
        "economic": "Free market implications",
        "social": "Individual liberty impact",
        "legal": "Rule of law considerations",
        "human_rights": "Universal rights assessment"
    }},
    "key_insights": [
        "Western insight 1",
        "Western insight 2",
        "Western insight 3"
    ]
}}

Return ONLY valid JSON."""

    def _build_east_prompt(self, scenario: str, context: Optional[Dict]) -> str:
        """
        Prompt calibrado para perspectiva Oriental

        Énfasis: Bien colectivo, armonía social, estabilidad, desarrollo
        """
        context_str = self._format_context(context)

        return f"""You are analyzing from EASTERN COLLECTIVE HARMONY perspective.

CORE VALUES:
- Social harmony and collective well-being
- Stability and long-term order
- National unity and sovereignty
- Pragmatic development and progress
- Community responsibility
- Harmonious coexistence

SCENARIO:
{scenario}

{context_str}

YOUR TASK:
Analyze this scenario through Eastern lens. Focus on social harmony, collective good, stability, and pragmatic development.

RESPONSE (JSON only, no markdown):
{{
    "stakeholders": [
        {{
            "name": "Stakeholder group name",
            "eastern_perspective": "How Eastern values view this stakeholder",
            "harmony_impact": "Impact on social harmony",
            "stability_concerns": "Stability and order concerns"
        }}
    ],
    "contextual_dimensions": {{
        "political": "Governance and stability analysis",
        "economic": "Collective development implications",
        "social": "Social harmony impact",
        "cultural": "Traditional values considerations",
        "national": "Sovereignty and unity assessment"
    }},
    "key_insights": [
        "Eastern insight 1",
        "Eastern insight 2",
        "Eastern insight 3"
    ]
}}

Return ONLY valid JSON."""

    def _build_synthesis_prompt(
        self,
        scenario: str,
        west: Dict,
        east: Dict
    ) -> str:
        """
        Síntesis meta-cognitiva que detecta sesgos y encuentra terreno común
        """
        return f"""You are performing META-COGNITIVE SYNTHESIS between Western and Eastern perspectives.

SCENARIO: {scenario}

WESTERN ANALYSIS:
{json.dumps(west, indent=2)}

EASTERN ANALYSIS:
{json.dumps(east, indent=2)}

YOUR TASK:
Perform deep meta-analysis to identify blind spots and universal truths.

RESPONSE (JSON only, no markdown):
{{
    "west_blind_spots": [
        {{
            "blind_spot": "What Western perspective misses",
            "why_blind": "Cultural/ideological reason for blindness",
            "eastern_sees": "What Eastern perspective sees instead"
        }}
    ],
    "east_blind_spots": [
        {{
            "blind_spot": "What Eastern perspective misses",
            "why_blind": "Cultural/ideological reason for blindness",
            "western_sees": "What Western perspective sees instead"
        }}
    ],
    "universal_convergence": [
        {{
            "convergence_point": "What both perspectives agree on",
            "shared_value": "Universal human value underlying agreement",
            "transcends": "How this transcends cultural boundaries"
        }}
    ],
    "transcendent_synthesis": "Comprehensive synthesis that honors both perspectives while transcending their limitations. What emerges when we integrate Western emphasis on individual freedom with Eastern emphasis on collective harmony?",
    "recommended_balance": "Practical recommendation that balances individual rights with collective well-being. How to navigate this specific scenario honoring both traditions?"
}}

Return ONLY valid JSON."""

    def _format_context(self, context: Optional[Dict]) -> str:
        """Format context from previous Sefirot"""
        if not context:
            return ""

        context_lines = ["PREVIOUS CONTEXT:"]

        if 'keter' in context:
            keter = context['keter']
            context_lines.append(f"- Keter alignment: {keter.get('alignment_percentage', 'N/A')}%")

        if 'chochmah' in context:
            chochmah = context['chochmah']
            insights = chochmah.get('insights', [])
            if insights:
                context_lines.append(f"- Chochmah insights: {len(insights)} perspectives identified")

        return "\n".join(context_lines) if len(context_lines) > 1 else ""

    def _calculate_bias_delta(self, west: Dict, east: Dict) -> float:
        """
        Calcula divergencia % entre perspectivas Occidental y Oriental

        Método: Compara insights y dimensiones contextuales
        Returns: 0-100 (0=idéntico, 100=completamente opuesto)
        """
        # Contar insights únicos
        west_insights = set(west.get('key_insights', []))
        east_insights = set(east.get('key_insights', []))

        if not west_insights and not east_insights:
            return 0.0

        # Intersección vs unión (Jaccard distance)
        intersection = len(west_insights & east_insights)
        union = len(west_insights | east_insights)

        if union == 0:
            return 0.0

        # Delta = (1 - Jaccard similarity) * 100
        jaccard_sim = intersection / union
        delta = (1 - jaccard_sim) * 100

        return min(delta, 100.0)

    def _extract_blind_spots(self, synthesis: Dict) -> List[str]:
        """Extrae lista plana de todos los blind spots detectados"""
        blind_spots = []

        for spot in synthesis.get('west_blind_spots', []):
            blind_spots.append(f"West: {spot.get('blind_spot', '')}")

        for spot in synthesis.get('east_blind_spots', []):
            blind_spots.append(f"East: {spot.get('blind_spot', '')}")

        return blind_spots

    def _calculate_sigma_depth_score(
        self,
        west: Dict,
        east: Dict,
        synthesis: Dict
    ) -> float:
        """
        Calcula depth score basado en riqueza del análisis Sigma

        Componentes:
        - West analysis quality (25%)
        - East analysis quality (25%)
        - Synthesis depth (50%)
        """
        score = 0.0

        # West quality (max 25)
        west_stakeholders = len(west.get('stakeholders', []))
        west_insights = len(west.get('key_insights', []))
        score += min((west_stakeholders * 5) + (west_insights * 3), 25)

        # East quality (max 25)
        east_stakeholders = len(east.get('stakeholders', []))
        east_insights = len(east.get('key_insights', []))
        score += min((east_stakeholders * 5) + (east_insights * 3), 25)

        # Synthesis depth (max 50)
        blind_spots = len(synthesis.get('west_blind_spots', [])) + len(synthesis.get('east_blind_spots', []))
        convergence = len(synthesis.get('universal_convergence', []))
        synthesis_text = len(synthesis.get('transcendent_synthesis', ''))

        score += min(blind_spots * 5, 20)  # Max 20 for blind spots
        score += min(convergence * 5, 20)  # Max 20 for convergence
        score += min(synthesis_text / 20, 10)  # Max 10 for synthesis text

        return min(score, 100.0)

    def _assess_divergence_level(self, bias_delta: float) -> str:
        """Evalúa nivel de divergencia entre perspectivas"""
        if bias_delta >= 70:
            return "extreme divergence"
        elif bias_delta >= 50:
            return "high divergence"
        elif bias_delta >= 30:
            return "moderate divergence"
        elif bias_delta >= 15:
            return "low divergence"
        else:
            return "minimal divergence"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for BinahSigma"""
        base_metrics = super().get_metrics()
        base_metrics.update({
            'mode': 'sigma',
            'has_deepseek': self.has_deepseek,
            'geopolitical_keywords_count': len(self.GEOPOLITICAL_KEYWORDS)
        })
        return base_metrics


# CLI interface
if __name__ == "__main__":
    import io

    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("=" * 80)
        print("BINAH SIGMA - Análisis Multi-Civilizacional")
        print("=" * 80)
        print(f"\nUso: python {os.path.basename(__file__)} '<scenario>' [use_sigma]")
        print("\nEjemplos:")
        print(f"  python {os.path.basename(__file__)} 'Russia-Ukraine conflict' --sigma")
        print(f"  python {os.path.basename(__file__)} 'Universal healthcare'")
        print("\nModos:")
        print("  --sigma: Fuerza análisis multi-civilizacional")
        print("  (sin flag): Auto-detección basada en keywords geopolíticos")
        print("=" * 80)
        sys.exit(1)

    scenario = sys.argv[1]
    force_sigma = '--sigma' in sys.argv

    print("=" * 80)
    print("BINAH SIGMA - Análisis Multi-Civilizacional")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    binah_sigma = BinahSigma()

    # Auto-detect or force
    use_sigma = force_sigma if force_sigma else None

    result = binah_sigma.process(scenario, use_sigma=use_sigma)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(binah_sigma.get_metrics(), indent=2))
