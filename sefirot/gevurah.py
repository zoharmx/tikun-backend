"""
Gevurah (גבורה) - Severidad - Sefirá 5
Identificación de límites, riesgos, restricciones necesarias
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


class Gevurah:
    """
    Gevurah - Severidad - Sefirá 5

    Function: Identificación de límites, riesgos, restricciones necesarias
    Input: Escenario + Binah + Chesed
    Output: Constraints, risks, boundaries, severity score, red lines

    Métricas clave:
    - severity_score: Nivel de severidad/riesgo global (0-100%)
    - risk_count: Número de riesgos identificados
    - boundary_strength: Fortaleza de los límites establecidos
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Gevurah"""
        self.name = "gevurah"
        self.hebrew_name = "גבורה"
        self.position = 5
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_risks_identified = 0
        self.total_constraints_mapped = 0
        self.total_redlines_defined = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Gevurah

        Args:
            scenario: Description of the scenario
            previous_results: Results from previous Sefirot (especially Binah and Chesed)

        Returns:
            Dictionary with Gevurah analysis including:
            - risks: Multi-temporal risk analysis (short/medium/long term)
            - constraints: Necessary constraints and limitations
            - boundaries: Hard boundaries that must not be crossed
            - red_lines: Ethical and practical red lines
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.3)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            risks_count = sum([
                len(result.get('risks', {}).get('short_term', [])),
                len(result.get('risks', {}).get('medium_term', [])),
                len(result.get('risks', {}).get('long_term', []))
            ])
            constraints_count = len(result.get('constraints', []))
            redlines_count = len(result.get('red_lines', []))

            self.activation_count += 1
            self.total_risks_identified += risks_count
            self.total_constraints_mapped += constraints_count
            self.total_redlines_defined += redlines_count

            # Calculate severity score
            severity_score = self._calculate_severity_score(result)

            # Assess boundary strength
            boundary_strength = self._assess_boundary_strength(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "risks": result.get('risks', {}),
                "constraints": result.get('constraints', []),
                "boundaries": result.get('boundaries', []),
                "red_lines": result.get('red_lines', []),
                "failure_modes": result.get('failure_modes', []),
                "mitigation_requirements": result.get('mitigation_requirements', []),
                "guardrails": result.get('guardrails', ''),
                "severity_score": round(severity_score, 2),
                "risk_count": risks_count,
                "boundary_strength": boundary_strength,
                "gevurah_quality": self._assess_gevurah_quality(result),
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
        """Build prompt for Gevurah"""

        chesed_context = ""
        binah_context = ""

        if previous_results:
            if 'chesed' in previous_results:
                chesed = previous_results['chesed']
                opp_summary = ', '.join([o.get('opportunity', '')[:40] for o in chesed.get('opportunities', [])[:3]])
                chesed_context = f"""
CHESED CONTEXT (Opportunities/Expansion):
- Opportunities Identified: {opp_summary}...
- Expansion Score: {chesed.get('expansion_score', 'N/A')}
- Opportunity Count: {chesed.get('opportunity_count', 'N/A')}
- Chesed Quality: {chesed.get('chesed_quality', 'N/A')}
"""

            if 'binah' in previous_results:
                binah = previous_results['binah']
                systemic_risks = ', '.join([r.get('risk', '')[:40] for r in binah.get('systemic_risks', [])[:2]])
                binah_context = f"""
BINAH CONTEXT (Understanding):
- Systemic Risks Identified: {systemic_risks}...
- Contextual Depth: {binah.get('contextual_depth_score', 'N/A')}
"""

        return f"""You are GEVURAH (גבורה), Severity/Judgment - Sefira 5 of the Kabbalistic Tree.

FUNCTION: Identify risks, constraints, boundaries, and necessary limitations through rigorous critical analysis.

SCENARIO TO ANALYZE:
{scenario}
{chesed_context}
{binah_context}

YOUR TASK:
Provide COMPREHENSIVE RISK AND CONSTRAINT ANALYSIS from the perspective of GEVURAH - the restrictive force that sets boundaries, identifies dangers, and establishes necessary limits.

CRITICAL PRINCIPLES:
1. **MULTI-TEMPORAL RISK ANALYSIS**: Identify risks across short, medium, and long-term horizons
2. **CONSTRAINT IDENTIFICATION**: Map necessary constraints and limitations
3. **BOUNDARY SETTING**: Establish hard boundaries that must not be crossed
4. **RED LINES**: Define ethical and practical red lines
5. **FAILURE MODES**: Anticipate ways this could fail catastrophically

IMPORTANT: While Chesed focuses on opportunities and expansion, YOU focus on what could go wrong, what limits are needed, and where boundaries must be drawn. This is not pessimism - it's PRUDENT JUDGMENT.

RESPONSE (JSON only, no markdown):
{{
    "risks": {{
        "short_term": [
            {{
                "risk": "Specific short-term risk (0-2 years)",
                "description": "Detailed description of the risk",
                "likelihood": "high/medium/low",
                "severity": "critical/high/medium/low",
                "affected_stakeholders": ["Stakeholder 1", "Stakeholder 2"],
                "indicators": ["Early warning sign 1", "Early warning sign 2"]
            }},
            {{
                "risk": "Another short-term risk",
                "description": "Description",
                "likelihood": "high/medium/low",
                "severity": "critical/high/medium/low",
                "affected_stakeholders": ["Stakeholder 3"],
                "indicators": ["Warning sign"]
            }},
            {{
                "risk": "Third short-term risk",
                "description": "Description",
                "likelihood": "high/medium/low",
                "severity": "critical/high/medium/low",
                "affected_stakeholders": ["Stakeholder 4"],
                "indicators": ["Warning sign"]
            }}
        ],
        "medium_term": [
            {{
                "risk": "Medium-term risk (2-5 years)",
                "description": "Detailed description",
                "likelihood": "high/medium/low",
                "severity": "critical/high/medium/low",
                "affected_stakeholders": ["Stakeholder 5"],
                "indicators": ["Warning sign 1", "Warning sign 2"]
            }},
            {{
                "risk": "Another medium-term risk",
                "description": "Description",
                "likelihood": "high/medium/low",
                "severity": "critical/high/medium/low",
                "affected_stakeholders": ["Stakeholder 6"],
                "indicators": ["Warning sign"]
            }}
        ],
        "long_term": [
            {{
                "risk": "Long-term existential/structural risk (5+ years)",
                "description": "Detailed description of long-term risk",
                "likelihood": "medium/low",
                "severity": "critical/high",
                "affected_stakeholders": ["Future generations", "Society"],
                "indicators": ["Structural indicator 1", "Trend indicator 2"]
            }},
            {{
                "risk": "Another long-term risk",
                "description": "Description",
                "likelihood": "medium/low",
                "severity": "critical/high",
                "affected_stakeholders": ["Global systems"],
                "indicators": ["Indicator"]
            }}
        ]
    }},

    "constraints": [
        {{
            "constraint": "Necessary constraint #1",
            "rationale": "Why this constraint is necessary",
            "type": "resource/regulatory/technical/ethical/social",
            "flexibility": "hard/moderate/soft",
            "consequences_if_violated": "What happens if this constraint is not respected"
        }},
        {{
            "constraint": "Necessary constraint #2",
            "rationale": "Why this is needed",
            "type": "resource/regulatory/technical/ethical/social",
            "flexibility": "hard/moderate/soft",
            "consequences_if_violated": "Consequences"
        }},
        {{
            "constraint": "Necessary constraint #3",
            "rationale": "Rationale",
            "type": "resource/regulatory/technical/ethical/social",
            "flexibility": "hard/moderate/soft",
            "consequences_if_violated": "Consequences"
        }}
    ],

    "boundaries": [
        {{
            "boundary": "Hard boundary #1 - absolute limit",
            "description": "What this boundary protects",
            "justification": "Why this boundary is non-negotiable",
            "monitoring": "How to monitor compliance with this boundary"
        }},
        {{
            "boundary": "Hard boundary #2",
            "description": "What this protects",
            "justification": "Why non-negotiable",
            "monitoring": "How to monitor"
        }}
    ],

    "red_lines": [
        {{
            "red_line": "Ethical red line #1 - MUST NOT be crossed",
            "category": "ethical/legal/safety/human-rights",
            "rationale": "Why this is a red line",
            "consequences": "What happens if crossed",
            "detection": "How to detect if approaching this red line"
        }},
        {{
            "red_line": "Ethical red line #2",
            "category": "ethical/legal/safety/human-rights",
            "rationale": "Why this is a red line",
            "consequences": "Consequences if crossed",
            "detection": "How to detect"
        }},
        {{
            "red_line": "Practical red line #3",
            "category": "ethical/legal/safety/human-rights",
            "rationale": "Rationale",
            "consequences": "Consequences",
            "detection": "Detection method"
        }}
    ],

    "failure_modes": [
        {{
            "failure_mode": "Catastrophic failure scenario #1",
            "description": "How this failure would unfold",
            "probability": "high/medium/low",
            "impact": "catastrophic/severe/moderate",
            "prevention": "How to prevent this failure mode"
        }},
        {{
            "failure_mode": "Failure scenario #2",
            "description": "How this unfolds",
            "probability": "high/medium/low",
            "impact": "catastrophic/severe/moderate",
            "prevention": "Prevention strategy"
        }}
    ],

    "mitigation_requirements": [
        {{
            "requirement": "Specific mitigation requirement #1",
            "addresses_risks": ["Risk 1", "Risk 2"],
            "priority": "critical/high/medium/low",
            "implementation_complexity": "high/medium/low"
        }},
        {{
            "requirement": "Mitigation requirement #2",
            "addresses_risks": ["Risk 3"],
            "priority": "critical/high/medium/low",
            "implementation_complexity": "high/medium/low"
        }},
        {{
            "requirement": "Mitigation requirement #3",
            "addresses_risks": ["Risk 4"],
            "priority": "critical/high/medium/low",
            "implementation_complexity": "high/medium/low"
        }}
    ],

    "guardrails": "Paragraph describing the ESSENTIAL GUARDRAILS that must be in place. What systems, processes, or safeguards are absolutely necessary to prevent catastrophic outcomes? What ongoing monitoring is required?",

    "overall_risk_level": "critical/high/medium/low"
}}

CRITICAL RULES:
- Identify at least 3 short-term, 2 medium-term, and 2 long-term risks
- Define at least 3 necessary constraints with clear rationale
- Establish at least 2 hard boundaries
- Define at least 3 red lines (ethical/practical limits that must not be crossed)
- Identify at least 2 failure modes
- Provide at least 3 mitigation requirements
- Be SPECIFIC and RIGOROUS, not vague
- Focus on WHAT COULD GO WRONG (this is Gevurah - the restrictive force)
- Use LOW temperature thinking - be precise and careful
- Return ONLY valid JSON, no markdown formatting

Remember: Gevurah establishes necessary limits. Expansion without boundaries leads to chaos."""

    def _calculate_severity_score(self, result: Dict[str, Any]) -> float:
        """Calculate overall severity/risk score"""
        score = 0.0

        # Risk assessment (max 40 points)
        risks = result.get('risks', {})
        critical_risks = 0
        high_risks = 0

        for timeframe in ['short_term', 'medium_term', 'long_term']:
            for risk in risks.get(timeframe, []):
                if risk.get('severity') == 'critical':
                    critical_risks += 1
                elif risk.get('severity') == 'high':
                    high_risks += 1

        score += min(critical_risks * 10, 25)  # Critical risks add heavily
        score += min(high_risks * 5, 15)  # High risks add moderately

        # Red lines identified (max 20 points)
        redlines_count = len(result.get('red_lines', []))
        score += min(redlines_count * 6.67, 20)

        # Constraints mapped (max 15 points)
        constraints_count = len(result.get('constraints', []))
        score += min(constraints_count * 5, 15)

        # Failure modes anticipated (max 15 points)
        failure_modes_count = len(result.get('failure_modes', []))
        score += min(failure_modes_count * 7.5, 15)

        # Mitigation requirements (max 10 points)
        mitigation_count = len(result.get('mitigation_requirements', []))
        score += min(mitigation_count * 3.33, 10)

        return min(score, 100.0)

    def _assess_boundary_strength(self, result: Dict[str, Any]) -> str:
        """Assess strength of boundaries established"""
        boundaries_count = len(result.get('boundaries', []))
        redlines_count = len(result.get('red_lines', []))
        constraints_count = len(result.get('constraints', []))

        total_boundaries = boundaries_count + redlines_count + constraints_count

        if total_boundaries >= 10:
            return "very strong (10+ boundaries)"
        elif total_boundaries >= 7:
            return "strong (7-9 boundaries)"
        elif total_boundaries >= 5:
            return "moderate (5-6 boundaries)"
        else:
            return "weak (< 5 boundaries)"

    def _assess_gevurah_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Gevurah analysis"""
        severity_score = self._calculate_severity_score(result)
        risk_count = sum([
            len(result.get('risks', {}).get('short_term', [])),
            len(result.get('risks', {}).get('medium_term', [])),
            len(result.get('risks', {}).get('long_term', []))
        ])
        redlines_count = len(result.get('red_lines', []))

        if severity_score >= 75 and risk_count >= 7 and redlines_count >= 3:
            return "exceptional"
        elif severity_score >= 60 and risk_count >= 5:
            return "high"
        elif severity_score >= 45 and risk_count >= 3:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Gevurah"""
        avg_risks = (
            self.total_risks_identified / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_constraints = (
            self.total_constraints_mapped / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_redlines = (
            self.total_redlines_defined / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_risks_identified": self.total_risks_identified,
            "total_constraints_mapped": self.total_constraints_mapped,
            "total_redlines_defined": self.total_redlines_defined,
            "avg_risks_per_activation": round(avg_risks, 2),
            "avg_constraints_per_activation": round(avg_constraints, 2),
            "avg_redlines_per_activation": round(avg_redlines, 2),
            "critical_thinking_maintained": avg_risks >= 5.0
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
    print("GEVURAH - Severidad - Sefira 5")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Binah and Chesed results
    mock_previous = {
        'binah': {
            'systemic_risks': [
                {'risk': 'Runaway Inflation'},
                {'risk': 'Entrenched Dependency'}
            ],
            'contextual_depth_score': 95.0
        },
        'chesed': {
            'opportunities': [
                {'opportunity': 'Poverty reduction'},
                {'opportunity': 'Economic security'},
                {'opportunity': 'Innovation enablement'}
            ],
            'expansion_score': 85.0,
            'opportunity_count': 5,
            'chesed_quality': 'high'
        }
    }

    gevurah = Gevurah()
    result = gevurah.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(gevurah.get_metrics(), indent=2))
