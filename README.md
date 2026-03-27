# Lightning-API

This repository contains a simple example of how to use the Lightning AI SDK to programmatically spin up cloud GPUs, run scripts, and manage resources.

## Files

- `lightning-api.py`: The main script that uses the `lightning_sdk` to:
  - Create or connect to a Lightning Studio.
  - Switch to a specific GPU machine (e.g., T4, L4, A100, H100).
  - Execute a Python script (`train.py`) on that machine.
  - Stop the machine afterward to save credits.
- `train.py`: A sample script that runs `nvidia-smi` to verify GPU availability on the connected instance.

## Prerequisites

You need to have the `lightning-sdk` installed and be authenticated with Lightning AI.

```bash
pip install lightning-sdk
```

## Usage

Run the main script to provision the GPU, run the job, and automatically spin it down:

```bash
python lightning-api.py
```