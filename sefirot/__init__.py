"""
Framework Tikun - 10 Sefirot Modules
Kabbalistic AI Ethics System

Complete 10-Sefirot Pipeline:
1. Keter (כתר) - Validation (ethics alignment)
2. Chochmah (חכמה) - Deep reasoning
3. Binah (בינה) - 9D context analysis
4. Chesed (חסד) - Opportunities & expansion
5. Gevurah (גבורה) - Risks & constraints
6. Tiferet (תפארת) - Synthesis & balance
7. Netzach (נצח) - Implementation strategy
8. Hod (הוד) - Communication & articulation
9. Yesod (יסוד) - Integration & readiness
10. Malchut (מלכות) - Action plan & manifestation

Architecture:
- Keter: Gemini 2.0 Flash (ethical validation, 100% accuracy validated)
- Chochmah-Malchut: Gemini 2.0 Flash (fast, coherent pipeline)
- Future: BinahSigma (Gemini + DeepSeek multi-civilizational analysis)
"""

# Import all fully implemented modules
from .keter import Keter, KeterValidator  # Export both names for compatibility
from .chochmah import Chochmah
from .binah import Binah
from .binah_sigma import BinahSigma  # Multi-civilizational analysis
from .chesed import Chesed
from .gevurah import Gevurah
from .tiferet import Tiferet
from .netzach import Netzach
from .hod import Hod
from .yesod import Yesod
from .malchut import Malchut

__all__ = [
    "Keter",
    "KeterValidator",  # Backward compatibility
    "Chochmah",
    "Binah",
    "BinahSigma",  # Multi-civilizational analysis (Occidente vs Oriente)
    "Chesed",
    "Gevurah",
    "Tiferet",
    "Netzach",
    "Hod",
    "Yesod",
    "Malchut",
]
