from kedro.pipeline import Pipeline, node

from .nodes import make_pitches, make_rythm, make_melody, make_data_file, make_lilypond_files, make_sheet_music


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=make_pitches,
                inputs=["params:NOTES", "params:amnt"],
                outputs="pitches",
                name="make_pitches_node",
            ),
            node(
                func=make_rythm,
                inputs=["params:RYTHMS", "params:amnt"],
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
                inputs=["melody", "params:MAX_NOTES_PER_PAGE"],
                outputs=["data_dict", "file_names"]
                name="make_data_file_node",
            ),
            node(
                func=make_lilypond_files,
                inputs=["data_dict", "params:LILYPOND_HEADER", "params:LILYPOND_END"],
                outputs="lilypond_files",
                name="make_sheet_music_node",
            ),
            node(
                func=make_sheet_music,
                inputs=["file_names"]
                outputs=None,
                name="convert_lilypond_to_png_node",
            ),
        ]
    )
