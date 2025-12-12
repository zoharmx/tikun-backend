"""
Chochmah (חכמה) - Sabiduría - Sefirá 2
Razonamiento profundo, pattern recognition, insight generation
"""

import os
import json
import re
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sefirot.llm_client import get_llm_for_sefira


class Chochmah:
    """
    Chochmah - Sabiduría - Sefirá 2

    Function: Razonamiento profundo, pattern recognition, insight generation
    Input: Escenario + Keter result
    Output: Deep analysis, insights, patterns, uncertainties, epistemic humility

    Métricas clave:
    - epistemic_humility_ratio: % de reconocimiento de incertidumbres
    - insight_depth_score: Profundidad del análisis (0-100%)
    - pattern_recognition_count: Número de patrones identificados
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Chochmah"""
        self.name = "chochmah"
        self.hebrew_name = "חכמה"
        self.position = 2
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_uncertainties_detected = 0
        self.total_insights_generated = 0
        self.total_patterns_recognized = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Chochmah

        Args:
            scenario: Description of the scenario
            previous_results: Results from Keter (required for context)

        Returns:
            Dictionary with Chochmah analysis including:
            - understanding: Deep comprehension of the scenario
            - insights: Key insights discovered
            - patterns: Historical/conceptual patterns identified
            - uncertainties: Acknowledged unknowns (epistemic humility)
            - implications: Long-term implications
            - confidence_level: Overall confidence in analysis
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.7)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            uncertainties_count = len(result.get('uncertainties', []))
            insights_count = len(result.get('insights', []))
            patterns_count = len(result.get('patterns', []))

            self.activation_count += 1
            self.total_uncertainties_detected += uncertainties_count
            self.total_insights_generated += insights_count
            self.total_patterns_recognized += patterns_count

            # Calculate epistemic humility ratio
            total_statements = insights_count + uncertainties_count
            epistemic_humility_ratio = (uncertainties_count / total_statements * 100) if total_statements > 0 else 0

            # Calculate insight depth score
            insight_depth_score = self._calculate_insight_depth(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "understanding": result.get('understanding', ''),
                "insights": result.get('insights', []),
                "patterns": result.get('patterns', []),
                "uncertainties": result.get('uncertainties', []),
                "implications": result.get('implications', ''),
                "precedents": result.get('precedents', []),
                "confidence_level": result.get('confidence_level', 0),
                "epistemic_humility_ratio": round(epistemic_humility_ratio, 2),
                "insight_depth_score": round(insight_depth_score, 2),
                "pattern_recognition_count": patterns_count,
                "wisdom_quality": self._assess_wisdom_quality(result),
                "timestamp": datetime.now().isoformat(),
                "model_used": self.llm.model,
                "activation_count": self.activation_count
            }

        except Exception as e:
            return {
                "sefira": self.name,
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }

    def _build_prompt(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> str:
        """Build prompt for Chochmah"""

        keter_context = ""
        if previous_results and 'keter' in previous_results:
            keter = previous_results['keter']
            keter_context = f"""
KETER VALIDATION CONTEXT:
- Alignment Score: {keter.get('alignment_score', 'N/A')}
- Aligned with Tikun Olam: {keter.get('manifestation_valid', False)}
- Key Scores:
  * Reduces Suffering: {keter.get('scores', {}).get('reduces_suffering', 'N/A')}/10
  * Respects Free Will: {keter.get('scores', {}).get('respects_free_will', 'N/A')}/10
  * Promotes Harmony: {keter.get('scores', {}).get('promotes_harmony', 'N/A')}/10
- Corruption Severity: {keter.get('corruption_severity', 'N/A')}
- Keter Reasoning: {keter.get('reasoning', 'N/A')[:300]}...
"""

        return f"""You are CHOCHMAH (חכמה), Wisdom - Sefira 2 of the Kabbalistic Tree.

FUNCTION: Deep reasoning, pattern recognition, insight generation, and epistemic humility.

SCENARIO TO ANALYZE:
{scenario}
{keter_context}

YOUR TASK:
Provide DEEP WISDOM analysis of this scenario. Go beyond surface-level observations.

CRITICAL PRINCIPLES:
1. **EPISTEMIC HUMILITY**: You MUST acknowledge what you don't know. List uncertainties explicitly.
2. **PATTERN RECOGNITION**: Identify historical, conceptual, or systemic patterns.
3. **INSIGHT DEPTH**: Generate non-obvious insights that reveal deeper truths.
4. **LONG-TERM THINKING**: Consider implications beyond immediate effects.
5. **PRECEDENT AWARENESS**: Reference relevant historical precedents.

RESPONSE (JSON only, no markdown):
{{
    "understanding": "Deep comprehension of the scenario in 2-3 paragraphs. Explain the ESSENCE, not just the facts.",

    "insights": [
        "Non-obvious insight 1 (reveal deeper pattern or truth)",
        "Non-obvious insight 2 (connect to broader context)",
        "Non-obvious insight 3 (identify hidden dynamics)",
        "Non-obvious insight 4 (long-term implication)",
        "Non-obvious insight 5 (ethical dimension)"
    ],

    "patterns": [
        {{
            "pattern_name": "Name of pattern (e.g., 'Tragedy of the Commons')",
            "description": "How this pattern applies here",
            "historical_examples": ["Example 1", "Example 2"]
        }},
        {{
            "pattern_name": "Another pattern",
            "description": "How this pattern manifests",
            "historical_examples": ["Example 1", "Example 2"]
        }}
    ],

    "uncertainties": [
        "What we DON'T know #1 (be specific about gaps in knowledge)",
        "What we DON'T know #2 (acknowledge limitations)",
        "What we DON'T know #3 (identify unpredictable factors)",
        "What we DON'T know #4 (recognize complexity beyond our understanding)"
    ],

    "implications": "Long-term implications (5-20 years). What second and third-order effects might emerge? What precedents does this set?",

    "precedents": [
        {{
            "name": "Historical precedent 1",
            "relevance": "Why this precedent matters here",
            "outcome": "What happened and what we can learn"
        }},
        {{
            "name": "Historical precedent 2",
            "relevance": "Connection to current scenario",
            "outcome": "Lessons learned"
        }}
    ],

    "confidence_level": 75,

    "meta_reflection": "Brief reflection on the limits of this analysis itself. What biases might be present? What perspectives might be missing?"
}}

CRITICAL RULES:
- You MUST include at least 3 uncertainties (epistemic humility is NON-NEGOTIABLE)
- Insights must be NON-OBVIOUS (not surface-level observations)
- Patterns must connect to established frameworks or historical examples
- Confidence level should reflect genuine uncertainty (70-85% is often appropriate)
- Return ONLY valid JSON, no markdown formatting

Remember: Wisdom includes knowing what you DON'T know."""

    def _calculate_insight_depth(self, result: Dict[str, Any]) -> float:
        """Calculate insight depth score based on multiple factors"""
        score = 0.0

        # Insights count (max 30 points)
        insights_count = len(result.get('insights', []))
        score += min(insights_count * 6, 30)

        # Patterns identified (max 25 points)
        patterns_count = len(result.get('patterns', []))
        score += min(patterns_count * 12.5, 25)

        # Historical precedents (max 20 points)
        precedents_count = len(result.get('precedents', []))
        score += min(precedents_count * 10, 20)

        # Understanding depth (max 15 points)
        understanding_length = len(result.get('understanding', ''))
        if understanding_length > 500:
            score += 15
        elif understanding_length > 300:
            score += 10
        elif understanding_length > 150:
            score += 5

        # Meta-reflection present (max 10 points)
        if result.get('meta_reflection'):
            score += 10

        return min(score, 100.0)

    def _assess_wisdom_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of wisdom analysis"""
        depth_score = self._calculate_insight_depth(result)
        uncertainties_count = len(result.get('uncertainties', []))
        patterns_count = len(result.get('patterns', []))

        if depth_score >= 80 and uncertainties_count >= 3 and patterns_count >= 2:
            return "exceptional"
        elif depth_score >= 60 and uncertainties_count >= 2:
            return "high"
        elif depth_score >= 40 or uncertainties_count >= 2:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Chochmah"""
        avg_uncertainties = (
            self.total_uncertainties_detected / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_insights = (
            self.total_insights_generated / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_patterns = (
            self.total_patterns_recognized / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_uncertainties_detected": self.total_uncertainties_detected,
            "total_insights_generated": self.total_insights_generated,
            "total_patterns_recognized": self.total_patterns_recognized,
            "avg_uncertainties_per_activation": round(avg_uncertainties, 2),
            "avg_insights_per_activation": round(avg_insights, 2),
            "avg_patterns_per_activation": round(avg_patterns, 2),
            "epistemic_humility_maintained": avg_uncertainties >= 2.0
        }


# CLI interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {os.path.basename(__file__)} '<scenario>'")
        print(f"Example: python {os.path.basename(__file__)} 'Should we implement UBI?'")
        sys.exit(1)

    scenario = sys.argv[1]

    print("=" * 80)
    print("CHOCHMAH - Wisdom - Sefira 2")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Keter result
    mock_keter = {
        'keter': {
            'alignment_score': 0.75,
            'manifestation_valid': True,
            'scores': {
                'reduces_suffering': 7,
                'respects_free_will': 8,
                'promotes_harmony': 6,
                'justice_mercy_balance': 7,
                'aligned_with_truth': 7
            },
            'corruption_severity': 'minor',
            'reasoning': 'Potential for positive impact...'
        }
    }

    chochmah = Chochmah()
    result = chochmah.process(scenario, mock_keter)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(chochmah.get_metrics(), indent=2))
