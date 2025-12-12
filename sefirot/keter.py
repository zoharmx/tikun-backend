"""
Keter (Crown) - Tikun Olam Validation Module

The highest Sefira that evaluates if an action/policy aligns with "repairing the world".
Evaluates 5 dimensions on -10 to +10 scale and detects corruptions.

Minimum alignment threshold: 60% (0.60)
"""

import os
import json
from typing import Dict, Any, List, Tuple
from datetime import datetime

# Import LLM client
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from sefirot.llm_client import get_llm_for_sefira

# Constants
KETER_ALIGNMENT_THRESHOLD = 0.60  # 60% threshold for alignment


class Keter:
    """
    Keter - Crown - Divine Purpose Alignment Validator

    Evaluates 5 core dimensions:
    1. reduces_suffering (-10 to +10)
    2. respects_free_will (-10 to +10)
    3. promotes_harmony (-10 to +10)
    4. justice_mercy_balance (-10 to +10)
    5. aligned_with_truth (-10 to +10)

    Alignment Score = (sum of all 5 scores + 50) / 100
    Must be >= 60% (0.60) to proceed
    """

    def __init__(self, api_key: str = None):
        """Initialize Keter with LLM client"""
        self.name = "keter"
        self.hebrew_name = "כתר"
        self.position = 1
        self.llm = get_llm_for_sefira(self.name)
        self.threshold = KETER_ALIGNMENT_THRESHOLD
        self.activation_count = 0

    def process(self, scenario: str, previous_results: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Process scenario through Keter - validates ethical alignment

        Args:
            scenario: Scenario to validate
            previous_results: Not used for Keter (it's the first Sefira)

        Returns:
            Dict with validation results
        """
        return self.validate(scenario)

    def validate(self, scenario: str, max_retries: int = 3) -> Dict[str, Any]:
        """
        Validate if scenario aligns with Tikun Olam

        Args:
            scenario: Description of the action/policy to evaluate
            max_retries: Maximum retry attempts for JSON parsing failures

        Returns:
            Dictionary with:
            - scores: Dict of 5 dimension scores (-10 to +10)
            - alignment_score: Float 0.0 to 1.0
            - corruptions: List of detected corruptions
            - corruption_severity: critical/moderate/minor/none
            - manifestation_valid: bool (True if >= 60% and no critical corruptions)
            - reasoning: Detailed explanation
            - timestamp: ISO timestamp
        """

        prompt = self._build_prompt(scenario)
        last_error = None

        # Retry loop for handling JSON parsing failures
        for attempt in range(max_retries):
            try:
                response = self.llm.generate(prompt, temperature=0.3)
                result = self.llm.parse_json_response(response)

                # Success - calculate alignment score
                if attempt > 0:
                    print(f"[SUCCESS] Keter JSON parsed successfully on attempt {attempt + 1}")

                scores = result['scores']

                # FIX: Normalize scores to int (handle string values from LLM)
                # Gemini sometimes returns "9" instead of 9
                normalized_scores = {}
                for key, value in scores.items():
                    try:
                        normalized_scores[key] = int(value)
                    except (ValueError, TypeError):
                        # If conversion fails, try to handle as is (might fail on sum)
                        normalized_scores[key] = value

                total_score = sum(normalized_scores.values())
                alignment_score = (total_score + 50) / 100.0

                # Determine corruption severity
                corruptions = result.get('corruptions', [])
                corruption_severity = self._assess_corruption_severity(corruptions)

                # Determine if manifestation is valid
                manifestation_valid = (
                    alignment_score >= self.threshold and
                    corruption_severity != 'critical'
                )

                self.activation_count += 1

                return {
                    'sefira': self.name,
                    'sefira_number': self.position,
                    'hebrew_name': self.hebrew_name,
                    'scores': normalized_scores,  # Use normalized scores (int instead of str)
                    'alignment_score': round(alignment_score, 4),
                    'alignment_percentage': round(alignment_score * 100, 2),
                    'corruptions': corruptions,
                    'corruption_severity': corruption_severity,
                    'manifestation_valid': manifestation_valid,
                    'threshold_met': alignment_score >= self.threshold,
                    'reasoning': result.get('reasoning', ''),
                    'timestamp': datetime.now().isoformat(),
                    'model_used': self.llm.model,
                    'activation_count': self.activation_count,
                    'attempts': attempt + 1
                }

            except Exception as e:
                last_error = e
                if attempt < max_retries - 1:
                    print(f"[WARNING] Keter attempt {attempt + 1} failed: {str(e)[:100]}...")
                    print(f"[INFO] Retrying ({attempt + 2}/{max_retries})...")
                else:
                    print(f"[ERROR] Keter failed after {max_retries} attempts")

        # All retries exhausted
        return {
            'sefira': 'keter',
            'error': f"Failed after {max_retries} attempts: {str(last_error)}",
            'manifestation_valid': False,
            'timestamp': datetime.now().isoformat(),
            'attempts': max_retries
        }

    def _build_prompt(self, scenario: str) -> str:
        """Build the prompt for Keter evaluation"""
        return f"""You are KETER - evaluate Tikun Olam (repairing the world) alignment.

SCENARIO:
{scenario}

SCORE 5 DIMENSIONS (-10 to +10):

1. reduces_suffering: Does it reduce or increase suffering?
   Scale: -10=maximum suffering (1M+ casualties), 0=neutral, +10=maximum reduction

2. respects_free_will: Does it respect human autonomy?
   Scale: -10=violates free will, 0=neutral, +10=respects autonomy

3. promotes_harmony: Does it promote peace and harmony?
   CRITICAL: Military action/war MUST score ≤+3, mass violence (>10K deaths) MUST be ≤0
   Scale: -10=war/genocide, 0=neutral, +10=transformative peace

4. justice_mercy_balance: Balances justice with compassion?
   Scale: -10=pure revenge, 0=neutral, +10=perfect balance

5. aligned_with_truth: Based on truth?
   Scale: -10=lies/deception, 0=unclear, +10=aligned with truth

CORRUPTION DETECTION:
Identify deviations from divine purpose (type, severity: critical/moderate/minor, description).

RESPONSE (JSON only, no markdown, no text before/after):
{{
    "scores": {{
        "reduces_suffering": <integer -10 to +10>,
        "respects_free_will": <integer -10 to +10>,
        "promotes_harmony": <integer -10 to +10>,
        "justice_mercy_balance": <integer -10 to +10>,
        "aligned_with_truth": <integer -10 to +10>
    }},
    "corruptions": [
        {{
            "type": "corruption name",
            "severity": "critical/moderate/minor",
            "description": "brief explanation (max 150 words)"
        }}
    ],
    "reasoning": "Explain your scores briefly (max 300 words)"
}}

CRITICAL: Return ONLY valid JSON. No markdown formatting, no code blocks, no asterisks, no underscores for emphasis. Use plain text in descriptions."""

    def _assess_corruption_severity(self, corruptions: List[Dict[str, Any]]) -> str:
        """Assess overall corruption severity"""
        if not corruptions:
            return 'none'

        severities = [c.get('severity', 'minor') for c in corruptions]

        if 'critical' in severities:
            return 'critical'
        elif 'moderate' in severities:
            return 'moderate'
        else:
            return 'minor'

    def export_result(self, result: Dict[str, Any], filepath: str = None) -> str:
        """Export result to JSON file"""
        if filepath is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filepath = f"keter_validation_{timestamp}.json"

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return filepath

    def get_metrics(self) -> Dict[str, Any]:
        """Get metrics for Keter"""
        return {
            "sefira": self.name,
            "position": self.position,
            "activations": self.activation_count,
            "threshold": self.threshold
        }


# Alias for backward compatibility
KeterValidator = Keter


# CLI interface for testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python keter.py '<scenario>'")
        print("Example: python keter.py 'Implement universal basic income'")
        sys.exit(1)

    scenario = sys.argv[1]

    print("=" * 60)
    print("KETER - Tikun Olam Validation")
    print("=" * 60)
    print(f"Scenario: {scenario}\n")

    validator = KeterValidator()
    result = validator.validate(scenario)

    if 'error' in result:
        print(f"ERROR: {result['error']}")
    else:
        print(f"Alignment Score: {result['alignment_percentage']}%")
        print(f"Threshold: {KETER_ALIGNMENT_THRESHOLD * 100}%")
        print(f"Threshold Met: {result['threshold_met']}")
        print(f"Manifestation Valid: {result['manifestation_valid']}")
        print(f"\nCorruption Severity: {result['corruption_severity']}")

        print("\nScores by Dimension:")
        for dimension, score in result['scores'].items():
            print(f"  {dimension}: {score:+d}")

        if result['corruptions']:
            print("\nCorruptions Detected:")
            for corruption in result['corruptions']:
                print(f"  - [{corruption['severity'].upper()}] {corruption['type']}")
                print(f"    {corruption['description']}")

        print(f"\nReasoning:\n{result['reasoning']}")

        # Export to file
        filepath = validator.export_result(result)
        print(f"\nResult exported to: {filepath}")
