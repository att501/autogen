# CRM Sample

This folder contains a minimal skeleton showing how to run a layered AutoGen setup for a CRM system.

The example includes:

- `run_host.py` – starts the gRPC host that coordinates agents.
- `run_lead_scraper_agent.py`, `run_email_agent.py`, `run_order_agent.py` – lightweight worker agents (GPT‑3.5 level).
- `run_manager_agent.py` – a manager agent that can reason over events.
- `config.yaml` – configuration for host and agent topics.

The scripts are simplified placeholders illustrating how to compose a host process and multiple workers. They can be extended to scrape leads, send emails, and manage orders.

## Usage

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install "autogen-ext[openai,azure]" pyyaml rich
   ```
3. Run the host and agents in separate terminals:
   ```bash
   python run_host.py
   python run_lead_scraper_agent.py
   python run_email_agent.py
   python run_order_agent.py
   python run_manager_agent.py
   ```

Agents publish and subscribe to events based on the topic types defined in `config.yaml`.
