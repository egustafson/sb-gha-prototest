# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-04-23

### Added
- Workflow step in `regression-test` job to print all workflow inputs and resolved runtime values

### Documentation
- Updated README feature list and execution flow to include workflow input reporting behavior

## [0.1.0] - 2026-04-23

### Added
- Initial release of sb-gha-prototest regression test suite
- GitHub Actions workflow (`regression-test.yml`) for testing sb-gha-protolib
- Reusable workflow support for integration with sb-gha-protolib repository
- Regression tests for `greeter()` function with 5 Latin-based names (Marcus, Julius, Lucius, Augustus, Aeneas)
- Parameterized Python version support in workflow (default: 3.14)
- Local testing script (`test-local.sh`) for development
- Comprehensive documentation:
  - README.md with overview and usage instructions
  - GITHUB_ACTIONS_INTEGRATION.md with integration examples
- Support for manual workflow dispatch and reusable workflow calls
- Pipeline caching for improved build performance
- Proper exit code handling (0 for success, 1 for failure)

### Features
- Tests verify that `greeter()` returns `"Hi <name>"` for alphanumeric names
- Validates function behavior across different Latin-based name inputs
- Clean, readable test output with pass/fail indicators

[0.1.0]: https://github.com/egustafson/sb-gha-prototest/releases/tag/v0.1.0
[0.1.1]: https://github.com/egustafson/sb-gha-prototest/releases/tag/v0.1.1
