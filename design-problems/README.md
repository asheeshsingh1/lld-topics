# Traffic Signal System

## Running the Application

This project uses absolute imports such as:

```python
from domain.direction import Direction
from service.intersection_service import IntersectionService
```

Because of this, the application must be run from the project root directory.

### Correct

```bash
python3.10 -m main.traffic_signal_simulator
```

### Incorrect

```bash
cd main
python3.10 traffic_signal_simulator.py
```

This will fail with:

```text
ModuleNotFoundError: No module named 'domain'
```

## Why?

When running a file directly, Python only adds the file's directory to `sys.path`.

Example:

```text
traffic-signal/
├── controller/
├── domain/
├── repository/
├── service/
└── main/
    └── traffic_signal_simulator.py
```

Running:

```bash
python3.10 -m main.traffic_signal_simulator
```

tells Python to treat the project root as the package root, making imports such as `domain.*`, `service.*`, and `repository.*` work correctly.

## Requirements

Each package directory should contain an `__init__.py` file:

```text
controller/__init__.py
domain/__init__.py
repository/__init__.py
service/__init__.py
main/__init__.py
```
