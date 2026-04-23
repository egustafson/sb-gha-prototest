# GitHub Actions Integration Guide

## For sb-gha-protolib Repository

You can invoke regression test workflows from the sb-gha-protolib repository to test your changes.

Available workflows:
- `.github/workflows/regression-test.yml`: Single Python version regression test
- `.github/workflows/regression-test-matrix.yml`: Matrix regression test from library minimum Python version through latest GA

### Option 1: Call as a Reusable Workflow

Add this to your sb-gha-protolib `.github/workflows/test.yml` (or similar):

```yaml
name: Test Suite

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  release:
    types: [published]

jobs:
  # ... your existing tests ...

  regression-test:
    name: Regression Tests
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
    with:
      revision: ${{ github.sha }}  # Use the current commit
```

### Option 2: Test Specific Tags

When you create a release/tag, you can test that specific version:

```yaml
jobs:
  regression-test:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
    with:
      revision: ${{ github.ref_name }}  # Test the tag being released
```

### Option 3: Manual Trigger

You can manually trigger the test workflow:

```bash
gh workflow run regression-test.yml \
  -R egustafson/sb-gha-prototest \
  -f revision=v0.2.0
```

### Option 4: Matrix Test Across Supported Python Versions

Use the matrix workflow to test from the library's `requires-python` minimum through a selected latest GA Python version.

```yaml
jobs:
  regression-test-matrix:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test-matrix.yml@main
    with:
      revision: ${{ github.sha }}
      latest-ga-python: "3.13"  # optional
```

## Workflow Behavior

- `regression-test.yml`
  - **Input**: `revision`, optional `python-version`
  - **Output**: Exit code 0 for success, 1 for failure
  - **Tests**: Validates `greeter()` function with 5 Latin-based names
  - **Duration**: Typically completes in under 1 minute

- `regression-test-matrix.yml`
  - **Input**: `revision`, optional `latest-ga-python`
  - **Behavior**: Reads `requires-python` from sb-gha-protolib at the target revision, builds version matrix, runs regression test on each version
  - **Output**: Matrix job succeeds only if all versions pass

## Integration Examples

### Test on Each Push
```yaml
on:
  push:
    branches: [main]

jobs:
  test-single:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
    with:
      revision: ${{ github.sha }}

  test-matrix:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test-matrix.yml@main
    with:
      revision: ${{ github.sha }}
      latest-ga-python: "3.13"
```

### Test on Release
```yaml
on:
  release:
    types: [published]

jobs:
  test:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
    with:
      revision: ${{ github.event.release.tag_name }}
```

### Test on Pull Request
```yaml
on:
  pull_request:

jobs:
  test:
    uses: egustafson/sb-gha-prototest/.github/workflows/regression-test.yml@main
    with:
      revision: ${{ github.head_ref }}  # Test the PR branch
```

## Troubleshooting

**Workflow not found**: Ensure the workflow file path is correct and uses the full path: `.github/workflows/regression-test.yml`

**Permission denied**: Make sure the sb-gha-prototest repository is public or you have appropriate access.

**Test failures**: Check the workflow logs in GitHub Actions to see which test case failed. Common issues:
- Incorrect revision specified
- Network issues pulling dependencies
- Changes to the `greeter()` function signature
