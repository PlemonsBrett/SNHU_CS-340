"""Scripts for development tasks."""

import subprocess
import sys


def run_lint() -> int:
    """Run the linter with auto-fix enabled."""
    return subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--fix", "."]
    ).returncode


def run_format() -> int:
    """Run the formatter."""
    return subprocess.run([sys.executable, "-m", "ruff", "format", "."]).returncode


def run_typecheck() -> int:
    """Run the type checker."""
    return subprocess.run([sys.executable, "-m", "pyright"]).returncode

def run_dashboard(host: str = "0.0.0.0", port: int = 8050, debug: bool = False) -> int:
    """
    Run the Grazioso Salvare dashboard application.
    
    Args:
        host: Host address to bind server to (default: "0.0.0.0" - all interfaces)
        port: Port to run server on (default: 8050)
        debug: Whether to run in debug mode (default: False)
        
    Returns:
        Return code (0 for success)
    """
    try:
        from grazioso.dashboard import run_server
        run_server(host=host, port=port, debug=debug)
        return 0
    except ImportError:
        print("Error: Dashboard module not found or dependencies not installed.")
        print("Make sure to install the package with all required dependencies:")
        print("  poetry install")
        return 1
    except Exception as e:
        print(f"Error starting dashboard: {e}")
        return 1