"""Project pipelines."""
from __future__ import annotations

from kedro.pipeline import Pipeline

from sheetyrecognizer.pipelines import generate_data 

def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    generate_data_pipeline = generate_data.create_pipeline()

    pipelines = {
            "gd": generate_data_pipeline,
            "__default__": generate_data_pipeline,
            }

    return pipelines
