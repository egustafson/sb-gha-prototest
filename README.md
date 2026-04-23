# SB-GHA-PROTOTEST

Regression test suite for the `greet` module in [sb-gha-protolib](https://github.com/egustafson/sb-gha-protolib).

## Overview

This repository provides a GitHub Actions workflow that performs regression testing on the `greeter()` function from the sb-gha-protolib repository. The workflow can be invoked from the protolib repository with a specific git tag or commit hash to test that revision.

## Features

- **GitHub Action Workflow**: Reusable workflow that accepts a revision input (tag or commit hash)
- **Parameterized Python Version**: Test against different Python versions (default: 3.14)
- **Input Reporting**: Prints all workflow inputs and resolved runtime values in job logs
- **Regression Tests**: Tests the `greeter()` function with 5 Latin-based names:
  - Marcus
  - Julius
  - Lucius
  - Augustus
  - Aeneas
- **Exit Code**: Returns success (0) if all tests pass, failure (1) if any test fails
- **Pipeline Caching**: Optimizes build times with pip package caching
- **Local Testing**: Includes local test script for development

## Quick Start

### Local Testing

Run the regression tests locally:

```bash
./test-local.sh
```

Or with explicit PYTHONPATH:

```bash
PYTHONPATH=../sb-gha-protolib:$PYTHONPATH python main.py
```

### GitHub Actions - Manual Trigger

Run the workflow manually from the Actions tab or via CLI:

```bash
gh workflow run regression-test.yml \
  -f revision=v0.2.0 \
  -f python-version=3.14
```

### GitHub Actions - Reusable Workflow

Call from sb-gha-protolib repository in your workflow:

```yaml
regression-test:
  uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
  with:
    revision: ${{ github.ref_name }}
    python-version: "3.14"  # optional
```

## Workflow Inputs

| Input | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `revision` | string | Yes | — | Git tag or commit hash of sb-gha-protolib to test |
| `python-version` | string | No | `3.14` | Python version to run tests with |

## How It Works

1. Checks out the test repository
2. Sets up the specified Python version
3. Reports workflow inputs and concrete values used for the run
4. Installs sb-gha-protolib from the specified revision
5. Runs regression tests validating `greeter()` function behavior
6. Reports test results with appropriate exit code

## Testing the Greet Module

The `greeter()` function from sb-gha-protolib:
- Returns `"Hi <name>"` for alphanumeric names
- Returns `"Not sure who you are."` for non-alphanumeric input

The regression tests verify this behavior with Latin-based names that are all alphanumeric, ensuring core functionality works as expected.

## Integration Examples

See [GITHUB_ACTIONS_INTEGRATION.md](GITHUB_ACTIONS_INTEGRATION.md) for detailed integration examples.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history and notable changes.

## Requirements

- Python 3.14 (or specified version)
- sb-gha-protolib repository accessible via GitHub

## License

See [LICENSE](LICENSE) file for details.
