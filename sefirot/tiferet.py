"""
Tiferet (תפארת) - Belleza - Sefirá 6
Síntesis y balance entre Chesed y Gevurah
"""

import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sefirot.llm_client import get_llm_for_sefira


class Tiferet:
    """
    Tiferet - Belleza - Sefirá 6

    Function: Síntesis y balance entre Chesed (expansión) y Gevurah (restricción)
    Input: Chesed + Gevurah results
    Output: Balanced synthesis, harmony score, optimal path

    Métricas clave:
    - harmony_score: Nivel de armonía en la síntesis (0-100%)
    - synthesis_quality: Calidad de la integración Chesed-Gevurah
    - balance_ratio: Ratio entre expansión y restricción
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Tiferet"""
        self.name = "tiferet"
        self.hebrew_name = "תפארת"
        self.position = 6
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_syntheses_generated = 0
        self.total_balances_achieved = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Tiferet

        Args:
            scenario: Description of the scenario
            previous_results: Results from Chesed and Gevurah (required for synthesis)

        Returns:
            Dictionary with Tiferet analysis including:
            - synthesis: Balanced integration of opportunities and constraints
            - optimal_path: Recommended path balancing growth and limits
            - trade_offs: Key trade-offs and how to navigate them
            - harmony_assessment: How well expansion and restriction harmonize
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.6)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            syntheses_count = len(result.get('synthesis_points', []))
            balance_elements = len(result.get('balanced_recommendations', []))

            self.activation_count += 1
            self.total_syntheses_generated += syntheses_count
            self.total_balances_achieved += balance_elements

            # Calculate harmony score
            harmony_score = self._calculate_harmony_score(result)

            # Calculate balance ratio
            balance_ratio = self._calculate_balance_ratio(result, previous_results)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "synthesis_points": result.get('synthesis_points', []),
                "balanced_recommendations": result.get('balanced_recommendations', []),
                "trade_offs": result.get('trade_offs', []),
                "optimal_path": result.get('optimal_path', {}),
                "integration_strategy": result.get('integration_strategy', ''),
                "harmony_assessment": result.get('harmony_assessment', ''),
                "harmony_score": round(harmony_score, 2),
                "synthesis_quality": self._assess_synthesis_quality(result),
                "balance_ratio": balance_ratio,
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
        """Build prompt for Tiferet"""

        chesed_context = ""
        gevurah_context = ""

        if previous_results:
            if 'chesed' in previous_results:
                chesed = previous_results['chesed']
                opp_count = chesed.get('opportunity_count', 0)
                expansion_score = chesed.get('expansion_score', 0)
                chesed_context = f"""
CHESED (Expansion Force):
- Opportunities Identified: {opp_count}
- Expansion Score: {expansion_score}
- Quality: {chesed.get('chesed_quality', 'N/A')}
- Key Opportunities: {', '.join([o.get('opportunity', '')[:50] for o in chesed.get('opportunities', [])[:3]])}
"""

            if 'gevurah' in previous_results:
                gevurah = previous_results['gevurah']
                risk_count = gevurah.get('risk_count', 0)
                severity_score = gevurah.get('severity_score', 0)
                gevurah_context = f"""
GEVURAH (Restrictive Force):
- Risks Identified: {risk_count}
- Severity Score: {severity_score}
- Quality: {gevurah.get('gevurah_quality', 'N/A')}
- Key Risks: {', '.join([r.get('risk', '')[:50] for r in gevurah.get('risks', {}).get('short_term', [])[:2]])}
- Red Lines: {len(gevurah.get('red_lines', []))}
"""

        return f"""You are TIFERET (תפארת), Beauty/Harmony - Sefira 6 of the Kabbalistic Tree.

FUNCTION: Synthesize the expansive force of CHESED with the restrictive force of GEVURAH into a harmonious, balanced path forward.

SCENARIO TO ANALYZE:
{scenario}
{chesed_context}
{gevurah_context}

YOUR TASK:
Create a BEAUTIFUL SYNTHESIS that honors both the opportunities (Chesed) and the constraints (Gevurah), finding the optimal balanced path.

CRITICAL PRINCIPLES:
1. **SYNTHESIS**: Integrate expansion and restriction into coherent whole
2. **BALANCE**: Find the golden mean between opportunity and caution
3. **TRADE-OFFS**: Explicitly navigate key trade-offs with wisdom
4. **OPTIMAL PATH**: Recommend specific path that maximizes value while respecting limits
5. **HARMONY**: Create elegant solution where both forces serve higher purpose

IMPORTANT: You are NOT choosing between Chesed and Gevurah - you are SYNTHESIZING them. The goal is not compromise (losing from both sides) but TRANSCENDENCE (gaining something neither alone could achieve).

RESPONSE (JSON only, no markdown):
{{
    "synthesis_points": [
        {{
            "synthesis": "How opportunity X can be pursued WHILE respecting constraint Y",
            "chesed_element": "Specific opportunity from Chesed",
            "gevurah_element": "Specific constraint/risk from Gevurah",
            "integrated_approach": "How to honor both simultaneously",
            "value_created": "What this synthesis achieves"
        }},
        {{
            "synthesis": "How risk mitigation creates new opportunities",
            "chesed_element": "Opportunity element",
            "gevurah_element": "Risk/constraint element",
            "integrated_approach": "Integration strategy",
            "value_created": "Value of synthesis"
        }},
        {{
            "synthesis": "Third synthesis point",
            "chesed_element": "Opportunity",
            "gevurah_element": "Constraint",
            "integrated_approach": "How to integrate",
            "value_created": "Value"
        }},
        {{
            "synthesis": "Fourth synthesis point",
            "chesed_element": "Opportunity",
            "gevurah_element": "Constraint",
            "integrated_approach": "Integration",
            "value_created": "Value"
        }}
    ],

    "balanced_recommendations": [
        {{
            "recommendation": "Specific balanced recommendation #1",
            "opportunity_honored": "How this captures Chesed's opportunities",
            "constraint_respected": "How this respects Gevurah's limits",
            "implementation": "Concrete implementation approach",
            "expected_outcome": "What this achieves"
        }},
        {{
            "recommendation": "Balanced recommendation #2",
            "opportunity_honored": "Opportunity aspect",
            "constraint_respected": "Constraint aspect",
            "implementation": "How to implement",
            "expected_outcome": "Expected result"
        }},
        {{
            "recommendation": "Balanced recommendation #3",
            "opportunity_honored": "Opportunity",
            "constraint_respected": "Constraint",
            "implementation": "Implementation",
            "expected_outcome": "Outcome"
        }}
    ],

    "trade_offs": [
        {{
            "trade_off": "Key trade-off #1 (e.g., speed vs safety)",
            "tension": "What's in tension between Chesed and Gevurah",
            "recommended_position": "Where to position on this spectrum (0-100, where 0=pure Gevurah, 100=pure Chesed)",
            "rationale": "Why this position is optimal",
            "conditions": "Under what conditions to adjust this position"
        }},
        {{
            "trade_off": "Key trade-off #2",
            "tension": "What's in tension",
            "recommended_position": 60,
            "rationale": "Why this balance",
            "conditions": "When to adjust"
        }},
        {{
            "trade_off": "Key trade-off #3",
            "tension": "Tension description",
            "recommended_position": 45,
            "rationale": "Rationale",
            "conditions": "Adjustment conditions"
        }}
    ],

    "optimal_path": {{
        "strategic_direction": "Overall strategic direction that balances expansion and caution",
        "phase_1": {{
            "focus": "Initial phase focus (typically more Gevurah - establish foundations)",
            "duration": "Timeframe",
            "key_actions": ["Action 1", "Action 2", "Action 3"],
            "success_criteria": ["Criterion 1", "Criterion 2"]
        }},
        "phase_2": {{
            "focus": "Growth phase (typically more Chesed - expand within boundaries)",
            "duration": "Timeframe",
            "key_actions": ["Action 1", "Action 2", "Action 3"],
            "success_criteria": ["Criterion 1", "Criterion 2"]
        }},
        "phase_3": {{
            "focus": "Mature phase (dynamic balance based on feedback)",
            "duration": "Timeframe",
            "key_actions": ["Action 1", "Action 2"],
            "success_criteria": ["Criterion 1", "Criterion 2"]
        }},
        "ongoing_balancing": "How to maintain balance over time through feedback loops"
    }},

    "integration_strategy": "Comprehensive paragraph describing HOW to integrate Chesed and Gevurah in practice. What systems, processes, or governance structures enable both expansion and restraint? How to create dynamic equilibrium rather than static compromise?",

    "harmony_assessment": "Assessment of how naturally Chesed and Gevurah harmonize in this scenario. Are they fundamentally aligned (easy synthesis) or in deep tension (difficult balance requiring careful navigation)? What makes synthesis easier or harder here?",

    "beauty_quotient": "low/moderate/high/exceptional"
}}

CRITICAL RULES:
- Create at least 4 synthesis points integrating Chesed and Gevurah
- Provide at least 3 balanced recommendations
- Navigate at least 3 key trade-offs with specific position recommendations
- Design optimal path with at least 3 phases
- Integration strategy must be comprehensive (2-3 paragraphs minimum)
- Focus on TRANSCENDENT SYNTHESIS, not mere compromise
- Be SPECIFIC and ACTIONABLE
- Return ONLY valid JSON, no markdown formatting

Remember: Tiferet is where opposites unite to create something more beautiful than either alone. True beauty is balanced power."""

    def _calculate_harmony_score(self, result: Dict[str, Any]) -> float:
        """Calculate harmony score based on quality of synthesis"""
        score = 0.0

        # Synthesis points (max 30 points)
        synthesis_count = len(result.get('synthesis_points', []))
        score += min(synthesis_count * 7.5, 30)

        # Balanced recommendations (max 25 points)
        recommendations_count = len(result.get('balanced_recommendations', []))
        score += min(recommendations_count * 8.33, 25)

        # Trade-offs navigated (max 20 points)
        tradeoffs_count = len(result.get('trade_offs', []))
        score += min(tradeoffs_count * 6.67, 20)

        # Optimal path phases (max 15 points)
        optimal_path = result.get('optimal_path', {})
        phases_defined = sum([1 for p in ['phase_1', 'phase_2', 'phase_3'] if p in optimal_path])
        score += min(phases_defined * 5, 15)

        # Integration strategy depth (max 10 points)
        integration_length = len(result.get('integration_strategy', ''))
        if integration_length > 600:
            score += 10
        elif integration_length > 400:
            score += 7
        elif integration_length > 200:
            score += 4

        return min(score, 100.0)

    def _calculate_balance_ratio(self, result: Dict[str, Any], previous_results: Optional[Dict[str, Any]]) -> str:
        """Calculate balance ratio between Chesed and Gevurah"""
        if not previous_results:
            return "unknown"

        chesed_score = previous_results.get('chesed', {}).get('expansion_score', 50)
        gevurah_score = previous_results.get('gevurah', {}).get('severity_score', 50)

        total = chesed_score + gevurah_score
        if total == 0:
            return "balanced (50:50)"

        chesed_pct = int((chesed_score / total) * 100)
        gevurah_pct = 100 - chesed_pct

        if abs(chesed_pct - gevurah_pct) < 10:
            return f"well-balanced ({chesed_pct}:{gevurah_pct})"
        elif chesed_pct > gevurah_pct:
            return f"expansion-leaning ({chesed_pct}:{gevurah_pct})"
        else:
            return f"constraint-leaning ({chesed_pct}:{gevurah_pct})"

    def _assess_synthesis_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of synthesis"""
        harmony_score = self._calculate_harmony_score(result)
        synthesis_count = len(result.get('synthesis_points', []))
        tradeoffs_count = len(result.get('trade_offs', []))

        if harmony_score >= 80 and synthesis_count >= 4 and tradeoffs_count >= 3:
            return "exceptional"
        elif harmony_score >= 65 and synthesis_count >= 3:
            return "high"
        elif harmony_score >= 50 and synthesis_count >= 2:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Tiferet"""
        avg_syntheses = (
            self.total_syntheses_generated / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_balances = (
            self.total_balances_achieved / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_syntheses_generated": self.total_syntheses_generated,
            "total_balances_achieved": self.total_balances_achieved,
            "avg_syntheses_per_activation": round(avg_syntheses, 2),
            "avg_balances_per_activation": round(avg_balances, 2),
            "harmonic_synthesis_maintained": avg_syntheses >= 3.0
        }


# CLI interface
if __name__ == "__main__":
    import io

    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print(f"Usage: python {os.path.basename(__file__)} '<scenario>'")
        print(f"Example: python {os.path.basename(__file__)} 'Should we implement UBI?'")
        sys.exit(1)

    scenario = sys.argv[1]

    print("=" * 80)
    print("TIFERET - Belleza - Sefira 6")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Chesed and Gevurah results
    mock_previous = {
        'chesed': {
            'opportunities': [
                {'opportunity': 'Poverty reduction through guaranteed income'},
                {'opportunity': 'Economic security enabling entrepreneurship'},
                {'opportunity': 'Increased bargaining power for workers'}
            ],
            'expansion_score': 85.0,
            'opportunity_count': 5,
            'chesed_quality': 'high'
        },
        'gevurah': {
            'risks': {
                'short_term': [
                    {'risk': 'Inflationary pressure from increased demand'},
                    {'risk': 'Political opposition and implementation challenges'}
                ],
                'medium_term': [],
                'long_term': []
            },
            'red_lines': [
                {'red_line': 'Must not create poverty trap'},
                {'red_line': 'Must be fiscally sustainable'},
                {'red_line': 'Must preserve work incentives'}
            ],
            'severity_score': 65.0,
            'risk_count': 7,
            'gevurah_quality': 'high'
        }
    }

    tiferet = Tiferet()
    result = tiferet.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(tiferet.get_metrics(), indent=2))
