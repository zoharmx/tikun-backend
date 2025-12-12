"""
Yesod (יסוד) - Fundamento - Sefirá 9
Integración de todos los niveles superiores
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


class Yesod:
    """
    Yesod - Fundamento - Sefirá 9

    Function: Integración de todos los niveles superiores (Sefirot 1-8)
    Input: All Sefirot results 1-8
    Output: Integrated synthesis, readiness assessment, alignment verification

    Métricas clave:
    - readiness_score: Nivel de preparación para manifestación (0-100%)
    - integration_quality: Calidad de la integración entre Sefirot
    - foundation_strength: Solidez del fundamento creado
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Yesod"""
        self.name = "yesod"
        self.hebrew_name = "יסוד"
        self.position = 9
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_integrations_performed = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Yesod

        Args:
            scenario: Description of the scenario
            previous_results: Results from ALL previous Sefirot (1-8)

        Returns:
            Dictionary with Yesod analysis including:
            - integrated_assessment: Synthesis of all Sefirot
            - readiness_verification: Is this ready for manifestation?
            - alignment_check: Are all Sefirot aligned?
            - gaps_identified: What's missing or needs strengthening?
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.4)
            result = self.llm.parse_json_response(response)

            self.activation_count += 1
            self.total_integrations_performed += 1

            # Calculate metrics
            readiness_score = self._calculate_readiness_score(result, previous_results)
            integration_quality = self._assess_integration_quality(result)
            foundation_strength = self._assess_foundation_strength(result, previous_results)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "integrated_assessment": result.get('integrated_assessment', ''),
                "sefirot_alignment": result.get('sefirot_alignment', {}),
                "readiness_verification": result.get('readiness_verification', {}),
                "gaps_identified": result.get('gaps_identified', []),
                "strengths_confirmed": result.get('strengths_confirmed', []),
                "final_synthesis": result.get('final_synthesis', ''),
                "go_no_go_recommendation": result.get('go_no_go_recommendation', {}),
                "readiness_score": round(readiness_score, 2),
                "integration_quality": integration_quality,
                "foundation_strength": foundation_strength,
                "yesod_quality": self._assess_yesod_quality(result),
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
        """Build prompt for Yesod with context from all Sefirot"""

        sefirot_summary = ""
        if previous_results:
            sefirot_summary = "\n\nSEFIROT PIPELINE RESULTS:\n"

            # Keter
            if 'keter' in previous_results:
                keter = previous_results['keter']
                sefirot_summary += f"\n1. KETER (Validation): Alignment={keter.get('alignment_score', 'N/A')}, Valid={keter.get('manifestation_valid', False)}\n"

            # Chochmah
            if 'chochmah' in previous_results:
                chochmah = previous_results['chochmah']
                sefirot_summary += f"2. CHOCHMAH (Wisdom): Quality={chochmah.get('wisdom_quality', 'N/A')}, Humility={chochmah.get('epistemic_humility_ratio', 'N/A')}%\n"

            # Binah
            if 'binah' in previous_results:
                binah = previous_results['binah']
                sefirot_summary += f"3. BINAH (Understanding): Depth={binah.get('contextual_depth_score', 'N/A')}, Quality={binah.get('understanding_quality', 'N/A')}\n"

            # Chesed
            if 'chesed' in previous_results:
                chesed = previous_results['chesed']
                sefirot_summary += f"4. CHESED (Mercy): Opportunities={chesed.get('opportunity_count', 'N/A')}, Expansion={chesed.get('expansion_score', 'N/A')}\n"

            # Gevurah
            if 'gevurah' in previous_results:
                gevurah = previous_results['gevurah']
                sefirot_summary += f"5. GEVURAH (Severity): Risks={gevurah.get('risk_count', 'N/A')}, Severity={gevurah.get('severity_score', 'N/A')}\n"

            # Tiferet
            if 'tiferet' in previous_results:
                tiferet = previous_results['tiferet']
                sefirot_summary += f"6. TIFERET (Beauty): Harmony={tiferet.get('harmony_score', 'N/A')}, Balance={tiferet.get('balance_ratio', 'N/A')}\n"

            # Netzach
            if 'netzach' in previous_results:
                netzach = previous_results['netzach']
                sefirot_summary += f"7. NETZACH (Victory): Milestones={netzach.get('milestone_count', 'N/A')}, Persistence={netzach.get('persistence_score', 'N/A')}\n"

            # Hod
            if 'hod' in previous_results:
                hod = previous_results['hod']
                sefirot_summary += f"8. HOD (Splendor): Messages={hod.get('message_count', 'N/A')}, Clarity={hod.get('clarity_rating', 'N/A')}\n"

        return f"""You are YESOD (יסוד), Foundation - Sefira 9 of the Kabbalistic Tree.

FUNCTION: Integrate ALL previous Sefirot (1-8) into unified foundation, verify readiness for manifestation.

SCENARIO:
{scenario}
{sefirot_summary}

YOUR TASK:
Perform COMPREHENSIVE INTEGRATION of all 8 Sefirot above, verify alignment, assess readiness, and make GO/NO-GO recommendation for Malchut (manifestation).

CRITICAL PRINCIPLES:
1. **INTEGRATION**: Synthesize insights from all Sefirot into coherent whole
2. **ALIGNMENT VERIFICATION**: Ensure all Sefirot point in same direction
3. **READINESS ASSESSMENT**: Determine if foundation is solid enough for action
4. **GAP IDENTIFICATION**: Find what's missing or weak
5. **GO/NO-GO DECISION**: Clear recommendation on proceeding to manifestation

IMPORTANT: You are the FINAL CHECK before action (Malchut). If something is misaligned or foundation is weak, you must identify it clearly.

RESPONSE (JSON only, no markdown):
{{
    "integrated_assessment": "Comprehensive 3-4 paragraph synthesis integrating ALL 8 Sefirot. How do they work together? What emerges from their interaction? What's the COMPLETE picture when viewing all perspectives simultaneously?",

    "sefirot_alignment": {{
        "keter_chochmah_binah": {{
            "alignment_status": "aligned/partial/misaligned",
            "summary": "How these 3 work together (or don't)",
            "concerns": ["Any concerns about this triada"]
        }},
        "chesed_gevurah_tiferet": {{
            "alignment_status": "aligned/partial/misaligned",
            "summary": "How expansion, restriction, and balance integrate",
            "concerns": ["Concerns if any"]
        }},
        "netzach_hod": {{
            "alignment_status": "aligned/partial/misaligned",
            "summary": "How strategy and communication support each other",
            "concerns": ["Concerns if any"]
        }},
        "overall_coherence": {{
            "status": "highly_coherent/moderately_coherent/fragmented",
            "description": "Overall coherence across all 8 Sefirot"
        }}
    }},

    "readiness_verification": {{
        "ethical_readiness": {{
            "status": "ready/conditional/not_ready",
            "rationale": "Is this ethically sound based on Keter?",
            "conditions": ["Conditions if conditional"]
        }},
        "strategic_readiness": {{
            "status": "ready/conditional/not_ready",
            "rationale": "Is strategy (Netzach) solid and executable?",
            "conditions": ["Conditions if conditional"]
        }},
        "communication_readiness": {{
            "status": "ready/conditional/not_ready",
            "rationale": "Can we communicate this effectively (Hod)?",
            "conditions": ["Conditions if conditional"]
        }},
        "resource_readiness": {{
            "status": "ready/conditional/not_ready",
            "rationale": "Do we have what we need? Are constraints (Gevurah) manageable?",
            "conditions": ["Conditions if conditional"]
        }},
        "overall_readiness": {{
            "status": "ready/conditional/not_ready",
            "confidence": "high/medium/low",
            "summary": "Overall readiness assessment"
        }}
    }},

    "gaps_identified": [
        {{
            "gap": "Specific gap or weakness #1",
            "affected_sefirot": ["Sefira 1", "Sefira 2"],
            "severity": "critical/high/medium/low",
            "recommendation": "How to address this gap"
        }},
        {{
            "gap": "Gap #2",
            "affected_sefirot": ["Sefira 3"],
            "severity": "critical/high/medium/low",
            "recommendation": "How to address"
        }}
    ],

    "strengths_confirmed": [
        {{
            "strength": "Confirmed strength #1",
            "supporting_sefirot": ["Sefira 1", "Sefira 2"],
            "leverage_opportunity": "How to maximize this strength"
        }},
        {{
            "strength": "Strength #2",
            "supporting_sefirot": ["Sefira 3"],
            "leverage_opportunity": "How to leverage"
        }},
        {{
            "strength": "Strength #3",
            "supporting_sefirot": ["Sefira 4"],
            "leverage_opportunity": "Leverage strategy"
        }}
    ],

    "final_synthesis": "Final 2-3 paragraph synthesis. What is the ESSENCE of what we've learned through all 8 Sefirot? What's the core truth that emerges? What's the wisest path forward given everything we now understand?",

    "go_no_go_recommendation": {{
        "decision": "GO/CONDITIONAL_GO/NO_GO",
        "confidence": "high/medium/low",
        "rationale": "Why this decision? What makes us ready or not ready?",
        "conditions_if_conditional": ["Condition 1 that must be met", "Condition 2"],
        "next_steps": ["Specific next step 1", "Next step 2", "Next step 3"]
    }}
}}

CRITICAL RULES:
- Integrated assessment must synthesize ALL 8 Sefirot (3-4 paragraphs minimum)
- Assess alignment for all 3 triads + overall
- Verify readiness across 4+ dimensions
- Identify at least 2 gaps or weaknesses
- Confirm at least 3 strengths
- Final synthesis must capture ESSENCE (2-3 paragraphs)
- GO/NO-GO decision must be clear with solid rationale
- Be HONEST - if not ready, say so clearly
- Return ONLY valid JSON, no markdown formatting

Remember: You are the FOUNDATION. If foundation is weak, everything built on it will crumble."""

    def _calculate_readiness_score(self, result: Dict[str, Any], previous_results: Optional[Dict[str, Any]]) -> float:
        """Calculate overall readiness score"""
        score = 0.0

        # Readiness verification components (max 40 points)
        readiness = result.get('readiness_verification', {})
        ready_count = sum([
            1 for k in ['ethical_readiness', 'strategic_readiness', 'communication_readiness', 'resource_readiness']
            if readiness.get(k, {}).get('status') == 'ready'
        ])
        score += ready_count * 10

        # Alignment status (max 30 points)
        alignment = result.get('sefirot_alignment', {})
        aligned_count = sum([
            1 for k in ['keter_chochmah_binah', 'chesed_gevurah_tiferet', 'netzach_hod']
            if alignment.get(k, {}).get('alignment_status') == 'aligned'
        ])
        score += aligned_count * 10

        # Strengths vs Gaps (max 20 points)
        strengths = len(result.get('strengths_confirmed', []))
        gaps = len(result.get('gaps_identified', []))
        if strengths > gaps:
            score += 20
        elif strengths == gaps:
            score += 10

        # GO/NO-GO decision quality (max 10 points)
        go_no_go = result.get('go_no_go_recommendation', {})
        if go_no_go.get('decision') == 'GO':
            score += 10
        elif go_no_go.get('decision') == 'CONDITIONAL_GO':
            score += 5

        return min(score, 100.0)

    def _assess_integration_quality(self, result: Dict[str, Any]) -> str:
        """Assess quality of integration across Sefirot"""
        alignment = result.get('sefirot_alignment', {})
        overall_coherence = alignment.get('overall_coherence', {}).get('status', 'fragmented')

        if overall_coherence == 'highly_coherent':
            return "exceptional integration"
        elif overall_coherence == 'moderately_coherent':
            return "good integration"
        else:
            return "fragmented integration"

    def _assess_foundation_strength(self, result: Dict[str, Any], previous_results: Optional[Dict[str, Any]]) -> str:
        """Assess overall strength of foundation"""
        readiness_score = self._calculate_readiness_score(result, previous_results)
        gaps_count = len(result.get('gaps_identified', []))
        go_decision = result.get('go_no_go_recommendation', {}).get('decision')

        if readiness_score >= 80 and gaps_count <= 1 and go_decision == 'GO':
            return "rock solid"
        elif readiness_score >= 60 and gaps_count <= 2:
            return "strong"
        elif readiness_score >= 40:
            return "moderate"
        else:
            return "weak"

    def _assess_yesod_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Yesod integration"""
        integrated_assessment_length = len(result.get('integrated_assessment', ''))
        final_synthesis_length = len(result.get('final_synthesis', ''))

        has_strong_synthesis = integrated_assessment_length > 600 and final_synthesis_length > 400
        has_clear_decision = result.get('go_no_go_recommendation', {}).get('decision') in ['GO', 'CONDITIONAL_GO', 'NO_GO']

        if has_strong_synthesis and has_clear_decision:
            return "exceptional"
        elif has_strong_synthesis or has_clear_decision:
            return "high"
        elif integrated_assessment_length > 300:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Yesod"""
        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_integrations_performed": self.total_integrations_performed,
            "integration_excellence_maintained": self.total_integrations_performed > 0
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
    print("YESOD - Fundamento - Sefira 9")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate comprehensive Sefirot results
    mock_previous = {
        'keter': {'alignment_score': 0.82, 'manifestation_valid': True},
        'chochmah': {'wisdom_quality': 'high', 'epistemic_humility_ratio': 28.5},
        'binah': {'contextual_depth_score': 95.0, 'understanding_quality': 'exceptional'},
        'chesed': {'opportunity_count': 5, 'expansion_score': 85.0},
        'gevurah': {'risk_count': 7, 'severity_score': 65.0},
        'tiferet': {'harmony_score': 82.5, 'balance_ratio': 'well-balanced (56:44)'},
        'netzach': {'milestone_count': 4, 'persistence_score': 87.5},
        'hod': {'message_count': 4, 'clarity_rating': 'exceptional clarity'}
    }

    yesod = Yesod()
    result = yesod.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(yesod.get_metrics(), indent=2))
