from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_pitches, make_rythm, make_data_file, make_music_files


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=make_pitches,
                outputs="pitches",
                name="make_pitches_node",
            ),
            node(
                func=make_rythm,
                outputs="rythms",
                name="make_rythms_node",
            ),
            node(
                func=make_melody,
                inputs=["pitches", "rythms"],
                outputs="melody",
                name="make_melody_node",
            ),
            node(
                func=make_data_file,
                inputs="melody",
                outputs="data_file",
                name="make_data_file_node",
            ),
            node(
                func=make_music_files,
                inputs="melody",
                outputs=None,
                name="make_sheet_music_node",
            ),
        ]
    )
