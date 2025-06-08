# 🤝 Contributing to Noesis³

Welcome, and thank you for considering contributing to **Noesis³**! This guide outlines how you can effectively contribute code, report issues, propose features, and improve documentation.

---

## 📦 Project Structure (Overview)

```
Noesis3/
├── origin/         # Rational cognition agent (math, writing)
├── riin/           # Creative cognition agent (lyrics, voice)
├── vanta/          # Strategic cognition agent (trading, risk)
├── core/           # Dispatcher, config loader, shared tools
├── config/         # YAML configs per agent
├── tasks/          # Structured task definitions
├── memory/         # Shared state abstraction
├── test_cases/     # Agent-specific test inputs and expected outputs
├── cli/            # Command line runners per agent
├── docs/           # Architecture, usage, coding guidelines
└── README.md
```

---

## 🧠 Contribution Guidelines

### 🔧 1. Setup Environment

* Python 3.10+
* Install dependencies:

```bash
pip install -r requirements.txt
```

### ✍️ 2. Code Guidelines

* Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* Use meaningful commit messages:

  * `feat(agent): add task_runner.py`
  * `fix(core): correct config path loading`
* Docstring format: Google Style
* Include inline comments for non-obvious logic

### 📁 3. File Expectations

Each new module or agent folder must include:

* `README.md` (brief overview of module purpose)
* at least one `task_runner.py` or core logic file
* sample config in `config/`
* optional test case in `test_cases/`

---

## 🧪 Testing

* Place all test examples in `test_cases/<agent>/<task_id>.json`
* Include both `input` and `expected_output` fields
* Run via CLI with debug flag: `python cli/origin_run.py --task <id> --debug`

---

## 🗣️ Pull Request Workflow

1. Fork the repo and create a new branch
2. Ensure your changes run and pass any related tests
3. Open a pull request with clear description
4. Wait for code review before merging

---

## ❓ Need Help?

If you're unsure how to begin, feel free to open an issue or reach out via GitHub discussions.

---

## 📄 License

By contributing, you agree that your work will be released under the MIT license.

---

Thanks again for being part of the Noesis³ ecosystem 💡
