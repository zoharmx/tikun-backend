"""
Malchut (מלכות) - Reino - Sefirá 10
Plan de acción concreto, manifestación en la realidad
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


class Malchut:
    """
    Malchut - Reino - Sefirá 10

    Function: Manifestación concreta, plan de acción ejecutable
    Input: Yesod integration (required for comprehensive action plan)
    Output: Concrete action plan, implementation steps, resource allocation

    Métricas clave:
    - manifestation_score: Nivel de concreción del plan (0-100%)
    - action_count: Número de acciones específicas definidas
    - feasibility_rating: Viabilidad de ejecución inmediata
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Malchut"""
        self.name = "malchut"
        self.hebrew_name = "מלכות"
        self.position = 10
        self.llm = get_llm_for_sefira(self.name)
        self.activation_count = 0
        self.total_actions_planned = 0
        self.total_resources_allocated = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Malchut

        Args:
            scenario: Description of the scenario
            previous_results: Results from Yesod (required for action planning)

        Returns:
            Dictionary with Malchut analysis including:
            - action_plan: Concrete step-by-step implementation plan
            - immediate_actions: What to do NOW (first 30 days)
            - resource_requirements: Detailed resource allocation
            - timeline: Specific dates and deadlines
            - success_metrics: How to measure progress
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.3)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            actions_count = len(result.get('immediate_actions', []))
            resources_count = len(result.get('resource_requirements', []))

            self.activation_count += 1
            self.total_actions_planned += actions_count
            self.total_resources_allocated += resources_count

            # Calculate manifestation score
            manifestation_score = self._calculate_manifestation_score(result)

            # Assess feasibility
            feasibility_rating = self._assess_feasibility_rating(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "executive_summary": result.get('executive_summary', ''),
                "go_no_go_decision": result.get('go_no_go_decision', {}),
                "immediate_actions": result.get('immediate_actions', []),
                "action_plan": result.get('action_plan', []),
                "resource_requirements": result.get('resource_requirements', {}),
                "timeline": result.get('timeline', {}),
                "success_metrics": result.get('success_metrics', []),
                "governance_structure": result.get('governance_structure', {}),
                "risk_mitigation_execution": result.get('risk_mitigation_execution', []),
                "first_step": result.get('first_step', ''),
                "manifestation_score": round(manifestation_score, 2),
                "action_count": actions_count,
                "feasibility_rating": feasibility_rating,
                "malchut_quality": self._assess_malchut_quality(result),
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
        """Build prompt for Malchut"""

        yesod_context = ""
        if previous_results and 'yesod' in previous_results:
            yesod = previous_results['yesod']
            readiness = yesod.get('overall_readiness', {})
            recommendation = yesod.get('recommendation', {})
            yesod_context = f"""
YESOD CONTEXT (Integration & Readiness):
- Integration Score: {yesod.get('integration_score', 'N/A')}
- Coherence Level: {yesod.get('coherence_level', 'N/A')}
- Readiness Decision: {recommendation.get('decision', 'N/A')}
- Key Strengths: {', '.join(yesod.get('strengths', [])[:3])}
- Key Gaps: {', '.join(yesod.get('gaps', [])[:3])}
- Ethical Readiness: {readiness.get('ethical_readiness', 'N/A')}
- Strategic Readiness: {readiness.get('strategic_readiness', 'N/A')}
"""

        return f"""You are MALCHUT (מלכות), Kingdom/Manifestation - Sefira 10 of the Kabbalistic Tree.

FUNCTION: Convert all analysis into CONCRETE ACTION PLAN that manifests in physical reality. You are the final step - where wisdom becomes deed.

SCENARIO TO ANALYZE:
{scenario}
{yesod_context}

YOUR TASK:
Create COMPREHENSIVE ACTION PLAN that is IMMEDIATELY EXECUTABLE. This is where theory meets practice.

CRITICAL PRINCIPLES:
1. **CONCRETE**: Every action must be specific, measurable, actionable
2. **IMMEDIATE**: Define what happens in the next 24 hours, 7 days, 30 days
3. **RESOURCED**: Specify exactly what/who/when/where/how much
4. **TRACKABLE**: Clear success metrics and accountability
5. **GROUNDED**: Must work in REAL WORLD with real constraints

IMPORTANT: Yesod verified readiness. You now convert that readiness into ACTION. Every action must be implementable TODAY.

RESPONSE (JSON only, no markdown):
{{
    "executive_summary": "Comprehensive 2-3 paragraph summary of the ENTIRE plan. What are we doing? Why now? What's the expected outcome? What makes this plan executable?",

    "go_no_go_decision": {{
        "decision": "GO/NO-GO/CONDITIONAL_GO",
        "confidence_level": "very high/high/moderate/low",
        "rationale": "Why this decision now based on Yesod readiness assessment",
        "conditions_if_conditional": ["Condition 1 that must be met", "Condition 2"],
        "timeline_to_decision": "If conditional, when to make final GO/NO-GO"
    }},

    "immediate_actions": [
        {{
            "action": "Specific immediate action #1 (within 24-48 hours)",
            "owner": "Who is responsible (role/person)",
            "deadline": "Exact deadline (YYYY-MM-DD HH:MM)",
            "resources_needed": ["Resource 1", "Resource 2"],
            "deliverable": "What concrete output/result",
            "why_now": "Why this must happen immediately",
            "estimated_effort": "X hours/days",
            "dependencies": ["Dependency 1 if any"]
        }},
        {{
            "action": "Immediate action #2 (within 7 days)",
            "owner": "Responsible party",
            "deadline": "Deadline",
            "resources_needed": ["Resources"],
            "deliverable": "Deliverable",
            "why_now": "Why immediate",
            "estimated_effort": "Effort",
            "dependencies": []
        }},
        {{
            "action": "Immediate action #3 (within 30 days)",
            "owner": "Owner",
            "deadline": "Deadline",
            "resources_needed": ["Resources"],
            "deliverable": "Deliverable",
            "why_now": "Why now",
            "estimated_effort": "Effort",
            "dependencies": []
        }},
        {{
            "action": "Immediate action #4",
            "owner": "Owner",
            "deadline": "Deadline",
            "resources_needed": ["Resources"],
            "deliverable": "Deliverable",
            "why_now": "Why important now",
            "estimated_effort": "Effort",
            "dependencies": []
        }}
    ],

    "action_plan": [
        {{
            "phase": "Phase 1: Foundation (Months 1-3)",
            "objective": "Clear objective for this phase",
            "actions": [
                {{
                    "action": "Specific action 1.1",
                    "owner": "Owner",
                    "deadline": "YYYY-MM-DD",
                    "success_criteria": ["Criterion 1", "Criterion 2"],
                    "resources": ["Resource 1", "Resource 2"]
                }},
                {{
                    "action": "Action 1.2",
                    "owner": "Owner",
                    "deadline": "Date",
                    "success_criteria": ["Criterion"],
                    "resources": ["Resource"]
                }},
                {{
                    "action": "Action 1.3",
                    "owner": "Owner",
                    "deadline": "Date",
                    "success_criteria": ["Criterion"],
                    "resources": ["Resource"]
                }}
            ],
            "deliverables": ["Deliverable 1", "Deliverable 2"],
            "phase_success_criteria": ["Overall phase criterion 1", "Criterion 2"]
        }},
        {{
            "phase": "Phase 2: Execution (Months 4-9)",
            "objective": "Phase objective",
            "actions": [
                {{
                    "action": "Action 2.1",
                    "owner": "Owner",
                    "deadline": "Date",
                    "success_criteria": ["Criterion"],
                    "resources": ["Resource"]
                }},
                {{
                    "action": "Action 2.2",
                    "owner": "Owner",
                    "deadline": "Date",
                    "success_criteria": ["Criterion"],
                    "resources": ["Resource"]
                }}
            ],
            "deliverables": ["Deliverable"],
            "phase_success_criteria": ["Criterion"]
        }},
        {{
            "phase": "Phase 3: Scaling (Months 10-18)",
            "objective": "Phase objective",
            "actions": [
                {{
                    "action": "Action 3.1",
                    "owner": "Owner",
                    "deadline": "Date",
                    "success_criteria": ["Criterion"],
                    "resources": ["Resource"]
                }}
            ],
            "deliverables": ["Deliverable"],
            "phase_success_criteria": ["Criterion"]
        }}
    ],

    "resource_requirements": {{
        "human_resources": [
            {{
                "role": "Role/position needed",
                "quantity": "Number needed",
                "skills_required": ["Skill 1", "Skill 2"],
                "time_commitment": "Full-time/part-time/hours per week",
                "when_needed": "Start date",
                "cost_estimate": "Annual cost or hourly rate"
            }},
            {{
                "role": "Another role",
                "quantity": "Number",
                "skills_required": ["Skills"],
                "time_commitment": "Commitment",
                "when_needed": "When",
                "cost_estimate": "Cost"
            }}
        ],
        "financial_resources": [
            {{
                "category": "Budget category (personnel/technology/marketing/etc)",
                "amount": "Specific dollar amount",
                "timeframe": "When needed (one-time/monthly/annual)",
                "justification": "Why this amount",
                "priority": "critical/high/medium/low"
            }},
            {{
                "category": "Another category",
                "amount": "Amount",
                "timeframe": "Timeframe",
                "justification": "Justification",
                "priority": "Priority"
            }}
        ],
        "technological_resources": [
            {{
                "resource": "Specific tool/platform/infrastructure",
                "purpose": "What it's for",
                "cost": "Cost estimate",
                "timeline": "When to acquire/implement",
                "alternatives": ["Alternative option 1", "Alternative 2"]
            }}
        ],
        "physical_resources": [
            {{
                "resource": "Office space/equipment/materials",
                "quantity": "How much/many",
                "cost": "Cost",
                "when_needed": "Timeline",
                "sourcing_plan": "How to acquire"
            }}
        ]
    }},

    "timeline": {{
        "start_date": "YYYY-MM-DD",
        "key_milestones": [
            {{
                "milestone": "First major milestone",
                "target_date": "YYYY-MM-DD",
                "deliverables": ["Deliverable 1", "Deliverable 2"],
                "gate_criteria": ["Criterion to proceed", "Criterion 2"],
                "responsible_party": "Who owns this milestone"
            }},
            {{
                "milestone": "Second milestone",
                "target_date": "Date",
                "deliverables": ["Deliverable"],
                "gate_criteria": ["Criterion"],
                "responsible_party": "Owner"
            }},
            {{
                "milestone": "Third milestone",
                "target_date": "Date",
                "deliverables": ["Deliverable"],
                "gate_criteria": ["Criterion"],
                "responsible_party": "Owner"
            }}
        ],
        "review_cadence": "How often to review progress (weekly/bi-weekly/monthly)",
        "adjustment_protocol": "How to adjust plan based on feedback and results"
    }},

    "success_metrics": [
        {{
            "metric": "Specific measurable metric #1",
            "target_value": "Specific target (number, percentage, etc)",
            "measurement_method": "How to measure",
            "measurement_frequency": "How often to measure",
            "owner": "Who tracks this",
            "milestone_targets": {{
                "30_days": "Target at 30 days",
                "90_days": "Target at 90 days",
                "6_months": "Target at 6 months",
                "12_months": "Target at 12 months"
            }}
        }},
        {{
            "metric": "Metric #2",
            "target_value": "Target",
            "measurement_method": "Method",
            "measurement_frequency": "Frequency",
            "owner": "Owner",
            "milestone_targets": {{
                "30_days": "Target",
                "90_days": "Target",
                "6_months": "Target",
                "12_months": "Target"
            }}
        }},
        {{
            "metric": "Metric #3",
            "target_value": "Target",
            "measurement_method": "Method",
            "measurement_frequency": "Frequency",
            "owner": "Owner",
            "milestone_targets": {{
                "30_days": "Target",
                "90_days": "Target",
                "6_months": "Target",
                "12_months": "Target"
            }}
        }}
    ],

    "governance_structure": {{
        "decision_authority": "Who has final decision-making authority",
        "steering_committee": [
            {{
                "role": "Role on committee",
                "responsibilities": ["Responsibility 1", "Responsibility 2"],
                "decision_scope": "What they can decide"
            }},
            {{
                "role": "Another role",
                "responsibilities": ["Responsibility"],
                "decision_scope": "Scope"
            }}
        ],
        "reporting_structure": "How progress is reported up the chain",
        "escalation_process": "How to escalate issues and blockers",
        "meeting_cadence": "How often governance meets"
    }},

    "risk_mitigation_execution": [
        {{
            "risk": "Top risk from Gevurah that needs mitigation NOW",
            "mitigation_action": "Specific action to mitigate",
            "owner": "Who owns mitigation",
            "deadline": "When to complete",
            "resources_allocated": ["Resources for mitigation"],
            "success_indicator": "How to know mitigation worked"
        }},
        {{
            "risk": "Second risk",
            "mitigation_action": "Action",
            "owner": "Owner",
            "deadline": "Deadline",
            "resources_allocated": ["Resources"],
            "success_indicator": "Indicator"
        }},
        {{
            "risk": "Third risk",
            "mitigation_action": "Action",
            "owner": "Owner",
            "deadline": "Deadline",
            "resources_allocated": ["Resources"],
            "success_indicator": "Indicator"
        }}
    ],

    "first_step": "THE SINGLE MOST IMPORTANT ACTION TO TAKE IN THE NEXT 24 HOURS. Be hyper-specific: Who does what, when, where, how. This is the action that starts everything.",

    "implementation_confidence": "very high/high/moderate/low"
}}

CRITICAL RULES:
- Define at least 4 immediate actions (24 hours to 30 days)
- Create at least 3 action plan phases with specific actions
- Specify at least 2 human resource requirements
- Identify at least 2 financial resource categories
- Set at least 3 key milestones with dates
- Define at least 3 success metrics with milestone targets
- Specify at least 3 risk mitigation execution items
- First step must be HYPER-SPECIFIC and executable in 24 hours
- ALL dates must be realistic and specific (YYYY-MM-DD format)
- ALL costs must be estimated (even if rough)
- ALL actions must have clear owners
- Focus on EXECUTABLE, CONCRETE, IMMEDIATE action
- Return ONLY valid JSON, no markdown formatting

Remember: Malchut is where vision becomes reality. A plan that isn't executed is just a dream. Make it REAL."""

    def _calculate_manifestation_score(self, result: Dict[str, Any]) -> float:
        """Calculate manifestation score based on plan concreteness"""
        score = 0.0

        # Immediate actions (max 25 points)
        immediate_count = len(result.get('immediate_actions', []))
        score += min(immediate_count * 6.25, 25)

        # Action plan phases (max 20 points)
        phases_count = len(result.get('action_plan', []))
        score += min(phases_count * 6.67, 20)

        # Resource requirements completeness (max 20 points)
        resources = result.get('resource_requirements', {})
        resource_categories = len([k for k in ['human_resources', 'financial_resources', 'technological_resources', 'physical_resources'] if k in resources])
        score += min(resource_categories * 5, 20)

        # Timeline milestones (max 15 points)
        milestones_count = len(result.get('timeline', {}).get('key_milestones', []))
        score += min(milestones_count * 5, 15)

        # Success metrics (max 10 points)
        metrics_count = len(result.get('success_metrics', []))
        score += min(metrics_count * 3.33, 10)

        # First step defined (max 10 points)
        first_step_length = len(result.get('first_step', ''))
        if first_step_length > 100:
            score += 10
        elif first_step_length > 50:
            score += 6
        elif first_step_length > 20:
            score += 3

        return min(score, 100.0)

    def _assess_feasibility_rating(self, result: Dict[str, Any]) -> str:
        """Assess feasibility of immediate execution"""
        immediate_count = len(result.get('immediate_actions', []))
        has_resources = len(result.get('resource_requirements', {})) >= 2
        has_first_step = len(result.get('first_step', '')) > 50

        # Check if immediate actions have owners
        actions_with_owners = sum([1 for a in result.get('immediate_actions', []) if len(a.get('owner', '')) > 0])

        if immediate_count >= 4 and has_resources and has_first_step and actions_with_owners >= 3:
            return "immediately executable"
        elif immediate_count >= 3 and (has_resources or has_first_step):
            return "executable with minor preparation"
        elif immediate_count >= 2:
            return "requires preparation"
        else:
            return "needs further planning"

    def _assess_malchut_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Malchut action plan"""
        manifestation_score = self._calculate_manifestation_score(result)
        immediate_count = len(result.get('immediate_actions', []))
        milestones_count = len(result.get('timeline', {}).get('key_milestones', []))

        if manifestation_score >= 85 and immediate_count >= 4 and milestones_count >= 3:
            return "exceptional"
        elif manifestation_score >= 70 and immediate_count >= 3:
            return "high"
        elif manifestation_score >= 55 and immediate_count >= 2:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Malchut"""
        avg_actions = (
            self.total_actions_planned / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_resources = (
            self.total_resources_allocated / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_actions_planned": self.total_actions_planned,
            "total_resources_allocated": self.total_resources_allocated,
            "avg_actions_per_activation": round(avg_actions, 2),
            "avg_resources_per_activation": round(avg_resources, 2),
            "concrete_manifestation_maintained": avg_actions >= 3.0
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
    print("MALCHUT - Reino - Sefira 10")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Yesod result
    mock_previous = {
        'yesod': {
            'integration_score': 88.5,
            'coherence_level': 'very high',
            'recommendation': {
                'decision': 'GO',
                'confidence_level': 'high'
            },
            'strengths': ['Strong ethical foundation', 'Comprehensive strategy', 'Clear communication plan'],
            'gaps': ['Resource allocation needs refinement'],
            'overall_readiness': {
                'ethical_readiness': 'ready',
                'strategic_readiness': 'ready'
            }
        }
    }

    malchut = Malchut()
    result = malchut.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(malchut.get_metrics(), indent=2))
