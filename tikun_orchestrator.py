"""
TikunOrchestrator - Orquestador del Pipeline Completo de 10 Sefirot
====================================================================

Ejecuta el flujo completo del framework Tikun Olam:
  Keter → Chochmah → Binah → Chesed → Gevurah → Tiferet →
  Netzach → Hod → Yesod → Malchut

Author: Framework Tikun
Date: 2025-12-07
Version: 2.0
"""

import os
import json
import sys
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import io

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from sefirot.keter import Keter
from sefirot.chochmah import Chochmah
from sefirot.binah import Binah
from sefirot.binah_sigma import BinahSigma  # Análisis multi-civilizacional
from sefirot.chesed import Chesed
from sefirot.gevurah import Gevurah
from sefirot.tiferet import Tiferet
from sefirot.netzach import Netzach
from sefirot.hod import Hod
from sefirot.yesod import Yesod
from sefirot.malchut import Malchut


class TikunOrchestrator:
    """
    Orquestador del pipeline completo de 10 Sefirot.

    Ejecuta el análisis ético completo desde validación inicial (Keter)
    hasta plan de acción concreto (Malchut).

    Features:
    - Ejecución secuencial con contexto acumulativo
    - Manejo de errores elegante
    - Exportación a JSON/TXT
    - Métricas del pipeline completo
    - Validación de coherencia entre Sefirot
    """

    def __init__(self, verbose: bool = True):
        """
        Inicializa el orquestador con todas las Sefirot.

        Args:
            verbose: Si True, imprime progreso detallado
        """
        self.verbose = verbose
        self.execution_count = 0

        # Inicializar las 10 Sefirot
        if self.verbose:
            print("=" * 80)
            print("INICIALIZANDO TIKUN ORCHESTRATOR")
            print("=" * 80)

        self.sefirot = self._initialize_sefirot()

        if self.verbose:
            print(f"\n✓ {len(self.sefirot)} Sefirot inicializadas correctamente")
            print("=" * 80 + "\n")

    def _initialize_sefirot(self) -> Dict[str, Any]:
        """Inicializa todas las Sefirot del pipeline"""
        sefirot = {}

        try:
            if self.verbose:
                print("[1/10] Inicializando KETER (Corona - Validación)...")
            sefirot['keter'] = Keter()

            if self.verbose:
                print("[2/10] Inicializando CHOCHMAH (Sabiduría - Razonamiento)...")
            sefirot['chochmah'] = Chochmah()

            if self.verbose:
                print("[3/10] Inicializando BINAH SIGMA (Análisis Multi-Civilizacional)...")
            sefirot['binah'] = BinahSigma()  # Usa BinahSigma para análisis robusto

            if self.verbose:
                print("[4/10] Inicializando CHESED (Misericordia - Oportunidades)...")
            sefirot['chesed'] = Chesed()

            if self.verbose:
                print("[5/10] Inicializando GEVURAH (Severidad - Riesgos)...")
            sefirot['gevurah'] = Gevurah()

            if self.verbose:
                print("[6/10] Inicializando TIFERET (Belleza - Síntesis)...")
            sefirot['tiferet'] = Tiferet()

            if self.verbose:
                print("[7/10] Inicializando NETZACH (Victoria - Estrategia)...")
            sefirot['netzach'] = Netzach()

            if self.verbose:
                print("[8/10] Inicializando HOD (Esplendor - Comunicación)...")
            sefirot['hod'] = Hod()

            if self.verbose:
                print("[9/10] Inicializando YESOD (Fundamento - Integración)...")
            sefirot['yesod'] = Yesod()

            if self.verbose:
                print("[10/10] Inicializando MALCHUT (Reino - Manifestación)...")
            sefirot['malchut'] = Malchut()

            return sefirot

        except Exception as e:
            print(f"\n✗ ERROR inicializando Sefirot: {e}")
            raise

    def process(self, scenario: str, case_name: Optional[str] = None) -> Dict[str, Any]:
        """
        Ejecuta el pipeline completo de las 10 Sefirot.

        Args:
            scenario: Descripción del escenario a analizar
            case_name: Nombre del caso (opcional, para logging)

        Returns:
            Dict con resultados de todas las Sefirot y métricas del pipeline
        """
        self.execution_count += 1
        start_time = datetime.now()

        if self.verbose:
            print("\n" + "=" * 80)
            print(f"EJECUTANDO PIPELINE TIKUN - {case_name or 'Caso ' + str(self.execution_count)}")
            print("=" * 80)
            print(f"Timestamp: {start_time.isoformat()}")
            print(f"Escenario: {scenario[:200]}{'...' if len(scenario) > 200 else ''}")
            print("=" * 80 + "\n")

        results = {
            'metadata': {
                'case_name': case_name,
                'execution_id': self.execution_count,
                'timestamp': start_time.isoformat(),
                'scenario': scenario
            },
            'sefirot_results': {},
            'pipeline_metrics': {},
            'errors': []
        }

        # Acumulador de contexto para pasar entre Sefirot
        context = {}

        # FASE 1: TRIADA SUPERIOR (Validación e Intelecto)
        if self.verbose:
            print("═" * 80)
            print("FASE 1: TRIADA SUPERIOR (Atzilut - Emanación)")
            print("═" * 80 + "\n")

        # 1. KETER - Validación
        keter_result = self._execute_sefira('keter', scenario, context)
        results['sefirot_results']['keter'] = keter_result
        context['keter'] = keter_result

        # 2. CHOCHMAH - Razonamiento Profundo
        chochmah_result = self._execute_sefira('chochmah', scenario, context)
        results['sefirot_results']['chochmah'] = chochmah_result
        context['chochmah'] = chochmah_result

        # 3. BINAH - Contexto 9D
        binah_result = self._execute_sefira('binah', scenario, context)
        results['sefirot_results']['binah'] = binah_result
        context['binah'] = binah_result

        # FASE 2: TRIADA MEDIA (Dialéctica Moral)
        if self.verbose:
            print("\n" + "═" * 80)
            print("FASE 2: TRIADA MEDIA (Beriah - Creación)")
            print("═" * 80 + "\n")

        # 4. CHESED - Oportunidades
        chesed_result = self._execute_sefira('chesed', scenario, context)
        results['sefirot_results']['chesed'] = chesed_result
        context['chesed'] = chesed_result

        # 5. GEVURAH - Riesgos
        gevurah_result = self._execute_sefira('gevurah', scenario, context)
        results['sefirot_results']['gevurah'] = gevurah_result
        context['gevurah'] = gevurah_result

        # 6. TIFERET - Síntesis
        tiferet_result = self._execute_sefira('tiferet', scenario, context)
        results['sefirot_results']['tiferet'] = tiferet_result
        context['tiferet'] = tiferet_result

        # FASE 3: TRIADA INFERIOR (Estrategia y Manifestación)
        if self.verbose:
            print("\n" + "═" * 80)
            print("FASE 3: TRIADA INFERIOR (Yetzirah + Assiah - Formación + Acción)")
            print("═" * 80 + "\n")

        # 7. NETZACH - Estrategia
        netzach_result = self._execute_sefira('netzach', scenario, context)
        results['sefirot_results']['netzach'] = netzach_result
        context['netzach'] = netzach_result

        # 8. HOD - Comunicación
        hod_result = self._execute_sefira('hod', scenario, context)
        results['sefirot_results']['hod'] = hod_result
        context['hod'] = hod_result

        # 9. YESOD - Integración
        yesod_result = self._execute_sefira('yesod', scenario, context)
        results['sefirot_results']['yesod'] = yesod_result
        context['yesod'] = yesod_result

        # 10. MALCHUT - Manifestación
        malchut_result = self._execute_sefira('malchut', scenario, context)
        results['sefirot_results']['malchut'] = malchut_result
        context['malchut'] = malchut_result

        # Calcular métricas del pipeline
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        results['pipeline_metrics'] = self._calculate_pipeline_metrics(
            results['sefirot_results'],
            duration
        )

        if self.verbose:
            print("\n" + "=" * 80)
            print("PIPELINE COMPLETADO")
            print("=" * 80)
            print(f"Duración total: {duration:.2f}s")
            print(f"Sefirot ejecutadas: {len([r for r in results['sefirot_results'].values() if 'error' not in r])}/10")
            print(f"Errores: {len(results['errors'])}")
            print("=" * 80 + "\n")

        return results

    def _execute_sefira(
        self,
        sefira_name: str,
        scenario: str,
        context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Ejecuta una Sefirá individual con manejo de errores.

        Args:
            sefira_name: Nombre de la Sefirá
            scenario: Escenario a analizar
            context: Contexto de Sefirot anteriores

        Returns:
            Resultado de la Sefirá o dict con error
        """
        if self.verbose:
            print(f"▶ Ejecutando {sefira_name.upper()}...")

        try:
            sefira = self.sefirot[sefira_name]
            start = datetime.now()

            # Ejecutar Sefirá
            result = sefira.process(scenario, context)

            duration = (datetime.now() - start).total_seconds()

            if self.verbose:
                status = "✓" if "error" not in result else "✗"
                print(f"  {status} Completada en {duration:.2f}s")

                # Imprimir métricas clave
                if "error" not in result:
                    self._print_sefira_summary(sefira_name, result)

            return result

        except Exception as e:
            error_msg = f"Error en {sefira_name}: {str(e)}"
            if self.verbose:
                print(f"  ✗ {error_msg}")

            return {
                'sefira': sefira_name,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }

    def _print_sefira_summary(self, sefira_name: str, result: Dict[str, Any]):
        """Imprime resumen de métricas clave de cada Sefirá"""
        if sefira_name == 'keter':
            print(f"    Alignment: {result.get('alignment_score', 'N/A')}%")
        elif sefira_name == 'chochmah':
            print(f"    Quality: {result.get('reasoning_quality', 'N/A')}")
        elif sefira_name == 'binah':
            print(f"    Depth: {result.get('contextual_depth_score', 'N/A')}%")
        elif sefira_name == 'chesed':
            print(f"    Expansion: {result.get('expansion_score', 'N/A')}%")
        elif sefira_name == 'gevurah':
            print(f"    Severity: {result.get('severity_score', 'N/A')}%")
        elif sefira_name == 'tiferet':
            print(f"    Harmony: {result.get('harmony_score', 'N/A')}%")
        elif sefira_name == 'netzach':
            print(f"    Persistence: {result.get('persistence_score', 'N/A')}%")
        elif sefira_name == 'hod':
            print(f"    Splendor: {result.get('splendor_score', 'N/A')}%")
        elif sefira_name == 'yesod':
            print(f"    Integration: {result.get('integration_score', 'N/A')}%")
        elif sefira_name == 'malchut':
            print(f"    Manifestation: {result.get('manifestation_score', 'N/A')}%")
        print()

    def _calculate_pipeline_metrics(
        self,
        sefirot_results: Dict[str, Any],
        duration: float
    ) -> Dict[str, Any]:
        """Calcula métricas agregadas del pipeline completo"""

        # Contar éxitos y fallos
        total_sefirot = len(sefirot_results)
        successful = len([r for r in sefirot_results.values() if 'error' not in r])
        failed = total_sefirot - successful

        # Extraer scores clave
        scores = {}
        if 'keter' in sefirot_results and 'error' not in sefirot_results['keter']:
            scores['keter_alignment'] = sefirot_results['keter'].get('alignment_score', 0)

        if 'binah' in sefirot_results and 'error' not in sefirot_results['binah']:
            scores['binah_depth'] = sefirot_results['binah'].get('contextual_depth_score', 0)

        if 'tiferet' in sefirot_results and 'error' not in sefirot_results['tiferet']:
            scores['tiferet_harmony'] = sefirot_results['tiferet'].get('harmony_score', 0)

        if 'yesod' in sefirot_results and 'error' not in sefirot_results['yesod']:
            scores['yesod_integration'] = sefirot_results['yesod'].get('integration_score', 0)

        # Calcular score promedio
        avg_score = sum(scores.values()) / len(scores) if scores else 0

        return {
            'total_sefirot': total_sefirot,
            'successful_sefirot': successful,
            'failed_sefirot': failed,
            'success_rate': round((successful / total_sefirot) * 100, 2),
            'total_duration_seconds': round(duration, 2),
            'avg_duration_per_sefira': round(duration / total_sefirot, 2),
            'key_scores': scores,
            'average_score': round(avg_score, 2),
            'pipeline_quality': self._assess_pipeline_quality(successful, avg_score)
        }

    def _assess_pipeline_quality(self, successful: int, avg_score: float) -> str:
        """Evalúa la calidad general del pipeline"""
        if successful < 10:
            return "incomplete"
        elif avg_score >= 85:
            return "exceptional"
        elif avg_score >= 70:
            return "high"
        elif avg_score >= 55:
            return "moderate"
        else:
            return "low"

    def export_results(
        self,
        results: Dict[str, Any],
        output_dir: str = ".",
        format: str = "json"
    ) -> str:
        """
        Exporta resultados a archivo.

        Args:
            results: Resultados del pipeline
            output_dir: Directorio de salida
            format: Formato de exportación ('json' o 'txt')

        Returns:
            Path del archivo generado
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        case_name = results['metadata'].get('case_name', 'tikun_analysis')
        safe_name = "".join(c for c in case_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_name = safe_name.replace(' ', '_')

        if format == "json":
            filename = f"{safe_name}_{timestamp}.json"
            filepath = Path(output_dir) / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

        elif format == "txt":
            filename = f"{safe_name}_{timestamp}.txt"
            filepath = Path(output_dir) / filename

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self._format_txt_report(results))

        else:
            raise ValueError(f"Formato no soportado: {format}")

        if self.verbose:
            print(f"\n✓ Resultados exportados: {filepath}")

        return str(filepath)

    def _format_txt_report(self, results: Dict[str, Any]) -> str:
        """Formatea resultados como reporte de texto"""
        lines = []
        lines.append("=" * 80)
        lines.append("REPORTE TIKUN OLAM - ANÁLISIS ÉTICO COMPLETO")
        lines.append("=" * 80)
        lines.append(f"\nCaso: {results['metadata'].get('case_name', 'N/A')}")
        lines.append(f"Timestamp: {results['metadata']['timestamp']}")
        lines.append(f"Execution ID: {results['metadata']['execution_id']}")
        lines.append("\n" + "=" * 80)
        lines.append("ESCENARIO ANALIZADO")
        lines.append("=" * 80)
        lines.append(results['metadata']['scenario'])

        lines.append("\n\n" + "=" * 80)
        lines.append("RESULTADOS POR SEFIRÁ")
        lines.append("=" * 80)

        for sefira_name, sefira_result in results['sefirot_results'].items():
            lines.append(f"\n{sefira_name.upper()}:")
            lines.append("-" * 40)

            if 'error' in sefira_result:
                lines.append(f"ERROR: {sefira_result['error']}")
            else:
                # Mostrar métricas clave
                for key, value in sefira_result.items():
                    if key not in ['timestamp', 'model_used', 'activation_count', 'sefira', 'sefira_number', 'hebrew_name']:
                        if isinstance(value, (int, float, str, bool)):
                            lines.append(f"  {key}: {value}")

        lines.append("\n\n" + "=" * 80)
        lines.append("MÉTRICAS DEL PIPELINE")
        lines.append("=" * 80)

        metrics = results['pipeline_metrics']
        lines.append(f"Sefirot exitosas: {metrics['successful_sefirot']}/{metrics['total_sefirot']}")
        lines.append(f"Tasa de éxito: {metrics['success_rate']}%")
        lines.append(f"Duración total: {metrics['total_duration_seconds']}s")
        lines.append(f"Duración promedio: {metrics['avg_duration_per_sefira']}s/sefirá")
        lines.append(f"Score promedio: {metrics['average_score']}")
        lines.append(f"Calidad del pipeline: {metrics['pipeline_quality']}")

        lines.append("\n" + "=" * 80)

        return "\n".join(lines)

    def get_metrics(self) -> Dict[str, Any]:
        """Obtiene métricas del orquestador"""
        return {
            'total_executions': self.execution_count,
            'sefirot_count': len(self.sefirot),
            'sefirot_names': list(self.sefirot.keys())
        }


# CLI Interface
if __name__ == "__main__":
    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    if len(sys.argv) < 2:
        print("=" * 80)
        print("TIKUN ORCHESTRATOR - Pipeline Completo de 10 Sefirot")
        print("=" * 80)
        print(f"\nUso: python {os.path.basename(__file__)} '<scenario>' [case_name]")
        print("\nEjemplo:")
        print(f"  python {os.path.basename(__file__)} 'Should we implement UBI?' 'UBI_Analysis'")
        print("\nEl pipeline ejecutará las 10 Sefirot en secuencia:")
        print("  1. Keter    - Validación ética")
        print("  2. Chochmah - Razonamiento profundo")
        print("  3. Binah    - Análisis contextual 9D")
        print("  4. Chesed   - Oportunidades y expansión")
        print("  5. Gevurah  - Riesgos y restricciones")
        print("  6. Tiferet  - Síntesis y balance")
        print("  7. Netzach  - Estrategia de implementación")
        print("  8. Hod      - Comunicación y articulación")
        print("  9. Yesod    - Integración y verificación")
        print("  10. Malchut - Plan de acción concreto")
        print("\nResultados se exportarán en JSON y TXT")
        print("=" * 80)
        sys.exit(1)

    scenario = sys.argv[1]
    case_name = sys.argv[2] if len(sys.argv) > 2 else None

    # Crear orchestrator
    orchestrator = TikunOrchestrator(verbose=True)

    # Ejecutar pipeline
    results = orchestrator.process(scenario, case_name)

    # Exportar resultados
    json_file = orchestrator.export_results(results, format="json")
    txt_file = orchestrator.export_results(results, format="txt")

    print("\n" + "=" * 80)
    print("ARCHIVOS GENERADOS:")
    print("=" * 80)
    print(f"JSON: {json_file}")
    print(f"TXT:  {txt_file}")
    print("=" * 80)
