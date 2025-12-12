"""
Binah Sigma (Understanding) - Versión Perfeccionada
===================================================

MEJORAS:
- Campos explícitos: mode, bias_delta, divergence_level
- Cálculo automático de métricas de divergencia
- Identificación de blind spots y convergence points
- Structured output para validación

Autor: Framework Tikun V2
Fecha: 2025-12-12
"""

from typing import Dict, List, Any, Tuple
from datetime import datetime
import json


class BinahSigmaPerfecto:
    """
    Binah Sigma perfeccionado con campos explícitos y métricas calculadas
    """
    
    def __init__(self, llm_west, llm_east, model_west="gemini-2.0-flash-exp", model_east="deepseek-chat"):
        """
        Args:
            llm_west: Cliente LLM para perspectiva occidental
            llm_east: Cliente LLM para perspectiva oriental
            model_west: Modelo occidental (default: Gemini)
            model_east: Modelo oriental (default: DeepSeek)
        """
        self.llm_west = llm_west
        self.llm_east = llm_east
        self.model_west = model_west
        self.model_east = model_east
    
    def generate_western_prompt(self, scenario: str, keter_result: Dict, chochmah_result: Dict) -> str:
        """Genera prompt para análisis occidental"""
        return f"""
You are analyzing this scenario from a WESTERN philosophical perspective 
(individualism, rights, progress, democracy, capitalism).

SCENARIO:
{scenario}

KETER ALIGNMENT: {keter_result.get('alignment_percentage', 0)}%
CHOCHMAH CONFIDENCE: {chochmah_result.get('confidence_level', 0)}%

Provide contextual analysis focusing on:
- Individual rights and freedoms
- Democratic governance
- Market mechanisms
- Scientific progress
- Utilitarian ethics (greatest good for greatest number)

OUTPUT (JSON):
{{
  "context_factors": [
    {{
      "factor": "Factor name",
      "importance": "high/medium/low",
      "reasoning": "Why this matters from Western view..."
    }},
    ... (5-10 factors)
  ],
  
  "stakeholder_groups": [
    {{
      "group": "Stakeholder name",
      "interests": "What they want...",
      "power_level": "high/medium/low",
      "perspective": "How they view this..."
    }},
    ... (5-10 groups)
  ],
  
  "biases_western": [
    {{
      "bias_name": "Name of Western bias",
      "description": "How this bias manifests...",
      "impact": "Effect on analysis..."
    }},
    ... (identify 3-6 Western-specific biases)
  ],
  
  "risks_opportunities": "Western perspective on risks and opportunities...",
  
  "recommended_approach": "What Western philosophy suggests..."
}}
"""
    
    def generate_eastern_prompt(self, scenario: str, keter_result: Dict, chochmah_result: Dict) -> str:
        """Genera prompt para análisis oriental"""
        return f"""
You are analyzing this scenario from an EASTERN philosophical perspective
(collectivism, harmony, duty, hierarchy, virtue ethics, Confucianism/Buddhism/Taoism).

SCENARIO:
{scenario}

KETER ALIGNMENT: {keter_result.get('alignment_percentage', 0)}%
CHOCHMAH CONFIDENCE: {chochmah_result.get('confidence_level', 0)}%

Provide contextual analysis focusing on:
- Social harmony and collective well-being
- Duty and responsibility (filial piety, social obligation)
- Hierarchical relationships (ruler-subject, elder-youth)
- Virtue ethics and moral cultivation
- Long-term thinking (generations, cosmic time)

OUTPUT (JSON):
{{
  "context_factors": [
    {{
      "factor": "Factor name",
      "importance": "high/medium/low",
      "reasoning": "Why this matters from Eastern view..."
    }},
    ... (5-10 factors)
  ],
  
  "stakeholder_groups": [
    {{
      "group": "Stakeholder name",
      "interests": "What they want...",
      "power_level": "high/medium/low",
      "perspective": "How they view this..."
    }},
    ... (5-10 groups)
  ],
  
  "biases_eastern": [
    {{
      "bias_name": "Name of Eastern bias",
      "description": "How this bias manifests...",
      "impact": "Effect on analysis..."
    }},
    ... (identify 3-6 Eastern-specific biases)
  ],
  
  "risks_opportunities": "Eastern perspective on risks and opportunities...",
  
  "recommended_approach": "What Eastern philosophy suggests..."
}}
"""
    
    def generate_synthesis_prompt(self, west_analysis: Dict, east_analysis: Dict, scenario: str) -> str:
        """Genera prompt para síntesis meta-cognitiva"""
        return f"""
You are performing META-COGNITIVE SYNTHESIS of Western and Eastern analyses.

SCENARIO:
{scenario}

WESTERN ANALYSIS:
{json.dumps(west_analysis, indent=2)}

EASTERN ANALYSIS:
{json.dumps(east_analysis, indent=2)}

YOUR TASK:
Synthesize these perspectives into transcendent wisdom that neither perspective alone sees.

OUTPUT (JSON):
{{
  "synthesis_narrative": "Paragraph explaining how East and West complement each other...",
  
  "blind_spots_identified": [
    {{
      "perspective": "western/eastern",
      "blind_spot": "What this perspective misses...",
      "why_blind": "Cultural reason for blindness...",
      "correction": "How other perspective corrects this..."
    }},
    ... (identify 4-8 blind spots total)
  ],
  
  "convergence_points": [
    {{
      "point": "Area where East and West agree...",
      "significance": "Why this convergence matters..."
    }},
    ... (identify 2-5 convergence points)
  ],
  
  "divergence_points": [
    {{
      "point": "Area where East and West fundamentally disagree...",
      "western_view": "...",
      "eastern_view": "...",
      "synthesis_approach": "How to navigate this divergence..."
    }},
    ... (identify 3-6 divergence points)
  ],
  
  "transcendent_insights": [
    "Insight 1: What NEITHER perspective sees alone...",
    "Insight 2: Emergent wisdom from synthesis...",
    ... (2-4 insights)
  ],
  
  "recommended_approach": "Synthesized recommendation balancing both perspectives...",
  
  "synthesis_quality_self_assessment": 0-100
}}
"""
    
    def calculate_bias_delta(self, west_biases: List, east_biases: List) -> int:
        """
        Calcula diferencia absoluta en número de sesgos detectados
        """
        return abs(len(west_biases) - len(east_biases))
    
    def calculate_divergence_level(self, west_analysis: Dict, east_analysis: Dict, synthesis: Dict) -> str:
        """
        Clasifica nivel de divergencia entre perspectivas
        
        Returns:
            'low_divergence', 'moderate_divergence', o 'high_divergence'
        """
        divergence_points = synthesis.get('divergence_points', [])
        convergence_points = synthesis.get('convergence_points', [])
        
        if not divergence_points and not convergence_points:
            return 'unknown'
        
        divergence_count = len(divergence_points)
        convergence_count = len(convergence_points)
        
        # Calculate ratio
        total_points = divergence_count + convergence_count
        if total_points == 0:
            return 'unknown'
        
        divergence_ratio = divergence_count / total_points
        
        if divergence_ratio >= 0.7:
            return 'high_divergence'
        elif divergence_ratio >= 0.4:
            return 'moderate_divergence'
        else:
            return 'low_divergence'
    
    def calculate_contextual_depth(self, west_analysis: Dict, east_analysis: Dict, synthesis: Dict) -> float:
        """
        Calcula score de profundidad contextual (0-100)
        
        Basado en:
        - Número de factores contextuales identificados
        - Número de stakeholders analizados
        - Calidad de síntesis
        """
        # Count context factors
        west_factors = len(west_analysis.get('context_factors', []))
        east_factors = len(east_analysis.get('context_factors', []))
        
        # Count stakeholders
        west_stakeholders = len(west_analysis.get('stakeholder_groups', []))
        east_stakeholders = len(east_analysis.get('stakeholder_groups', []))
        
        # Synthesis quality
        synthesis_quality = synthesis.get('synthesis_quality_self_assessment', 0)
        
        # Calculate score
        factor_score = min((west_factors + east_factors) * 3, 40)  # Max 40 points
        stakeholder_score = min((west_stakeholders + east_stakeholders) * 2, 30)  # Max 30 points
        synthesis_score = synthesis_quality * 0.3  # Max 30 points
        
        total_score = factor_score + stakeholder_score + synthesis_score
        return round(min(total_score, 100), 1)
    
    def analyze(self, scenario: str, keter_result: Dict, chochmah_result: Dict) -> Dict[str, Any]:
        """
        Ejecuta análisis Binah Sigma completo con campos explícitos
        
        Args:
            scenario: Descripción del escenario
            keter_result: Resultado de Keter
            chochmah_result: Resultado de Chochmah
            
        Returns:
            Dict con análisis Binah Sigma perfeccionado
        """
        # 1. Análisis Occidental
        west_prompt = self.generate_western_prompt(scenario, keter_result, chochmah_result)
        west_response = self.llm_west.generate(
            prompt=west_prompt,
            model=self.model_west,
            temperature=0.7,
            max_tokens=2500
        )
        
        # Parse Western analysis
        west_analysis = self._parse_json_response(west_response, "Western")
        
        # 2. Análisis Oriental
        east_prompt = self.generate_eastern_prompt(scenario, keter_result, chochmah_result)
        east_response = self.llm_east.generate(
            prompt=east_prompt,
            model=self.model_east,
            temperature=0.7,
            max_tokens=2500
        )
        
        # Parse Eastern analysis
        east_analysis = self._parse_json_response(east_response, "Eastern")
        
        # 3. Síntesis Meta-Cognitiva
        synthesis_prompt = self.generate_synthesis_prompt(west_analysis, east_analysis, scenario)
        synthesis_response = self.llm_west.generate(  # Use Western LLM for synthesis
            prompt=synthesis_prompt,
            model=self.model_west,
            temperature=0.8,  # Slightly higher for creative synthesis
            max_tokens=3000
        )
        
        # Parse synthesis
        synthesis = self._parse_json_response(synthesis_response, "Synthesis")
        
        # 4. Calculate Metrics
        west_biases = west_analysis.get('biases_western', [])
        east_biases = east_analysis.get('biases_eastern', [])
        
        bias_delta = self.calculate_bias_delta(west_biases, east_biases)
        divergence_level = self.calculate_divergence_level(west_analysis, east_analysis, synthesis)
        contextual_depth_score = self.calculate_contextual_depth(west_analysis, east_analysis, synthesis)
        
        blind_spots = synthesis.get('blind_spots_identified', [])
        convergence_points = synthesis.get('convergence_points', [])
        
        # 5. Build Result with EXPLICIT FIELDS
        result = {
            # Metadata
            'sefira': 'binah',
            'sefira_number': 3,
            'hebrew_name': 'בינה',
            
            # EXPLICIT MODE
            'mode': 'sigma',  # ← CRITICAL: Explicit mode declaration
            
            # Analyses
            'western_analysis': west_analysis,
            'eastern_analysis': east_analysis,
            'meta_synthesis': synthesis,
            
            # EXPLICIT METRICS
            'bias_delta': bias_delta,  # ← CRITICAL: Delta between W and E bias counts
            'divergence_level': divergence_level,  # ← CRITICAL: Classification of divergence
            'blind_spots_detected': len(blind_spots),  # ← CRITICAL: Total blind spots
            'convergence_points': len(convergence_points),  # ← CRITICAL: Agreement points
            
            # Depth scores
            'contextual_depth_score': contextual_depth_score,
            'synthesis_quality': synthesis.get('synthesis_quality_self_assessment', 0),
            
            # Biases
            'biases_western_count': len(west_biases),
            'biases_eastern_count': len(east_biases),
            'biases_total': len(west_biases) + len(east_biases),
            
            # Models used
            'model_west': self.model_west,
            'model_east': self.model_east,
            
            # Quality assessment
            'understanding_quality': self._assess_quality(contextual_depth_score),
            
            # Timestamp
            'timestamp': datetime.now().isoformat(),
        }
        
        return result
    
    def _parse_json_response(self, response: str, analysis_name: str) -> Dict:
        """Parse JSON response with error handling"""
        try:
            clean_response = response.strip()
            if clean_response.startswith('```json'):
                clean_response = clean_response[7:]
            if clean_response.endswith('```'):
                clean_response = clean_response[:-3]
            clean_response = clean_response.strip()
            
            return json.loads(clean_response)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Failed to parse {analysis_name} JSON response: {e}\n"
                f"Response preview: {response[:500]}"
            )
    
    def _assess_quality(self, depth_score: float) -> str:
        """Assess overall quality based on depth score"""
        if depth_score >= 90:
            return 'exceptional'
        elif depth_score >= 75:
            return 'excellent'
        elif depth_score >= 60:
            return 'good'
        elif depth_score >= 45:
            return 'adequate'
        else:
            return 'needs_improvement'


# Ejemplo de uso
if __name__ == "__main__":
    print("Binah Sigma Perfecto - Campos Explícitos y Métricas Calculadas")
    print("=" * 70)
    print("\nCampos Explícitos Generados:")
    print("  ✓ mode: 'sigma'")
    print("  ✓ bias_delta: Diferencia absoluta en biases W vs E")
    print("  ✓ divergence_level: 'low/moderate/high_divergence'")
    print("  ✓ blind_spots_detected: Count total de blind spots")
    print("  ✓ convergence_points: Count de puntos de convergencia")
    print("\nEsto permite validación automática en tests.")
