"""
Streamlit Cloud entry point.
Configured for app.py; delegates to main.py.
"""
import runpy

runpy.run_path("main.py", run_name="__main__")
