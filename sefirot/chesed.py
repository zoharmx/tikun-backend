"""
Chesed (חסד) - Misericordia - Sefirá 4
Identificación de oportunidades, beneficios, expansión positiva
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


class Chesed:
    """
    Chesed - Misericordia - Sefirá 4

    Function: Identificación de oportunidades, beneficios, expansión positiva
    Input: Escenario + Binah synthesis
    Output: Opportunities, benefits, expansion potential, abundance mindset

    Métricas clave:
    - expansion_score: Potencial de expansión positiva (0-100%)
    - opportunity_count: Número de oportunidades identificadas
    - benefit_coverage: Amplitud de beneficios (individuos/grupos/sociedad)
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Chesed"""
        self.name = "chesed"
        self.hebrew_name = "חסד"
        self.position = 4
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_opportunities_identified = 0
        self.total_benefits_mapped = 0
        self.total_beneficiaries_reached = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Chesed

        Args:
            scenario: Description of the scenario
            previous_results: Results from previous Sefirot (especially Binah)

        Returns:
            Dictionary with Chesed analysis including:
            - opportunities: Specific opportunities identified
            - benefits: Benefits for different stakeholder groups
            - expansion_potential: Areas for positive expansion
            - abundance_mindset: Generative possibilities
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.7)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            opportunities_count = len(result.get('opportunities', []))
            benefits_count = sum([len(b.get('specific_benefits', [])) for b in result.get('benefits_by_stakeholder', [])])
            beneficiaries_count = len(result.get('benefits_by_stakeholder', []))

            self.activation_count += 1
            self.total_opportunities_identified += opportunities_count
            self.total_benefits_mapped += benefits_count
            self.total_beneficiaries_reached += beneficiaries_count

            # Calculate expansion score
            expansion_score = self._calculate_expansion_score(result)

            # Assess benefit coverage
            benefit_coverage = self._assess_benefit_coverage(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "opportunities": result.get('opportunities', []),
                "benefits_by_stakeholder": result.get('benefits_by_stakeholder', []),
                "expansion_potential": result.get('expansion_potential', {}),
                "abundance_mindset": result.get('abundance_mindset', []),
                "synergies": result.get('synergies', []),
                "generative_possibilities": result.get('generative_possibilities', ''),
                "expansion_score": round(expansion_score, 2),
                "opportunity_count": opportunities_count,
                "benefit_coverage": benefit_coverage,
                "chesed_quality": self._assess_chesed_quality(result),
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
        """Build prompt for Chesed"""

        binah_context = ""
        if previous_results and 'binah' in previous_results:
            binah = previous_results['binah']
            stakeholders_summary = ', '.join([s.get('name', '') for s in binah.get('stakeholders', [])[:3]])
            synthesis_snippet = binah.get('synthesis', '')[:400]
            binah_context = f"""
BINAH CONTEXT (Understanding):
- Stakeholders Identified: {stakeholders_summary}
- Contextual Depth Score: {binah.get('contextual_depth_score', 'N/A')}
- Temporal Horizon: {binah.get('temporal_horizon', 'N/A')}
- Synthesis Snippet: {synthesis_snippet}...
"""

        return f"""You are CHESED (חסד), Mercy/Loving-kindness - Sefira 4 of the Kabbalistic Tree.

FUNCTION: Identify opportunities, benefits, and positive expansion potential through the lens of abundance and generosity.

SCENARIO TO ANALYZE:
{scenario}
{binah_context}

YOUR TASK:
Provide COMPREHENSIVE OPPORTUNITY ANALYSIS from the perspective of CHESED - the expansive force of generosity, growth, and positive potential.

CRITICAL PRINCIPLES:
1. **OPPORTUNITY IDENTIFICATION**: Find ALL opportunities for positive impact, growth, and benefit
2. **BENEFIT MAPPING**: Map benefits to specific stakeholders with detail
3. **EXPANSION POTENTIAL**: Identify areas where expansion would create value
4. **ABUNDANCE MINDSET**: Think generatively - what new possibilities could emerge?
5. **SYNERGIES**: Find synergies between different opportunities

RESPONSE (JSON only, no markdown):
{{
    "opportunities": [
        {{
            "opportunity": "Specific opportunity #1",
            "description": "What this opportunity entails in detail",
            "potential_impact": "high/medium/low",
            "timeframe": "immediate/short-term/medium-term/long-term",
            "feasibility": "high/medium/low",
            "beneficiaries": ["Stakeholder group 1", "Stakeholder group 2"],
            "success_indicators": ["Measurable indicator 1", "Measurable indicator 2"]
        }},
        {{
            "opportunity": "Specific opportunity #2",
            "description": "What this opportunity entails",
            "potential_impact": "high/medium/low",
            "timeframe": "immediate/short-term/medium-term/long-term",
            "feasibility": "high/medium/low",
            "beneficiaries": ["Stakeholder group 3"],
            "success_indicators": ["Measurable indicator 1", "Measurable indicator 2"]
        }},
        {{
            "opportunity": "Specific opportunity #3",
            "description": "What this opportunity entails",
            "potential_impact": "high/medium/low",
            "timeframe": "immediate/short-term/medium-term/long-term",
            "feasibility": "high/medium/low",
            "beneficiaries": ["Stakeholder group 4"],
            "success_indicators": ["Measurable indicator 1"]
        }},
        {{
            "opportunity": "Specific opportunity #4",
            "description": "What this opportunity entails",
            "potential_impact": "high/medium/low",
            "timeframe": "immediate/short-term/medium-term/long-term",
            "feasibility": "high/medium/low",
            "beneficiaries": ["Stakeholder group 5"],
            "success_indicators": ["Measurable indicator 1"]
        }},
        {{
            "opportunity": "Specific opportunity #5",
            "description": "What this opportunity entails",
            "potential_impact": "high/medium/low",
            "timeframe": "immediate/short-term/medium-term/long-term",
            "feasibility": "high/medium/low",
            "beneficiaries": ["Stakeholder group 6"],
            "success_indicators": ["Measurable indicator 1"]
        }}
    ],

    "benefits_by_stakeholder": [
        {{
            "stakeholder_group": "Stakeholder Group 1",
            "specific_benefits": [
                {{
                    "benefit": "Specific tangible benefit",
                    "type": "economic/social/health/educational/environmental/political",
                    "magnitude": "transformative/significant/moderate/minor",
                    "confidence": "high/medium/low"
                }},
                {{
                    "benefit": "Another specific benefit",
                    "type": "economic/social/health/educational/environmental/political",
                    "magnitude": "transformative/significant/moderate/minor",
                    "confidence": "high/medium/low"
                }}
            ],
            "aggregate_impact": "Overall positive impact on this stakeholder group"
        }},
        {{
            "stakeholder_group": "Stakeholder Group 2",
            "specific_benefits": [
                {{
                    "benefit": "Specific benefit for this group",
                    "type": "economic/social/health/educational/environmental/political",
                    "magnitude": "transformative/significant/moderate/minor",
                    "confidence": "high/medium/low"
                }}
            ],
            "aggregate_impact": "Overall positive impact on this stakeholder group"
        }},
        {{
            "stakeholder_group": "Society at Large",
            "specific_benefits": [
                {{
                    "benefit": "Systemic benefit to society",
                    "type": "social/environmental/political",
                    "magnitude": "transformative/significant/moderate/minor",
                    "confidence": "medium/low"
                }}
            ],
            "aggregate_impact": "Broad societal benefit"
        }}
    ],

    "expansion_potential": {{
        "areas_for_growth": [
            {{
                "area": "Specific area where expansion is possible",
                "current_state": "Description of current state",
                "expansion_path": "How to expand from current to desired state",
                "value_created": "What value expansion would create"
            }},
            {{
                "area": "Another area for expansion",
                "current_state": "Description of current state",
                "expansion_path": "How to expand",
                "value_created": "Value created"
            }}
        ],
        "scalability_potential": "Assessment of how scalable the scenario/intervention is",
        "multiplicative_effects": "How benefits might multiply over time or across domains"
    }},

    "abundance_mindset": [
        "Generative possibility #1 - something NEW that could emerge",
        "Generative possibility #2 - unexpected positive outcome",
        "Generative possibility #3 - long-term transformation potential",
        "Generative possibility #4 - catalyst effect (triggering other positive changes)"
    ],

    "synergies": [
        {{
            "synergy": "Synergy between opportunities X and Y",
            "description": "How these opportunities reinforce each other",
            "amplification_factor": "How much more value is created together vs separately"
        }},
        {{
            "synergy": "Another synergy",
            "description": "How these opportunities reinforce each other",
            "amplification_factor": "Additional value created"
        }}
    ],

    "generative_possibilities": "Paragraph describing the GENERATIVE POTENTIAL of this scenario. What new possibilities, innovations, or transformations could emerge if this is pursued with abundance mindset? Think beyond direct benefits to cascading positive effects.",

    "expansion_rating": "low/moderate/high/exceptional"
}}

CRITICAL RULES:
- Identify at least 5 concrete opportunities with clear success indicators
- Map benefits to at least 3 stakeholder groups
- Identify at least 2 areas for expansion
- Provide at least 4 generative possibilities (abundance mindset)
- Find at least 2 synergies between opportunities
- Be SPECIFIC and CONCRETE, not vague or generic
- Focus on POSITIVE POTENTIAL (this is Chesed - the expansive force)
- Return ONLY valid JSON, no markdown formatting

Remember: Chesed sees possibilities where others see limitations. Abundance, not scarcity."""

    def _calculate_expansion_score(self, result: Dict[str, Any]) -> float:
        """Calculate expansion score based on opportunities and potential"""
        score = 0.0

        # Opportunities count and quality (max 30 points)
        opportunities = result.get('opportunities', [])
        high_impact_opps = sum(1 for o in opportunities if o.get('potential_impact') == 'high')
        score += min(len(opportunities) * 5, 20)  # 5 points per opportunity, max 20
        score += min(high_impact_opps * 5, 10)  # Bonus for high-impact opportunities

        # Benefits coverage (max 25 points)
        benefits_count = sum([len(b.get('specific_benefits', [])) for b in result.get('benefits_by_stakeholder', [])])
        score += min(benefits_count * 3, 25)

        # Expansion potential (max 20 points)
        expansion_areas = len(result.get('expansion_potential', {}).get('areas_for_growth', []))
        score += min(expansion_areas * 10, 20)

        # Abundance mindset (max 15 points)
        abundance_count = len(result.get('abundance_mindset', []))
        score += min(abundance_count * 3.75, 15)

        # Synergies identified (max 10 points)
        synergies_count = len(result.get('synergies', []))
        score += min(synergies_count * 5, 10)

        return min(score, 100.0)

    def _assess_benefit_coverage(self, result: Dict[str, Any]) -> str:
        """Assess breadth of benefit coverage"""
        stakeholder_groups = len(result.get('benefits_by_stakeholder', []))

        if stakeholder_groups >= 5:
            return "comprehensive (5+ groups)"
        elif stakeholder_groups >= 3:
            return "broad (3-4 groups)"
        elif stakeholder_groups >= 1:
            return "focused (1-2 groups)"
        else:
            return "limited"

    def _assess_chesed_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Chesed analysis"""
        expansion_score = self._calculate_expansion_score(result)
        opportunities_count = len(result.get('opportunities', []))
        synergies_count = len(result.get('synergies', []))

        if expansion_score >= 80 and opportunities_count >= 5 and synergies_count >= 2:
            return "exceptional"
        elif expansion_score >= 65 and opportunities_count >= 4:
            return "high"
        elif expansion_score >= 50 and opportunities_count >= 3:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Chesed"""
        avg_opportunities = (
            self.total_opportunities_identified / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_benefits = (
            self.total_benefits_mapped / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_beneficiaries = (
            self.total_beneficiaries_reached / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_opportunities_identified": self.total_opportunities_identified,
            "total_benefits_mapped": self.total_benefits_mapped,
            "total_beneficiaries_reached": self.total_beneficiaries_reached,
            "avg_opportunities_per_activation": round(avg_opportunities, 2),
            "avg_benefits_per_activation": round(avg_benefits, 2),
            "avg_beneficiaries_per_activation": round(avg_beneficiaries, 2),
            "expansive_thinking_maintained": avg_opportunities >= 4.0
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
    print("CHESED - Misericordia - Sefira 4")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Binah result
    mock_previous = {
        'binah': {
            'stakeholders': [
                {'name': 'Unemployed Workers'},
                {'name': 'Taxpayers'},
                {'name': 'Government'}
            ],
            'synthesis': 'UBI presents complex multi-dimensional challenge with opportunities for positive impact...',
            'contextual_depth_score': 95.0,
            'temporal_horizon': 'comprehensive (0-20 years)'
        }
    }

    chesed = Chesed()
    result = chesed.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(chesed.get_metrics(), indent=2))
