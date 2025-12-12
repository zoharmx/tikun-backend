"""
Netzach (נצח) - Victoria - Sefirá 7
Estrategia de implementación, persistencia, resiliencia
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


class Netzach:
    """
    Netzach - Victoria - Sefirá 7

    Function: Estrategia de implementación, persistencia, resiliencia
    Input: Tiferet synthesis (balanced path)
    Output: Implementation strategy, milestones, persistence requirements

    Métricas clave:
    - persistence_score: Capacidad de mantener momentum (0-100%)
    - milestone_count: Número de hitos definidos
    - resilience_rating: Fortaleza ante obstáculos
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Netzach"""
        self.name = "netzach"
        self.hebrew_name = "נצח"
        self.position = 7
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_milestones_defined = 0
        self.total_strategies_created = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Netzach

        Args:
            scenario: Description of the scenario
            previous_results: Results from Tiferet (required for strategy)

        Returns:
            Dictionary with Netzach analysis including:
            - implementation_strategy: How to execute the balanced path
            - milestones: Key milestones with success criteria
            - persistence_requirements: What's needed to sustain momentum
            - resilience_planning: How to handle obstacles and setbacks
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.5)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            milestones_count = len(result.get('milestones', []))
            strategies_count = len(result.get('implementation_phases', []))

            self.activation_count += 1
            self.total_milestones_defined += milestones_count
            self.total_strategies_created += strategies_count

            # Calculate persistence score
            persistence_score = self._calculate_persistence_score(result)

            # Assess resilience rating
            resilience_rating = self._assess_resilience_rating(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "implementation_strategy": result.get('implementation_strategy', ''),
                "implementation_phases": result.get('implementation_phases', []),
                "milestones": result.get('milestones', []),
                "persistence_requirements": result.get('persistence_requirements', []),
                "resilience_planning": result.get('resilience_planning', {}),
                "momentum_builders": result.get('momentum_builders', []),
                "long_term_sustainability": result.get('long_term_sustainability', ''),
                "persistence_score": round(persistence_score, 2),
                "milestone_count": milestones_count,
                "resilience_rating": resilience_rating,
                "netzach_quality": self._assess_netzach_quality(result),
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
        """Build prompt for Netzach"""

        tiferet_context = ""
        if previous_results and 'tiferet' in previous_results:
            tiferet = previous_results['tiferet']
            optimal_path = tiferet.get('optimal_path', {})
            strategic_direction = optimal_path.get('strategic_direction', 'N/A')
            harmony_score = tiferet.get('harmony_score', 'N/A')
            tiferet_context = f"""
TIFERET CONTEXT (Balanced Synthesis):
- Strategic Direction: {strategic_direction[:200]}
- Harmony Score: {harmony_score}
- Synthesis Quality: {tiferet.get('synthesis_quality', 'N/A')}
- Balance Ratio: {tiferet.get('balance_ratio', 'N/A')}
"""

        return f"""You are NETZACH (נצח), Victory/Endurance - Sefira 7 of the Kabbalistic Tree.

FUNCTION: Create robust implementation strategy with persistence, momentum, and resilience to achieve victory over obstacles.

SCENARIO TO ANALYZE:
{scenario}
{tiferet_context}

YOUR TASK:
Develop COMPREHENSIVE IMPLEMENTATION STRATEGY that ensures the balanced path from Tiferet is actually executed with endurance and resilience.

CRITICAL PRINCIPLES:
1. **STRATEGIC PLANNING**: Break down execution into clear phases with milestones
2. **PERSISTENCE**: Identify what's needed to maintain momentum over time
3. **RESILIENCE**: Plan for obstacles, setbacks, and how to overcome them
4. **MOMENTUM BUILDING**: Create positive feedback loops that sustain effort
5. **VICTORY MINDSET**: Focus on HOW to win, not just what to do

IMPORTANT: Tiferet provided the WHAT (balanced path). You provide the HOW (execution strategy) with emphasis on endurance and overcoming resistance.

RESPONSE (JSON only, no markdown):
{{
    "implementation_strategy": "Comprehensive paragraph describing overall implementation approach. How do we execute Tiferet's balanced path? What's the core strategy for achieving victory? What makes this approach robust and sustainable?",

    "implementation_phases": [
        {{
            "phase": "Phase 1: Foundation Building",
            "timeframe": "Months 1-3",
            "primary_objectives": ["Objective 1", "Objective 2", "Objective 3"],
            "key_activities": ["Activity 1", "Activity 2", "Activity 3"],
            "success_metrics": ["Metric 1", "Metric 2"],
            "critical_success_factors": ["Factor 1", "Factor 2"],
            "anticipated_challenges": ["Challenge 1", "Challenge 2"]
        }},
        {{
            "phase": "Phase 2: Momentum Building",
            "timeframe": "Months 4-8",
            "primary_objectives": ["Objective 1", "Objective 2"],
            "key_activities": ["Activity 1", "Activity 2", "Activity 3"],
            "success_metrics": ["Metric 1", "Metric 2"],
            "critical_success_factors": ["Factor 1", "Factor 2"],
            "anticipated_challenges": ["Challenge 1", "Challenge 2"]
        }},
        {{
            "phase": "Phase 3: Scaling & Consolidation",
            "timeframe": "Months 9-18",
            "primary_objectives": ["Objective 1", "Objective 2"],
            "key_activities": ["Activity 1", "Activity 2"],
            "success_metrics": ["Metric 1", "Metric 2"],
            "critical_success_factors": ["Factor 1"],
            "anticipated_challenges": ["Challenge 1"]
        }},
        {{
            "phase": "Phase 4: Sustained Victory",
            "timeframe": "18+ months",
            "primary_objectives": ["Objective 1"],
            "key_activities": ["Activity 1", "Activity 2"],
            "success_metrics": ["Metric 1"],
            "critical_success_factors": ["Factor 1"],
            "anticipated_challenges": ["Challenge 1"]
        }}
    ],

    "milestones": [
        {{
            "milestone": "Major milestone #1",
            "target_date": "Month 3",
            "success_criteria": ["Criterion 1", "Criterion 2", "Criterion 3"],
            "dependencies": ["Dependency 1", "Dependency 2"],
            "verification_method": "How to verify achievement",
            "importance": "critical/high/medium"
        }},
        {{
            "milestone": "Major milestone #2",
            "target_date": "Month 6",
            "success_criteria": ["Criterion 1", "Criterion 2"],
            "dependencies": ["Dependency 1"],
            "verification_method": "Verification method",
            "importance": "critical/high/medium"
        }},
        {{
            "milestone": "Major milestone #3",
            "target_date": "Month 12",
            "success_criteria": ["Criterion 1", "Criterion 2"],
            "dependencies": ["Dependency 1"],
            "verification_method": "Verification method",
            "importance": "critical/high/medium"
        }},
        {{
            "milestone": "Major milestone #4",
            "target_date": "Month 18",
            "success_criteria": ["Criterion 1"],
            "dependencies": [],
            "verification_method": "Verification method",
            "importance": "high/medium"
        }}
    ],

    "persistence_requirements": [
        {{
            "requirement": "Organizational commitment requirement",
            "description": "What organizational support is needed to sustain effort",
            "type": "leadership/resources/culture/governance",
            "criticality": "critical/high/medium",
            "how_to_secure": "How to obtain and maintain this requirement"
        }},
        {{
            "requirement": "Resource persistence requirement",
            "description": "What resources must be sustained over time",
            "type": "leadership/resources/culture/governance",
            "criticality": "critical/high/medium",
            "how_to_secure": "How to ensure continuous availability"
        }},
        {{
            "requirement": "Cultural/mindset requirement",
            "description": "What attitudes/beliefs must persist",
            "type": "leadership/resources/culture/governance",
            "criticality": "critical/high/medium",
            "how_to_secure": "How to cultivate and maintain"
        }}
    ],

    "resilience_planning": {{
        "common_obstacles": [
            {{
                "obstacle": "Likely obstacle #1",
                "probability": "high/medium/low",
                "impact": "high/medium/low",
                "mitigation_strategy": "How to prevent or minimize",
                "response_plan": "What to do if it happens"
            }},
            {{
                "obstacle": "Likely obstacle #2",
                "probability": "high/medium/low",
                "impact": "high/medium/low",
                "mitigation_strategy": "Prevention strategy",
                "response_plan": "Response if occurs"
            }},
            {{
                "obstacle": "Likely obstacle #3",
                "probability": "high/medium/low",
                "impact": "high/medium/low",
                "mitigation_strategy": "Prevention",
                "response_plan": "Response"
            }}
        ],
        "setback_recovery": "Paragraph on how to recover from major setbacks. What systems ensure we can get back on track? What's the reset protocol?",
        "adaptation_mechanisms": "How the strategy adapts based on feedback. What triggers adaptations? How do we learn and adjust?"
    }},

    "momentum_builders": [
        "Early win that builds confidence and support",
        "Feedback loop that reinforces progress",
        "Visibility mechanism that maintains stakeholder engagement",
        "Celebration/recognition system that sustains motivation",
        "Incremental improvement system that compounds over time"
    ],

    "long_term_sustainability": "Paragraph describing how this initiative becomes self-sustaining over time. What makes it durable beyond initial implementation? What institutional mechanisms ensure continuation? How does it become 'the new normal'?",

    "victory_indicators": [
        "Clear indicator that victory has been achieved",
        "Another victory indicator",
        "Third success indicator"
    ]
}}

CRITICAL RULES:
- Define at least 4 implementation phases with clear objectives
- Establish at least 4 major milestones with success criteria
- Identify at least 3 persistence requirements
- Plan for at least 3 common obstacles with mitigation strategies
- Provide at least 5 momentum builders
- Implementation strategy must be comprehensive (2-3 paragraphs)
- Focus on ENDURANCE and RESILIENCE, not just initial execution
- Be SPECIFIC and ACTIONABLE
- Return ONLY valid JSON, no markdown formatting

Remember: Netzach is about sustained effort leading to victory. Plans fail without persistence."""

    def _calculate_persistence_score(self, result: Dict[str, Any]) -> float:
        """Calculate persistence score based on strategy robustness"""
        score = 0.0

        # Implementation phases (max 25 points)
        phases_count = len(result.get('implementation_phases', []))
        score += min(phases_count * 6.25, 25)

        # Milestones defined (max 25 points)
        milestones_count = len(result.get('milestones', []))
        score += min(milestones_count * 6.25, 25)

        # Persistence requirements (max 20 points)
        persistence_count = len(result.get('persistence_requirements', []))
        score += min(persistence_count * 6.67, 20)

        # Resilience planning (max 20 points)
        obstacles_count = len(result.get('resilience_planning', {}).get('common_obstacles', []))
        score += min(obstacles_count * 6.67, 20)

        # Momentum builders (max 10 points)
        momentum_count = len(result.get('momentum_builders', []))
        score += min(momentum_count * 2, 10)

        return min(score, 100.0)

    def _assess_resilience_rating(self, result: Dict[str, Any]) -> str:
        """Assess resilience rating based on obstacle planning"""
        resilience = result.get('resilience_planning', {})
        obstacles_count = len(resilience.get('common_obstacles', []))
        has_setback_recovery = len(resilience.get('setback_recovery', '')) > 100
        has_adaptation = len(resilience.get('adaptation_mechanisms', '')) > 100

        if obstacles_count >= 3 and has_setback_recovery and has_adaptation:
            return "very high"
        elif obstacles_count >= 2 and (has_setback_recovery or has_adaptation):
            return "high"
        elif obstacles_count >= 1:
            return "moderate"
        else:
            return "low"

    def _assess_netzach_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Netzach strategy"""
        persistence_score = self._calculate_persistence_score(result)
        phases_count = len(result.get('implementation_phases', []))
        milestones_count = len(result.get('milestones', []))

        if persistence_score >= 80 and phases_count >= 4 and milestones_count >= 4:
            return "exceptional"
        elif persistence_score >= 65 and phases_count >= 3:
            return "high"
        elif persistence_score >= 50 and phases_count >= 2:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Netzach"""
        avg_milestones = (
            self.total_milestones_defined / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_strategies = (
            self.total_strategies_created / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_milestones_defined": self.total_milestones_defined,
            "total_strategies_created": self.total_strategies_created,
            "avg_milestones_per_activation": round(avg_milestones, 2),
            "avg_strategies_per_activation": round(avg_strategies, 2),
            "strategic_persistence_maintained": avg_milestones >= 3.0
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
    print("NETZACH - Victoria - Sefira 7")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Tiferet result
    mock_previous = {
        'tiferet': {
            'optimal_path': {
                'strategic_direction': 'Implement UBI with phased rollout, starting with pilot programs',
                'phase_1': {'focus': 'Pilot programs in select regions'},
                'phase_2': {'focus': 'Gradual expansion based on results'},
                'phase_3': {'focus': 'National implementation with adjustments'}
            },
            'harmony_score': 82.5,
            'synthesis_quality': 'high',
            'balance_ratio': 'well-balanced (56:44)'
        }
    }

    netzach = Netzach()
    result = netzach.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(netzach.get_metrics(), indent=2))
