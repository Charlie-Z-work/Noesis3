# 📐 Noesis Architecture Overview

## 🧠 Overview

Noesis³ is a modular multi-agent cognitive framework composed of three distinct agents—**Origin**, **Riin**, and **Vanta**—orchestrated by a central coordination system with shared memory and standardized task interfaces.

This document outlines the architectural principles, component roles, and communication flow among modules in the system.

---

## 🗂️ Core Components

### 1. Agents

Each agent is an autonomous cognitive unit with its own logic, configuration, and behavior:

* `origin/`: Handles scientific reasoning, mathematical modeling, and academic writing tasks.
* `riin/`: Responsible for creative tasks such as lyric generation, artistic expression, and voice synthesis.
* `vanta/`: Focuses on data modeling, quantitative analysis, and risk-based decision making.

Each agent exposes a unified entrypoint `run_task(config: dict)`.

### 2. `core/`

Provides coordination logic for routing tasks, inter-agent calls, and shared services:

* `agent_dispatcher.py`: Directs tasks to the right agent based on task type.
* `config_loader.py`: Loads YAML-based agent-specific configurations.

### 3. `memory/`

Stores shared memory across agents. Can be abstracted to Redis, SQLite, or JSON. Unified access via `MemoryClient` interface.

### 4. `config/`

Contains YAML configuration files for each agent:

* `origin.yaml`, `riin.yaml`, `vanta.yaml`

Includes model settings, pipeline steps, and runtime options.

### 5. `tasks/`

Defines structured task schemas that agents can execute. Each task includes:

* task\_id
* associated agent
* description and expected behavior
* path to test case file

---

## 🔁 Communication Flow

```
[ CLI / API ]
     ↓
 [ core/agent_dispatcher.py ]
     ↓
 [ agent_module.run_task() ]
     ↓
[ local core logic + model APIs ]
     ↓
[ optional: write to memory/, read config/, log result ]
```

---

## 🧰 Extensibility

* Add new agent: create new folder `agent_name/` with core + config + tasks
* Add new task: define YAML in `tasks/` and implement handler logic in agent
* Swap LLM backend: change model config in YAML and update dispatch logic
* External UI: connect via CLI or expose core as FastAPI endpoints

---

## 📌 Example Use Case

A user sends a `scientific_brainstorm` task via CLI:

* `agent_dispatcher.py` maps to `origin`
* `origin.run_task()` loads config and handles the task
* Intermediate results may be saved to `memory/`
* Final output saved to `logs/origin/YYYYMMDD.json`

---

## 📄 Status

This architecture is currently implemented in modular skeletons and is evolving toward full runtime capability.

---

## 👤 Maintained by

Charlie Z · [github.com/Charlie-Z-work](https://github.com/Charlie-Z-work)
