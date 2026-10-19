import importlib
import json
import sys
import urllib.request
import urllib.error

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3" # Replace with your local model tag if needed

def query_ollama(prompt_text, system_context=""):
    """Routes prompt and context through Ollama API."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "system": system_context,
        "stream": False
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_API_URL, 
        data=data, 
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("response", "")
    except urllib.error.URLError as e:
        print(f"[Error] Failed to connect to Ollama: {e.reason}", file=sys.stderr)
        return None

def dynamic_execute_hook(module_name, entry_point, telemetry_data):
    """Dynamically loads an external evaluation script and executes its entry point."""
    try:
        mod = importlib.import_module(module_name)
        func = getattr(mod, entry_point)
        return func(telemetry_data)
    except ModuleNotFoundError:
        print(f"[Warning] Evaluation module '{module_name}' not found. Simulating fallback execution.", file=sys.stderr)
        # Fallback simulation for demonstration
        return {"systemic_anomaly_detected": True, "noise_filtered": True}
    except AttributeError:
        print(f"[Error] Entry point '{entry_point}' not found in module '{module_name}'.", file=sys.stderr)
        return None

def run_validation_harness(harness_json_path):
    """Parses the validation harness schema, tests via Ollama, and executes evaluation hooks."""
    with open(harness_json_path, "r", encoding="utf-8") as f:
        harness = json.load(f)

    print(f"Loaded Harness Version: {harness['harness_metadata']['version']}")
    
    for suite in harness.get("validation_suites", []):
        print(f"\n--- Running Suite: {suite['suite_id']} ({suite['domain_focus']}) ---")
        
        for scenario in suite.get("test_scenarios", []):
            scenario_id = scenario["scenario_id"]
            rationale = scenario["underlying_problem_rationale"]
            trigger = scenario["input_trigger_sequence"]
            eval_hook = scenario["evaluation_hook"]
            
            print(f"\n[Scenario: {scenario_id}]")
            print(f"Rationale: {rationale}")
            
            # Step 1: Route analysis through Ollama
            system_prompt = (
                "You are an automated telemetry and systemic anomaly evaluation engine. "
                "Analyze the provided input trigger against the underlying problem rationale."
            )
            user_prompt = f"Trigger Event: {trigger}\nEvaluate whether this indicates a systemic anomaly."
            
            print("-> Routing analysis through Ollama...")
            llm_analysis = query_ollama(user_prompt, system_context=system_prompt)
            if llm_analysis:
                print(f"LLM Output Preview: {llm_analysis[:200]}...")
            
            # Step 2: Execute external script evaluation hook
            print(f"-> Executing external module '{eval_hook['module_name']}.{eval_hook['entry_point']}'...")
            eval_result = dynamic_execute_hook(
                eval_hook["module_name"], 
                eval_hook["entry_point"], 
                scenario["rationality_parameters"]
            )
            
            print(f"Result of External Hook: {eval_result}")

if __name__ == "__main__":
    # Example usage (assumes harness JSON is saved locally as harness.json)
    # run_validation_harness("harness.json")
    pass
