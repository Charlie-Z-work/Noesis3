import argparse
import yaml
import os
import sys

# Assuming origin module is in PYTHONPATH or relative path
from origin.task_runner import run_task

def load_task_config(task_id):
    task_path = os.path.join("tasks", f"{task_id}.yaml")
    if not os.path.exists(task_path):
        raise FileNotFoundError(f"Task file not found: {task_path}")
    with open(task_path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Run Origin agent tasks via CLI")
    parser.add_argument("--task", type=str, required=True, help="Task ID to run (without extension)")
    parser.add_argument("--config", type=str, help="Optional path to override agent config")
    parser.add_argument("--debug", action="store_true", help="Run in debug mode")
    parser.add_argument("--save-log", action="store_true", help="Save output to logs/")

    args = parser.parse_args()
    
    try:
        task_config = load_task_config(args.task)
        if args.debug:
            print("[DEBUG] Loaded task config:", task_config)

        result = run_task(task_config)

        print("\n[RESULT]\n", result)

        if args.save_log:
            from datetime import datetime
            import json
            log_dir = os.path.join("logs", "origin")
            os.makedirs(log_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_path = os.path.join(log_dir, f"{args.task}_{timestamp}.json")
            with open(log_path, 'w') as f:
                json.dump({"input": task_config, "output": result}, f, indent=2)
            print(f"[LOG SAVED] {log_path}")

    except Exception as e:
        print("[ERROR]", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
