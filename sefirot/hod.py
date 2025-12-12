"""
Hod (הוד) - Esplendor - Sefirá 8
Articulación, comunicación, documentación
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


class Hod:
    """
    Hod - Esplendor - Sefirá 8

    Function: Articulación, comunicación, documentación
    Input: Netzach strategy
    Output: Communication plan, messaging, documentation strategy

    Métricas clave:
    - splendor_score: Calidad de la articulación (0-100%)
    - clarity_rating: Claridad del messaging
    - message_count: Número de mensajes clave definidos
    """

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Hod"""
        self.name = "hod"
        self.hebrew_name = "הוד"
        self.position = 8
        self.llm = get_llm_for_sefira(self.name)  # Uses Claude Sonnet
        self.activation_count = 0
        self.total_messages_crafted = 0
        self.total_audiences_addressed = 0

    def process(self, scenario: str, previous_results: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process scenario through Hod

        Args:
            scenario: Description of the scenario
            previous_results: Results from Netzach (required for communication planning)

        Returns:
            Dictionary with Hod analysis including:
            - communication_strategy: Overall approach to communication
            - key_messages: Core messages for different audiences
            - messaging_by_stakeholder: Tailored messaging per stakeholder group
            - documentation_requirements: What needs to be documented
        """
        prompt = self._build_prompt(scenario, previous_results)

        try:
            response = self.llm.generate(prompt, temperature=0.7)
            result = self.llm.parse_json_response(response)

            # Calculate metrics
            messages_count = len(result.get('key_messages', []))
            audiences_count = len(result.get('messaging_by_stakeholder', []))

            self.activation_count += 1
            self.total_messages_crafted += messages_count
            self.total_audiences_addressed += audiences_count

            # Calculate splendor score
            splendor_score = self._calculate_splendor_score(result)

            # Assess clarity rating
            clarity_rating = self._assess_clarity_rating(result)

            return {
                "sefira": self.name,
                "sefira_number": self.position,
                "hebrew_name": self.hebrew_name,
                "communication_strategy": result.get('communication_strategy', ''),
                "key_messages": result.get('key_messages', []),
                "messaging_by_stakeholder": result.get('messaging_by_stakeholder', []),
                "narrative_arc": result.get('narrative_arc', {}),
                "documentation_requirements": result.get('documentation_requirements', []),
                "communication_channels": result.get('communication_channels', []),
                "transparency_framework": result.get('transparency_framework', ''),
                "splendor_score": round(splendor_score, 2),
                "clarity_rating": clarity_rating,
                "message_count": messages_count,
                "hod_quality": self._assess_hod_quality(result),
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
        """Build prompt for Hod"""

        netzach_context = ""
        if previous_results and 'netzach' in previous_results:
            netzach = previous_results['netzach']
            strategy_snippet = netzach.get('implementation_strategy', '')[:300]
            milestones_count = netzach.get('milestone_count', 0)
            netzach_context = f"""
NETZACH CONTEXT (Implementation Strategy):
- Implementation Strategy: {strategy_snippet}...
- Milestone Count: {milestones_count}
- Persistence Score: {netzach.get('persistence_score', 'N/A')}
- Resilience Rating: {netzach.get('resilience_rating', 'N/A')}
"""

        return f"""You are HOD (הוד), Splendor/Glory - Sefira 8 of the Kabbalistic Tree.

FUNCTION: Create clear, compelling communication that articulates the vision, strategy, and progress with elegance and precision.

SCENARIO TO ANALYZE:
{scenario}
{netzach_context}

YOUR TASK:
Design COMPREHENSIVE COMMUNICATION STRATEGY that makes complex ideas clear, builds support, and maintains transparency.

CRITICAL PRINCIPLES:
1. **CLARITY**: Make complex ideas accessible without oversimplification
2. **TAILORED MESSAGING**: Adapt communication for different stakeholders
3. **NARRATIVE ARC**: Tell a compelling story that resonates
4. **TRANSPARENCY**: Build trust through honest, clear communication
5. **DOCUMENTATION**: Create enduring records that capture wisdom

IMPORTANT: Netzach created the execution strategy. You ensure everyone understands it, supports it, and can track progress clearly.

RESPONSE (JSON only, no markdown):
{{
    "communication_strategy": "Comprehensive paragraph describing overall communication approach. What's the core narrative? How do we build understanding and support? What makes this communication strategy effective and trustworthy?",

    "key_messages": [
        {{
            "message": "Core message #1 - The Vision",
            "description": "What this message communicates",
            "talking_points": ["Point 1", "Point 2", "Point 3"],
            "emotional_appeal": "What emotion this evokes (hope/urgency/pride/trust)",
            "evidence_to_cite": ["Evidence 1", "Evidence 2"]
        }},
        {{
            "message": "Core message #2 - The Why",
            "description": "Why this matters now",
            "talking_points": ["Point 1", "Point 2", "Point 3"],
            "emotional_appeal": "Emotion evoked",
            "evidence_to_cite": ["Evidence 1", "Evidence 2"]
        }},
        {{
            "message": "Core message #3 - The Path Forward",
            "description": "How we'll achieve this",
            "talking_points": ["Point 1", "Point 2"],
            "emotional_appeal": "Emotion evoked",
            "evidence_to_cite": ["Evidence 1"]
        }},
        {{
            "message": "Core message #4 - The Benefits",
            "description": "What success looks like",
            "talking_points": ["Point 1", "Point 2"],
            "emotional_appeal": "Emotion evoked",
            "evidence_to_cite": ["Evidence 1"]
        }}
    ],

    "messaging_by_stakeholder": [
        {{
            "stakeholder_group": "Stakeholder Group 1",
            "primary_concerns": ["Concern 1", "Concern 2"],
            "tailored_message": "Message specifically for this group addressing their concerns",
            "communication_tone": "professional/empathetic/aspirational/reassuring",
            "preferred_channels": ["Channel 1", "Channel 2"],
            "frequency": "weekly/monthly/quarterly/as-needed"
        }},
        {{
            "stakeholder_group": "Stakeholder Group 2",
            "primary_concerns": ["Concern 1", "Concern 2"],
            "tailored_message": "Tailored message for this group",
            "communication_tone": "professional/empathetic/aspirational/reassuring",
            "preferred_channels": ["Channel 1", "Channel 2"],
            "frequency": "weekly/monthly/quarterly/as-needed"
        }},
        {{
            "stakeholder_group": "Stakeholder Group 3",
            "primary_concerns": ["Concern 1"],
            "tailored_message": "Message for this group",
            "communication_tone": "professional/empathetic/aspirational/reassuring",
            "preferred_channels": ["Channel 1"],
            "frequency": "monthly/quarterly"
        }},
        {{
            "stakeholder_group": "General Public",
            "primary_concerns": ["Concern 1"],
            "tailored_message": "Public-facing message",
            "communication_tone": "accessible/inspirational",
            "preferred_channels": ["Channel 1", "Channel 2"],
            "frequency": "quarterly/as-needed"
        }}
    ],

    "narrative_arc": {{
        "opening": "How we introduce this initiative. What hooks attention and builds credibility?",
        "context": "Background and why this matters now. Historical context, current challenges.",
        "vision": "Compelling picture of the desired future state. What becomes possible?",
        "journey": "Honest acknowledgment of challenges and how we'll overcome them. The path forward.",
        "call_to_action": "What we're asking stakeholders to do. How they can contribute to success.",
        "ongoing_story": "How we maintain narrative momentum over time. Celebration of milestones, adaptation to setbacks."
    }},

    "documentation_requirements": [
        {{
            "document": "Strategic Vision Document",
            "purpose": "Articulate long-term vision and rationale",
            "audience": "Leadership, key stakeholders",
            "update_frequency": "Annually or upon major strategy shifts",
            "key_sections": ["Section 1", "Section 2", "Section 3"]
        }},
        {{
            "document": "Implementation Playbook",
            "purpose": "Guide execution teams with clear instructions",
            "audience": "Implementation teams, project managers",
            "update_frequency": "Quarterly",
            "key_sections": ["Section 1", "Section 2", "Section 3"]
        }},
        {{
            "document": "Progress Dashboard",
            "purpose": "Track and communicate progress transparently",
            "audience": "All stakeholders",
            "update_frequency": "Real-time or monthly",
            "key_sections": ["Metrics", "Milestones", "Issues", "Wins"]
        }},
        {{
            "document": "Stakeholder FAQ",
            "purpose": "Address common questions and concerns",
            "audience": "All stakeholders",
            "update_frequency": "As-needed based on feedback",
            "key_sections": ["Questions by topic"]
        }}
    ],

    "communication_channels": [
        {{
            "channel": "Town Hall Meetings",
            "purpose": "Direct engagement and Q&A",
            "frequency": "Quarterly",
            "target_audience": "All stakeholders",
            "effectiveness_rating": "high/medium/low"
        }},
        {{
            "channel": "Email Updates",
            "purpose": "Regular progress updates",
            "frequency": "Monthly",
            "target_audience": "Registered stakeholders",
            "effectiveness_rating": "high/medium/low"
        }},
        {{
            "channel": "Public Website/Portal",
            "purpose": "Transparent information hub",
            "frequency": "Continuous",
            "target_audience": "General public",
            "effectiveness_rating": "high/medium/low"
        }},
        {{
            "channel": "Working Group Sessions",
            "purpose": "Deep dives with key stakeholders",
            "frequency": "Monthly/as-needed",
            "target_audience": "Subject matter experts",
            "effectiveness_rating": "high/medium/low"
        }}
    ],

    "transparency_framework": "Paragraph describing commitment to transparency. What information will be shared publicly? How will progress and challenges be communicated honestly? What mechanisms ensure accountability and trust? How do we balance transparency with appropriate confidentiality?",

    "communication_quality_indicators": [
        "Indicator of effective communication #1",
        "Indicator #2",
        "Indicator #3"
    ]
}}

CRITICAL RULES:
- Define at least 4 key messages with talking points
- Create tailored messaging for at least 4 stakeholder groups
- Design narrative arc with all 6 components
- Specify at least 4 documentation requirements
- Identify at least 4 communication channels
- Communication strategy must be comprehensive (2-3 paragraphs)
- Focus on CLARITY, RESONANCE, and TRUST
- Be SPECIFIC and ACTIONABLE
- Return ONLY valid JSON, no markdown formatting

Remember: Hod is the power of articulation. Ideas without clear communication remain unrealized."""

    def _calculate_splendor_score(self, result: Dict[str, Any]) -> float:
        """Calculate splendor score based on communication quality"""
        score = 0.0

        # Key messages (max 25 points)
        messages_count = len(result.get('key_messages', []))
        score += min(messages_count * 6.25, 25)

        # Stakeholder messaging (max 25 points)
        stakeholder_count = len(result.get('messaging_by_stakeholder', []))
        score += min(stakeholder_count * 6.25, 25)

        # Narrative arc completeness (max 20 points)
        narrative = result.get('narrative_arc', {})
        narrative_components = sum([1 for k in ['opening', 'context', 'vision', 'journey', 'call_to_action', 'ongoing_story'] if k in narrative])
        score += min(narrative_components * 3.33, 20)

        # Documentation requirements (max 20 points)
        docs_count = len(result.get('documentation_requirements', []))
        score += min(docs_count * 5, 20)

        # Communication channels (max 10 points)
        channels_count = len(result.get('communication_channels', []))
        score += min(channels_count * 2.5, 10)

        return min(score, 100.0)

    def _assess_clarity_rating(self, result: Dict[str, Any]) -> str:
        """Assess clarity of communication"""
        messages_count = len(result.get('key_messages', []))
        stakeholder_count = len(result.get('messaging_by_stakeholder', []))

        # Check if messages have talking points
        messages_with_points = sum([1 for m in result.get('key_messages', []) if len(m.get('talking_points', [])) >= 2])

        if messages_count >= 4 and stakeholder_count >= 4 and messages_with_points >= 3:
            return "exceptional clarity"
        elif messages_count >= 3 and stakeholder_count >= 3:
            return "high clarity"
        elif messages_count >= 2:
            return "moderate clarity"
        else:
            return "low clarity"

    def _assess_hod_quality(self, result: Dict[str, Any]) -> str:
        """Assess overall quality of Hod communication"""
        splendor_score = self._calculate_splendor_score(result)
        messages_count = len(result.get('key_messages', []))
        channels_count = len(result.get('communication_channels', []))

        if splendor_score >= 80 and messages_count >= 4 and channels_count >= 4:
            return "exceptional"
        elif splendor_score >= 65 and messages_count >= 3:
            return "high"
        elif splendor_score >= 50 and messages_count >= 2:
            return "moderate"
        else:
            return "low"

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Hod"""
        avg_messages = (
            self.total_messages_crafted / self.activation_count
            if self.activation_count > 0
            else 0
        )

        avg_audiences = (
            self.total_audiences_addressed / self.activation_count
            if self.activation_count > 0
            else 0
        )

        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "total_messages_crafted": self.total_messages_crafted,
            "total_audiences_addressed": self.total_audiences_addressed,
            "avg_messages_per_activation": round(avg_messages, 2),
            "avg_audiences_per_activation": round(avg_audiences, 2),
            "clear_articulation_maintained": avg_messages >= 3.0
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
    print("HOD - Esplendor - Sefira 8")
    print("=" * 80)
    print(f"Scenario: {scenario}\n")

    # Simulate Netzach result
    mock_previous = {
        'netzach': {
            'implementation_strategy': 'Phased rollout starting with pilot programs, building momentum through early wins, and scaling based on validated learning...',
            'milestone_count': 4,
            'persistence_score': 87.5,
            'resilience_rating': 'very high'
        }
    }

    hod = Hod()
    result = hod.process(scenario, mock_previous)

    if "error" in result:
        print(f"ERROR: {result['error']}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("\n" + "=" * 80)
        print("METRICS:")
        print(json.dumps(hod.get_metrics(), indent=2))
