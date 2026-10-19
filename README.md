Problem Resolution Validation Harness
A modular, schema-driven testing and validation framework designed to evaluate how automated algorithms detect, isolate, and handle complex systemic anomalies, chronic performance drift, and deniable interference patterns.
Architecture Overview
Standard testing harnesses often focus on single-point stress testing or surface-level error rates. This harness evaluates root-cause resolution and systemic rationality by decoupling test scenarios from execution logic:
 * JSON Validation Schema: Enforces strict structuring of test suites, problem classifications, rationality parameters, and evaluation hooks.
 * Local LLM Integration (Ollama): Routes test prompts through local models to analyze trigger sequences against underlying problem rationales.
 * Dynamic Execution Engine: Uses Python's importlib to dynamically load external evaluation modules and execute custom assertion logic on runtime telemetry.
 ```
Repository Structure
├── schema/
│   └── validation_harness_schema.json    # JSON Schema definition for test scenarios
├── eval_modules/
│   └── telemetry_weight.py               # Modular evaluation logic and custom assertions
├── harness_runner.py                     # Main execution harness (Ollama routing + dynamic imports)
└── README.md
```
Installation & Prerequisites
 * Python 3.9+
 * Ollama running locally (default endpoint: http://localhost:11434)
 * Clone or download the repository structure.
 * Ensure Ollama is running and has your target model pulled:
   ollama run llama3
```
Usage Example
1. Define a Validation Payload (harness.json)
{
  "harness_metadata": {
    "version": "2.0.0",
    "target_max_size_bytes": 4096,
    "serialization_format": "compact_json"
  },
  "validation_suites": [
    {
      "suite_id": "suite_systemic_telemetry_01",
      "domain_focus": "network_synchronization_drift",
      "test_scenarios": [
        {
          "scenario_id": "sc_sensor_clock_drift",
          "problem_classification": "recurrence_pattern_anomaly",
          "underlying_problem_rationale": "Cumulative drift over rolling windows indicates a systemic clock synchronization error. Algorithm must suppress isolated false positives and flag drift trends.",
          "input_trigger_sequence": "Sensor node 4 reports timestamp delta of +45ms relative to atomic reference clock.",
          "rationality_parameters": {
            "ambiguity_coefficient": 0.30,
            "recurrence_interval_seconds": 3600,
            "cumulative_threshold": 4
          },
          "evaluation_hook": {
            "module_name": "eval_modules.telemetry_weight",
            "entry_point": "evaluate_drift_trend",
            "custom_assertion_logic": "assert result.systemic_anomaly_detected == true"
          },
          "expected_resolution": {
            "flag_systemic_anomaly": true,
            "max_allowed_latency_ms": 100
          }
        }
      ]
    }
  ]
}
```
2. Run the Harness Runner
Execute the Python script to parse the harness, route analysis through Ollama, and invoke the dynamic evaluation hooks:
from harness_runner import run_validation_harness
```
if __name__ == "__main__":
    run_validation_harness("harness.json")
```
Creating Custom Evaluation Modules
To add custom validation logic, create a Python file inside the eval_modules/ directory with a function matching your schema's entry_point:
```
# eval_modules/telemetry_weight.py

def evaluate_drift_trend(parameters):
    """
    Evaluates telemetry drift against cumulative thresholds.
    """
    threshold = parameters.get("cumulative_threshold", 3)
    # Custom evaluation logic here
    anomaly_detected = True if threshold >= 3 else False
    
    return {
        "systemic_anomaly_detected": anomaly_detected,
        "noise_filtered": True
    }
``
