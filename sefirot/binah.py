"""
Binah (בינה) - Entendimiento - Sefirá 3
Análisis contextual multidimensional y síntesis
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


class Binah:
    """
    Binah - Entendimiento - Sefirá 3

    Function: Análisis contextual multidimensional y síntesis
    Input: Escenario + Keter + Chochmah results
    Output: 9-dimensional context analysis, stakeholder mapping, effects cascade

    Métricas clave:
    - contextual_depth_score: Completitud del análisis 9D (0-100%)
    - stakeholder_coverage: Cantidad de stakeholders identificados
    - temporal_horizon: Profundidad temporal del análisis (corto/medio/largo plazo)
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Binah"""
        self.name = "binah"
        self.hebrew_name = "בינה"
        self.position = 3
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_stakeholders_identified = 0
        self.total_dimensions_analyzed = 0
        self.total_effects_mapped = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Binah

        Args:
            scenario: Description of the scenario
            previous_results: Results from Keter and Chochmah (required for context)

        Returns:
            Dictionary with Binah analysis including:
            - context_9d: 9-dimensional context analysis
            - stakeholders: Stakeholder mapping with impact analysis
            - effects_cascade: 1st, 2nd, 3rd order effects
            - systemic_risks: Systemic risks identification
            - synthesis: Comprehensive synthesis
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.5)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            dimensions_count = len(result.get('context_9d', []))
            stakeholders_count = len(result.get('stakeholders', []))
            effects_count = sum([
                len(result.get('effects_cascade', {}).get('first_order', [])),
                len(result.get('effects_cascade', {}).get('second_order', [])),
                len(result.get('effects_cascade', {}).get('third_order', []))
            ])

            self.activation_count += 1
            self.total_dimensions_analyzed += dimensions_count
            self.total_stakeholders_identified += stakeholders_count
            self.total_effects_mapped += effects_count

            # Calculate contextual depth score
            contextual_depth_score = self._calculate_contextual_depth(result)

            # Assess temporal horizon
            temporal_horizon = self._assess_temporal_horizon(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "context_9d": result.get('context_9d', []),
                "stakeholders": result.get('stakeholders', []),
                "effects_cascade": result.get('effects_cascade', {}),
                "systemic_risks": result.get('systemic_risks', []),
                "ethical_considerations": result.get('ethical_considerations', []),
                "synthesis": result.get('synthesis', ''),
                "contextual_depth_score": round(contextual_depth_score, 2),
                "stakeholder_coverage": stakeholders_count,
                "temporal_horizon": temporal_horizon,
                "understanding_quality": self._assess_understanding_quality(result),
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
        """Build prompt for Binah"""

        keter_context = ""
        chochmah_context = ""

        if previous_results:
            if 'keter' in previous_results:
                keter = previous_results['keter']
                keter_context = f"""
KETER CONTEXT:
- Alignment Score: {keter.get('alignment_score', 'N/A')}
- Aligned with Tikun Olam: {keter.get('manifestation_valid', False)}
- Corruption Severity: {keter.get('corruption_severity', 'N/A')}
"""

            if 'chochmah' in previous_results:
                chochmah = previous_results['chochmah']
                insights_summary = ', '.join(chochmah.get('insights', [])[:3])
                patterns_summary = ', '.join([p.get('pattern_name', '') for p in chochmah.get('patterns', [])[:2]])
                chochmah_context = f"""
CHOCHMAH CONTEXT:
- Key Insights: {insights_summary}...
- Patterns Identified: {patterns_summary}
- Uncertainties Count: {len(chochmah.get('uncertainties', []))}
- Wisdom Quality: {chochmah.get('wisdom_quality', 'N/A')}
"""

        return f"""You are BINAH (בינה), Understanding - Sefira 3 of the Kabbalistic Tree.

FUNCTION: Deep contextual understanding through 9-dimensional analysis, stakeholder mapping, and effects cascade modeling.

SCENARIO TO ANALYZE:
{scenario}
{keter_context}
{chochmah_context}

YOUR TASK:
Provide COMPREHENSIVE CONTEXTUAL UNDERSTANDING of this scenario through systematic multi-dimensional analysis.

CRITICAL PRINCIPLES:
1. **9-DIMENSIONAL CONTEXT ANALYSIS**: Analyze ALL 9 dimensions systematically
2. **STAKEHOLDER MAPPING**: Identify ALL affected parties with impact assessment
3. **EFFECTS CASCADE**: Map 1st → 2nd → 3rd order effects with confidence levels
4. **SYSTEMIC RISKS**: Identify emergent systemic risks beyond individual effects
5. **SYNTHESIS**: Generate coherent understanding integrating all dimensions

THE 9 DIMENSIONS YOU MUST ANALYZE:

1. **Historical Context**: Relevant historical background, precedents, evolution
2. **Cultural Context**: Cultural norms, values, beliefs, sensitivities affected
3. **Economic Context**: Economic systems, incentives, resources, distribution
4. **Political Context**: Power structures, governance, policies, stakeholders
5. **Social Context**: Social dynamics, relationships, community impacts
6. **Technological Context**: Tech capabilities, dependencies, disruptions
7. **Environmental Context**: Environmental impacts, sustainability, resources
8. **Legal/Regulatory Context**: Laws, regulations, compliance, rights
9. **Ethical Context**: Moral principles, values conflicts, dilemmas

RESPONSE (JSON only, no markdown):
{{
    "context_9d": [
        {{
            "dimension": "Historical Context",
            "analysis": "Detailed analysis of historical dimension (2-3 sentences)",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 8
        }},
        {{
            "dimension": "Cultural Context",
            "analysis": "Detailed analysis of cultural dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 7
        }},
        {{
            "dimension": "Economic Context",
            "analysis": "Detailed analysis of economic dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 9
        }},
        {{
            "dimension": "Political Context",
            "analysis": "Detailed analysis of political dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 8
        }},
        {{
            "dimension": "Social Context",
            "analysis": "Detailed analysis of social dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 7
        }},
        {{
            "dimension": "Technological Context",
            "analysis": "Detailed analysis of technological dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 6
        }},
        {{
            "dimension": "Environmental Context",
            "analysis": "Detailed analysis of environmental dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 5
        }},
        {{
            "dimension": "Legal/Regulatory Context",
            "analysis": "Detailed analysis of legal/regulatory dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 7
        }},
        {{
            "dimension": "Ethical Context",
            "analysis": "Detailed analysis of ethical dimension",
            "key_factors": ["Factor 1", "Factor 2", "Factor 3"],
            "relevance_score": 9
        }}
    ],

    "stakeholders": [
        {{
            "name": "Primary Stakeholder Group 1",
            "description": "Who they are and their role",
            "impact_level": "high/medium/low",
            "impact_type": "positive/negative/mixed",
            "power_level": "high/medium/low",
            "interests": ["Interest 1", "Interest 2"],
            "vulnerabilities": ["Vulnerability 1", "Vulnerability 2"]
        }},
        {{
            "name": "Primary Stakeholder Group 2",
            "description": "Who they are and their role",
            "impact_level": "high/medium/low",
            "impact_type": "positive/negative/mixed",
            "power_level": "high/medium/low",
            "interests": ["Interest 1", "Interest 2"],
            "vulnerabilities": ["Vulnerability 1", "Vulnerability 2"]
        }},
        {{
            "name": "Secondary Stakeholder Group",
            "description": "Who they are and their role",
            "impact_level": "medium/low",
            "impact_type": "positive/negative/mixed",
            "power_level": "medium/low",
            "interests": ["Interest 1"],
            "vulnerabilities": ["Vulnerability 1"]
        }}
    ],

    "effects_cascade": {{
        "first_order": [
            {{
                "effect": "Direct immediate effect 1",
                "affected_stakeholders": ["Stakeholder 1", "Stakeholder 2"],
                "timeframe": "Immediate (0-6 months)",
                "confidence": "high/medium/low"
            }},
            {{
                "effect": "Direct immediate effect 2",
                "affected_stakeholders": ["Stakeholder 3"],
                "timeframe": "Short-term (6-12 months)",
                "confidence": "high/medium/low"
            }},
            {{
                "effect": "Direct immediate effect 3",
                "affected_stakeholders": ["Stakeholder 4"],
                "timeframe": "Immediate (0-6 months)",
                "confidence": "high/medium/low"
            }}
        ],
        "second_order": [
            {{
                "effect": "Indirect consequence triggered by 1st order effects",
                "caused_by": "First order effect 1",
                "affected_stakeholders": ["Stakeholder 5"],
                "timeframe": "Medium-term (1-3 years)",
                "confidence": "medium/low"
            }},
            {{
                "effect": "Systemic response or adaptation",
                "caused_by": "First order effect 2",
                "affected_stakeholders": ["Stakeholder 6"],
                "timeframe": "Medium-term (1-3 years)",
                "confidence": "medium/low"
            }}
        ],
        "third_order": [
            {{
                "effect": "Emergent cultural/social shift",
                "caused_by": "Second order effects combination",
                "affected_stakeholders": ["Society at large"],
                "timeframe": "Long-term (3-10 years)",
                "confidence": "low"
            }},
            {{
                "effect": "Paradigm shift or structural transformation",
                "caused_by": "Feedback loops from 2nd order",
                "affected_stakeholders": ["Future generations"],
                "timeframe": "Long-term (5-20 years)",
                "confidence": "low"
            }}
        ]
    }},

    "systemic_risks": [
        {{
            "risk": "Systemic risk 1 (emergent from interactions)",
            "description": "How this systemic risk emerges",
            "severity": "high/medium/low",
            "likelihood": "high/medium/low",
            "affected_systems": ["System 1", "System 2"]
        }},
        {{
            "risk": "Systemic risk 2 (feedback loops)",
            "description": "How feedback loops create this risk",
            "severity": "high/medium/low",
            "likelihood": "high/medium/low",
            "affected_systems": ["System 3"]
        }}
    ],

    "ethical_considerations": [
        {{
            "consideration": "Primary ethical consideration",
            "dilemma": "Core ethical dilemma or tension",
            "principles_involved": ["Justice", "Autonomy", "Beneficence"],
            "trade_offs": "What values are in tension"
        }},
        {{
            "consideration": "Secondary ethical consideration",
            "dilemma": "Additional ethical complexity",
            "principles_involved": ["Equity", "Dignity"],
            "trade_offs": "What must be balanced"
        }}
    ],

    "synthesis": "Comprehensive synthesis integrating all 9 dimensions, stakeholder dynamics, effects cascades, and systemic risks. This should provide a HOLISTIC UNDERSTANDING of the scenario in 3-4 paragraphs, revealing how different dimensions interact and influence each other.",

    "contextual_complexity_rating": "low/medium/high/extreme"
}}

CRITICAL RULES:
- You MUST analyze ALL 9 dimensions (no exceptions)
- Identify at least 3 stakeholder groups with detailed impact analysis
- Map at least 3 first-order, 2 second-order, and 2 third-order effects
- Identify at least 2 systemic risks (emergent, not just individual effects)
- Synthesis must integrate findings across all dimensions (3-4 paragraphs minimum)
- Return ONLY valid JSON, no markdown formatting

Remember: Understanding requires seeing the WHOLE system, not just isolated parts."""

    def _calculate_contextual_depth(self, result: Dict[str, Any]) -> float:
        """Calculate contextual depth score based on completeness"""
        score = 0.0

        # 9D Analysis completeness (max 40 points)
        dimensions_analyzed = len(result.get('context_9d', []))
        score += min((dimensions_analyzed / 9) * 40, 40)

        # Stakeholder coverage (max 20 points)
        stakeholders_count = len(result.get('stakeholders', []))
        if stakeholders_count >= 5:
            score += 20
        elif stakeholders_count >= 3:
            score += 15
        elif stakeholders_count >= 1:
            score += 10

        # Effects cascade depth (max 20 points)
        effects = result.get('effects_cascade', {})
        first_order_count = len(effects.get('first_order', []))
        second_order_count = len(effects.get('second_order', []))
        third_order_count = len(effects.get('third_order', []))

        if third_order_count >= 2 and second_order_count >= 2 and first_order_count >= 3:
            score += 20
        elif second_order_count >= 2 and first_order_count >= 3:
            score += 15
        elif first_order_count >= 3:
            score += 10

        # Synthesis quality (max 10 points)
        synthesis_length = len(result.get('synthesis', ''))
        if synthesis_length > 800:
            score += 10
        elif synthesis_length > 500:
            score += 7
        elif synthesis_length > 300:
            score += 5

        # Systemic risks identified (max 10 points)
        systemic_risks_count = len(result.get('systemic_risks', []))
        score += min(systemic_risks_count * 5, 10)

        return min(score, 100.0)

    def _assess_temporal_horizon(self, result: Dict[str, Any]) -> str:
        """Assess temporal horizon coverage"""
        effects = result.get('effects_cascade', {})

        has_immediate = len(effects.get('first_order', [])) > 0
        has_medium = len(effects.get('second_order', [])) > 0
        has_long = len(effects.get('third_order', [])) > 0

        if has_immediate and has_medium and has_long:
            return "comprehensive (0-20 years)"
        elif has_immediate and has_medium:
            return "medium-term (0-5 years)"
        elif has_immediate:
            return "short-term (0-2 years)"
        else:
            return "limited"

    def _assess_understanding_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of understanding"""
        depth_score = self._calculate_contextual_depth(result)
        dimensions_count = len(result.get('context_9d', []))
        stakeholders_count = len(result.get('stakeholders', []))

        if depth_score >= 80 and dimensions_count == 9 and stakeholders_count >= 4:
            return "exceptional"
        elif depth_score >= 65 and dimensions_count >= 7 and stakeholders_count >= 3:
            return "high"
        elif depth_score >= 50 and dimensions_count >= 5:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Binah"""
        avg_dimensions = (
            self.total_dimensions_analyzed / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_stakeholders = (
            self.total_stakeholders_identified / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_effects = (
            self.total_effects_mapped / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_dimensions_analyzed": self.total_dimensions_analyzed,
            "total_stakeholders_identified": self.total_stakeholders_identified,
            "total_effects_mapped": self.total_effects_mapped,
            "avg_dimensions_per_activation": round(avg_dimensions, 2),
            "avg_stakeholders_per_activation": round(avg_stakeholders, 2),
            "avg_effects_per_activation": round(avg_effects, 2),
            "full_9d_coverage": avg_dimensions >= 9.0
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
    print("BINAH - Entendimiento - Sefira 3")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Keter and Chochmah results
    mock_previous = {
        'keter': {
            'alignment_score': 0.75,
            'manifestation_valid': True,
            'corruption_severity': 'minor',
            'reasoning': 'Potential for positive impact...'
        },
        'chochmah': {
            'insights': [
                'UBI could address automation displacement',
                'Historical precedents show mixed results',
                'Requires careful implementation design'
            ],
            'patterns': [
                {'pattern_name': 'Welfare State Evolution'},
                {'pattern_name': 'Economic Transition Challenges'}
            ],
            'uncertainties': [
                'Unknown behavioral responses to guaranteed income',
                'Uncertain macroeconomic effects',
                'Political feasibility unclear'
            ],
            'wisdom_quality': 'high'
        }
    }

    binah = Binah()
    result = binah.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(binah.get_metrics(), indent=2))
