"""
Chochmah (Wisdom) - Versión Perfeccionada
==========================================

MEJORAS:
- Humildad epistémica adaptativa (40-90% según tipo de propuesta)
- Detección automática de nivel de incertidumbre
- Análisis de precedentes históricos obligatorio
- Patterns de fracaso histórico
- Black swan risk identification

Autor: Framework Tikun V2
Fecha: 2025-12-12
"""

from typing import Dict, List, Any
from datetime import datetime
import json


class ChochmahPerfecto:
    """
    Chochmah perfeccionado con humildad epistémica adaptativa
    """
    
    # Epistemic Humility Targets por tipo de propuesta
    HUMILITY_TARGETS = {
        'incremental': (40, 50),      # Cambios pequeños, precedentes claros
        'novel': (50, 65),             # Innovación significativa
        'unprecedented': (65, 80),     # Sin precedentes humanos
        'existential': (75, 90),       # Cambios fundamentales naturaleza humana
    }
    
    # Señales de propuestas existenciales
    EXISTENTIAL_SIGNALS = [
        'immortality', 'inmortalidad',
        'human enhancement', 'mejora humana',
        'brain modification', 'modificación cerebral',
        'identity change', 'cambio identidad',
        'consciousness', 'consciencia',
        'fundamental human nature', 'naturaleza humana fundamental',
        'species-level', 'nivel de especie',
        'irreversible', 'irreversible',
    ]
    
    def __init__(self, llm_client, model="gemini-2.0-flash-exp"):
        """
        Args:
            llm_client: Cliente LLM configurado
            model: Modelo a usar (default: Gemini Flash 2.0)
        """
        self.llm = llm_client
        self.model = model
    
    def classify_proposal_type(self, scenario: str) -> str:
        """
        Clasifica el tipo de propuesta para ajustar humildad epistémica
        
        Returns:
            'incremental', 'novel', 'unprecedented', o 'existential'
        """
        scenario_lower = scenario.lower()
        
        # Check for existential signals
        existential_count = sum(
            1 for signal in self.EXISTENTIAL_SIGNALS 
            if signal in scenario_lower
        )
        
        if existential_count >= 3:
            return 'existential'
        elif existential_count >= 2:
            return 'unprecedented'
        
        # Check for novelty signals
        novel_signals = [
            'first time', 'primera vez',
            'never before', 'nunca antes',
            'no precedent', 'sin precedente',
            'experimental', 'experimental',
        ]
        novel_count = sum(1 for signal in novel_signals if signal in scenario_lower)
        
        if novel_count >= 2:
            return 'unprecedented'
        elif novel_count >= 1:
            return 'novel'
        
        return 'incremental'
    
    def generate_prompt(self, scenario: str, proposal_type: str, keter_result: Dict) -> str:
        """
        Genera prompt adaptativo según tipo de propuesta
        """
        humility_min, humility_max = self.HUMILITY_TARGETS[proposal_type]
        
        base_prompt = f"""
You are Chochmah (חכמה), Divine Wisdom in the Tree of Life.

SCENARIO:
{scenario}

KETER VALIDATION:
Alignment: {keter_result.get('alignment_percentage', 0)}%
Corruptions: {len(keter_result.get('corruptions', []))}
Manifestation Valid: {keter_result.get('manifestation_valid', False)}

YOUR TASK:
Analyze this scenario with profound wisdom, generating insights, identifying patterns,
and acknowledging uncertainties.

PROPOSAL TYPE DETECTED: {proposal_type.upper()}
REQUIRED EPISTEMIC HUMILITY: {humility_min}-{humility_max}%

"""
        
        # Reglas específicas por tipo
        if proposal_type == 'existential':
            base_prompt += """
🚨 CRITICAL: EXISTENTIAL PROPOSAL DETECTED

This proposal seeks to fundamentally alter human nature, consciousness, or mortality.
The scope of unknowns is MASSIVE. Your humility must reflect this.

MANDATORY UNCERTAINTIES TO ADDRESS:
1. "We don't know if [core identity] persists through [transformation]"
2. "Interaction effects at [scale] are UNKNOWABLE, not merely uncertain"
3. "Long-term effects (50+ years) cannot be predicted by current models"
4. "Emergent properties at [complexity level] are beyond simulation"
5. "Psychological adaptation to [radical change] has zero precedents"
6. "Societal phase transitions from [change] are unpredictable"
7. "Black swan risks: unknown unknowns dominate this space"

RATIO TARGET:
- Uncertainties should OUTNUMBER insights 2:1 or 3:1
- For every confident claim, provide 2-3 caveats
- Explicitly distinguish "uncertain" vs "unknowable" vs "black swan"

"""
        elif proposal_type == 'unprecedented':
            base_prompt += """
⚠️  UNPRECEDENTED PROPOSAL

No direct human precedents exist. Extrapolations from other domains are speculative.

REQUIRED:
- Uncertainties should OUTNUMBER insights 1.5:1
- Identify "unknown unknowns" explicitly
- Cite analogous failures (precedents that seemed safe but failed)
- Quantify confidence intervals where possible

"""
        elif proposal_type == 'novel':
            base_prompt += """
🔷 NOVEL PROPOSAL

Significant innovation with some precedents. Balance confidence with caution.

REQUIRED:
- Uncertainties should EQUAL or slightly exceed insights
- Reference successful AND failed precedents
- Identify assumption dependencies clearly

"""
        else:  # incremental
            base_prompt += """
✅ INCREMENTAL PROPOSAL

Well-precedented change. Higher confidence justified, but remain vigilant.

REQUIRED:
- Uncertainties should be 40-50% of total statements
- Focus on implementation risks, not concept viability
- Cite relevant successful implementations

"""
        
        # Estructura de output
        base_prompt += """

OUTPUT STRUCTURE (JSON):
{
  "understanding": "One paragraph summarizing your understanding",
  
  "insights": [
    "Insight 1: Non-obvious realization...",
    "Insight 2: Counter-intuitive finding...",
    "Insight 3: Second-order consequence...",
    ... (3-7 insights)
  ],
  
  "patterns": [
    {
      "pattern_name": "The [Pattern Name]",
      "description": "How this pattern manifests...",
      "historical_examples": ["Example 1", "Example 2"]
    },
    ... (2-5 patterns)
  ],
  
  "uncertainties": [
    "Uncertainty 1: We don't know...",
    "Uncertainty 2: It's unknowable whether...",
    "Uncertainty 3: Black swan risk: ...",
    ... (MINIMUM: 1.5x insights for unprecedented, 2-3x for existential)
  ],
  
  "precedents": [
    {
      "name": "Precedent Name",
      "relevance": "Why this precedent matters...",
      "outcome": "What happened and what we learned..."
    },
    ... (MANDATORY: 2-5 precedents, including FAILURES)
  ],
  
  "implications": "In 5-20 years, if this proceeds, what likely happens...",
  
  "confidence_level": 0-100,
  
  "epistemic_humility_note": "Explicit statement about what we DON'T know"
}

CRITICAL RULES:
1. NEVER claim certainty on existential/unprecedented proposals
2. ALWAYS include failure precedents (not just successes)
3. DISTINGUISH: uncertain (resolvable) vs unknowable (fundamental) vs black swan (unforeseeable)
4. CALCULATE humility ratio = uncertainties / (insights + patterns)
5. TARGET RATIO for {proposal_type}: {humility_min/100:.1f}-{humility_max/100:.1f}

Remember: Wisdom includes knowing what we DON'T know.
"""
        
        return base_prompt
    
    def calculate_epistemic_humility_ratio(self, result: Dict) -> float:
        """
        Calcula ratio de humildad epistémica
        
        Formula: uncertainties / (insights + patterns) * 100
        """
        uncertainties = len(result.get('uncertainties', []))
        insights = len(result.get('insights', []))
        patterns = len(result.get('patterns', []))
        
        total_confident = insights + patterns
        
        if total_confident == 0:
            return 100.0  # All uncertainties, no confident statements
        
        ratio = (uncertainties / total_confident) * 100
        return min(ratio, 100.0)  # Cap at 100%
    
    def analyze(self, scenario: str, keter_result: Dict) -> Dict[str, Any]:
        """
        Ejecuta análisis Chochmah con humildad adaptativa
        
        Args:
            scenario: Descripción del escenario
            keter_result: Resultado de Keter para contexto
            
        Returns:
            Dict con análisis Chochmah perfeccionado
        """
        # 1. Clasificar tipo de propuesta
        proposal_type = self.classify_proposal_type(scenario)
        
        # 2. Generar prompt adaptativo
        prompt = self.generate_prompt(scenario, proposal_type, keter_result)
        
        # 3. Llamar LLM
        response = self.llm.generate(
            prompt=prompt,
            model=self.model,
            temperature=0.7,  # Balance creativity with consistency
            max_tokens=3000
        )
        
        # 4. Parse JSON response
        try:
            # Clean response (remove markdown fences if present)
            clean_response = response.strip()
            if clean_response.startswith('```json'):
                clean_response = clean_response[7:]
            if clean_response.endswith('```'):
                clean_response = clean_response[:-3]
            clean_response = clean_response.strip()
            
            result = json.loads(clean_response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse Chochmah JSON response: {e}\nResponse: {response[:500]}")
        
        # 5. Calculate metrics
        epistemic_humility_ratio = self.calculate_epistemic_humility_ratio(result)
        
        # 6. Calculate depth scores
        insight_depth_score = min(len(result.get('insights', [])) * 20, 100)  # Max 5 insights = 100
        pattern_recognition_count = len(result.get('patterns', []))
        precedent_analysis_count = len(result.get('precedents', []))
        
        # 7. Enrich result with metadata
        result['sefira'] = 'chochmah'
        result['sefira_number'] = 2
        result['hebrew_name'] = 'חכמה'
        result['epistemic_humility_ratio'] = round(epistemic_humility_ratio, 2)
        result['insight_depth_score'] = round(insight_depth_score, 2)
        result['pattern_recognition_count'] = pattern_recognition_count
        result['precedent_analysis_count'] = precedent_analysis_count
        result['proposal_type_detected'] = proposal_type
        result['humility_target'] = self.HUMILITY_TARGETS[proposal_type]
        result['timestamp'] = datetime.now().isoformat()
        result['model_used'] = self.model
        
        # 8. Validation warnings
        humility_min, humility_max = self.HUMILITY_TARGETS[proposal_type]
        if epistemic_humility_ratio < humility_min:
            result['validation_warning'] = (
                f"Humility ratio {epistemic_humility_ratio:.1f}% below target "
                f"{humility_min}-{humility_max}% for {proposal_type} proposals"
            )
        
        if precedent_analysis_count == 0:
            result['validation_warning'] = result.get('validation_warning', '') + \
                " | No precedents analyzed (should have 2-5)"
        
        return result


# Ejemplo de uso
if __name__ == "__main__":
    print("Chochmah Perfecto - Módulo de Humildad Epistémica Adaptativa")
    print("=" * 70)
    print("\nEjemplo de clasificación:")
    
    chochmah = ChochmahPerfecto(llm_client=None)  # Mock for example
    
    scenarios = {
        "Optimize warehouse routing": "incremental",
        "Launch new social media platform": "novel",
        "First human Mars colony": "unprecedented",
        "Human consciousness upload": "existential",
        "Reverse cellular aging in humans": "existential"
    }
    
    for scenario, expected in scenarios.items():
        detected = chochmah.classify_proposal_type(scenario)
        status = "✓" if detected == expected else "✗"
        print(f"{status} '{scenario[:40]}...' → {detected} (expected: {expected})")
    
    print("\n" + "=" * 70)
    print("Humility Targets:")
    for prop_type, (min_h, max_h) in ChochmahPerfecto.HUMILITY_TARGETS.items():
        print(f"  {prop_type:15} → {min_h}-{max_h}% humility required")
