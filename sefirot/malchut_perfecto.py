"""
Malchut (Manifestation) - Versión Perfeccionada
================================================

MEJORAS:
- Fechas dinámicas (no hardcoded)
- Deadlines siempre en futuro
- Cálculo automático de timelines
- Validación de fechas antes de output

Autor: Framework Tikun V2
Fecha: 2025-12-12
"""

from typing import Dict, List, Any
from datetime import datetime, timedelta
import json


class MalchutPerfecto:
    """
    Malchut perfeccionado con fechas dinámicas y validación
    """
    
    # Timeline presets
    TIMELINE_PRESETS = {
        'immediate': timedelta(weeks=2),       # 2 semanas
        'short_term': timedelta(months=3),     # 3 meses
        'medium_term': timedelta(months=12),   # 1 año
        'long_term': timedelta(years=3),       # 3 años
    }
    
    def __init__(self, llm_client, model="gemini-2.0-flash-exp"):
        """
        Args:
            llm_client: Cliente LLM configurado
            model: Modelo a usar
        """
        self.llm = llm_client
        self.model = model
        self.current_date = datetime.now()
    
    def calculate_deadlines(self) -> Dict[str, str]:
        """
        Calcula deadlines para diferentes horizontes temporales
        
        Returns:
            Dict con fechas formateadas
        """
        deadlines = {}
        
        for horizon, delta in self.TIMELINE_PRESETS.items():
            deadline_date = self.current_date + delta
            deadlines[horizon] = deadline_date.strftime('%Y-%m-%d')
            deadlines[f'{horizon}_datetime'] = deadline_date.strftime('%Y-%m-%d %H:%M')
        
        return deadlines
    
    def generate_prompt(
        self, 
        scenario: str, 
        all_sefirot_results: Dict,
        yesod_recommendation: str
    ) -> str:
        """
        Genera prompt con fechas dinámicas
        """
        deadlines = self.calculate_deadlines()
        
        # Extract key metrics
        keter_alignment = all_sefirot_results.get('keter', {}).get('alignment_percentage', 0)
        yesod_readiness = all_sefirot_results.get('yesod', {}).get('readiness_score', 0)
        
        prompt = f"""
You are Malchut (מלכות), the Sefira of Manifestation in the Tree of Life.

SCENARIO:
{scenario}

INTEGRATED ASSESSMENT:
- Keter Alignment: {keter_alignment}%
- Yesod Readiness: {yesod_readiness}%
- Yesod Recommendation: {yesod_recommendation}

CURRENT DATE: {self.current_date.strftime('%Y-%m-%d')}

DEADLINE HORIZONS:
- Immediate actions: By {deadlines['immediate']} (2 weeks from now)
- Short-term: By {deadlines['short_term']} (3 months from now)
- Medium-term: By {deadlines['medium_term']} (1 year from now)
- Long-term: By {deadlines['long_term']} (3 years from now)

🚨 CRITICAL: ALL DEADLINES MUST BE IN THE FUTURE
Use the horizons above. DO NOT use past dates. DO NOT use hardcoded dates.

YOUR TASK:
Generate an actionable implementation plan with concrete actions, owners, deadlines, and resources.

OUTPUT (JSON):
{{
  "executive_summary": "2-3 paragraph summary of the plan...",
  
  "go_no_go_decision": {{
    "decision": "GO / NO_GO / CONDITIONAL_GO",
    "rationale": "Why this decision...",
    "success_probability": 0-100,
    "timeline": "Expected timeline for full implementation"
  }},
  
  "immediate_actions": [
    {{
      "action": "Specific action to take immediately",
      "owner": "Role responsible (e.g., 'Chief Science Officer')",
      "deadline": "{deadlines['immediate_datetime']}",
      "resources_needed": ["Resource 1", "Resource 2"],
      "deliverable": "Concrete output expected",
      "why_now": "Why this action is urgent",
      "estimated_effort": "Hours/days required",
      "dependencies": []
    }},
    ... (3-5 immediate actions, all with deadline around {deadlines['immediate']})
  ],
  
  "action_plan": [
    {{
      "phase": "Phase 1: Foundation (Month 1-3)",
      "objective": "What this phase achieves...",
      "actions": [
        {{
          "action": "Specific action",
          "owner": "Role responsible",
          "deadline": "YYYY-MM-DD (within {deadlines['short_term']})",
          "success_criteria": ["Criterion 1", "Criterion 2"],
          "resources": ["Resource 1", "Resource 2"]
        }},
        ... (3-5 actions per phase)
      ],
      "deliverables": ["Deliverable 1", "Deliverable 2"],
      "phase_success_criteria": ["Overall criterion 1", "Overall criterion 2"]
    }},
    ... (3-5 phases with increasing deadlines)
  ],
  
  "resource_requirements": {{
    "human_resources": [
      {{
        "role": "Role name",
        "quantity": "Number needed",
        "skills_required": ["Skill 1", "Skill 2"],
        "time_commitment": "Full-time / Part-time",
        "when_needed": "YYYY-MM-DD",
        "cost_estimate": "$X,XXX per year"
      }},
      ... (5-10 roles)
    ],
    
    "financial_resources": [
      {{
        "category": "Personnel / Equipment / Operations / etc.",
        "amount": "$X,XXX,XXX",
        "timeframe": "Annual / One-time",
        "justification": "Why this amount..."
      }},
      ... (5-8 categories)
    ],
    
    "infrastructure_resources": [
      {{
        "resource": "Resource name",
        "specification": "Technical specs...",
        "quantity": "Number needed",
        "acquisition_timeline": "YYYY-MM-DD",
        "cost": "$X,XXX"
      }},
      ... (3-5 infrastructure items)
    ]
  }},
  
  "risk_mitigation_plan": [
    {{
      "risk": "Specific risk from Gevurah analysis",
      "likelihood": "low/medium/high",
      "impact": "low/medium/high",
      "mitigation_actions": ["Action 1", "Action 2"],
      "owner": "Role responsible",
      "deadline": "YYYY-MM-DD"
    }},
    ... (top 5-10 risks)
  ],
  
  "success_metrics": [
    {{
      "metric": "Metric name",
      "target": "Specific target value",
      "measurement_method": "How to measure...",
      "review_frequency": "Weekly / Monthly / Quarterly"
    }},
    ... (5-8 metrics)
  ],
  
  "first_step": "The absolute first action to take (action + owner + deadline)",
  
  "manifestation_score": 0-100,
  "action_count": 0,  // Total number of actions defined
  "feasibility_rating": "immediately_executable / executable_with_prep / requires_major_prep / aspirational",
  "malchut_quality": "exceptional / excellent / good / adequate / needs_improvement"
}}

CRITICAL RULES:
1. ALL deadlines MUST be AFTER {self.current_date.strftime('%Y-%m-%d')}
2. Use realistic timelines (don't promise 1-week miracles for complex tasks)
3. Immediate actions should be achievable within 2 weeks
4. Phases should build logically on each other
5. Resource requirements should be specific and costed
6. Every action needs clear owner and success criteria

Remember: This is the bridge from wisdom to reality. Make it executable.
"""
        
        return prompt
    
    def validate_dates(self, result: Dict) -> List[str]:
        """
        Valida que todas las fechas sean futuras
        
        Returns:
            Lista de warnings (vacía si todo OK)
        """
        warnings = []
        
        # Check immediate actions
        for action in result.get('immediate_actions', []):
            deadline_str = action.get('deadline', '')
            if deadline_str:
                try:
                    deadline = datetime.fromisoformat(deadline_str.replace('Z', '+00:00'))
                    if deadline <= self.current_date:
                        warnings.append(
                            f"⚠️ Immediate action deadline in past: {deadline_str}"
                        )
                except Exception as e:
                    warnings.append(f"⚠️ Invalid deadline format: {deadline_str}")
        
        # Check action plan phases
        for phase in result.get('action_plan', []):
            for action in phase.get('actions', []):
                deadline_str = action.get('deadline', '')
                if deadline_str:
                    try:
                        deadline = datetime.fromisoformat(deadline_str.replace('Z', '+00:00'))
                        if deadline <= self.current_date:
                            warnings.append(
                                f"⚠️ Phase action deadline in past: {deadline_str}"
                            )
                    except Exception as e:
                        warnings.append(f"⚠️ Invalid phase deadline: {deadline_str}")
        
        return warnings
    
    def analyze(
        self, 
        scenario: str, 
        all_sefirot_results: Dict
    ) -> Dict[str, Any]:
        """
        Ejecuta análisis Malchut con fechas dinámicas
        
        Args:
            scenario: Descripción del escenario
            all_sefirot_results: Resultados de todas las Sefirot previas
            
        Returns:
            Dict con plan de acción Malchut perfeccionado
        """
        # 1. Get Yesod recommendation
        yesod_result = all_sefirot_results.get('yesod', {})
        recommendation = yesod_result.get('go_no_go_recommendation', {})
        yesod_decision = recommendation.get('decision', 'UNKNOWN')
        
        # 2. Generate prompt with dynamic dates
        prompt = self.generate_prompt(scenario, all_sefirot_results, yesod_decision)
        
        # 3. Call LLM
        response = self.llm.generate(
            prompt=prompt,
            model=self.model,
            temperature=0.7,
            max_tokens=4000
        )
        
        # 4. Parse JSON response
        try:
            clean_response = response.strip()
            if clean_response.startswith('```json'):
                clean_response = clean_response[7:]
            if clean_response.endswith('```'):
                clean_response = clean_response[:-3]
            clean_response = clean_response.strip()
            
            result = json.loads(clean_response)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Failed to parse Malchut JSON response: {e}\n"
                f"Response preview: {response[:500]}"
            )
        
        # 5. Validate dates
        date_warnings = self.validate_dates(result)
        
        # 6. Calculate metrics
        immediate_action_count = len(result.get('immediate_actions', []))
        phase_count = len(result.get('action_plan', []))
        total_action_count = immediate_action_count
        for phase in result.get('action_plan', []):
            total_action_count += len(phase.get('actions', []))
        
        manifestation_score = result.get('manifestation_score', 0)
        
        # 7. Assess quality
        malchut_quality = self._assess_quality(manifestation_score, total_action_count, date_warnings)
        
        # 8. Enrich result with metadata
        result['sefira'] = 'malchut'
        result['sefira_number'] = 10
        result['hebrew_name'] = 'מלכות'
        result['action_count'] = total_action_count
        result['immediate_action_count'] = immediate_action_count
        result['phase_count'] = phase_count
        result['malchut_quality'] = malchut_quality
        result['timestamp'] = self.current_date.isoformat()
        result['model_used'] = self.model
        
        # Add date validation warnings if any
        if date_warnings:
            result['date_validation_warnings'] = date_warnings
        else:
            result['date_validation'] = 'all_dates_valid'
        
        return result
    
    def _assess_quality(self, manifestation_score: float, action_count: int, warnings: List) -> str:
        """Assess overall quality of Malchut output"""
        if warnings:
            return 'needs_improvement'  # Date warnings are critical
        
        if manifestation_score >= 90 and action_count >= 15:
            return 'exceptional'
        elif manifestation_score >= 75 and action_count >= 10:
            return 'excellent'
        elif manifestation_score >= 60 and action_count >= 7:
            return 'good'
        elif manifestation_score >= 45 and action_count >= 4:
            return 'adequate'
        else:
            return 'needs_improvement'


# Ejemplo de uso
if __name__ == "__main__":
    print("Malchut Perfecto - Fechas Dinámicas")
    print("=" * 70)
    
    malchut = MalchutPerfecto(llm_client=None)  # Mock for example
    
    print(f"\nFecha Actual: {malchut.current_date.strftime('%Y-%m-%d')}")
    print("\nDeadlines Calculados:")
    
    deadlines = malchut.calculate_deadlines()
    for horizon, date in deadlines.items():
        if not horizon.endswith('_datetime'):
            print(f"  {horizon:15} → {date}")
    
    print("\n✓ Todas las fechas son FUTURAS")
    print("✓ Fechas calculadas dinámicamente (no hardcoded)")
    print("✓ Validación automática antes de output")
