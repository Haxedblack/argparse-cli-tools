# 🧮 CLI Calculator using argparse

This is a command-line calculator built using Python's `argparse` module. It demonstrates:

- Positional arguments for two numbers
- `--opp` optional argument with choices (`add`, `sub`, `mul`, `div`)
- `--verbose` flag to describe the operation
- `--round` option to round the result to N decimal places
- Graceful error handling (e.g., division by zero)

## 🧪 Example Usage

```bash
python calc.py 5 2 --opp mul --verbose
# Output:
# Multiplying 5.0 and 2.0
# Result: 10.0
