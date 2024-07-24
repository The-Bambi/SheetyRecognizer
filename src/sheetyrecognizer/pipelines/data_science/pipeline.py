from kedro.pipeline import Pipeline, node

from .nodes import split_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=split_data,
                inputs=["data_dict", "params:TRAIN_TO_OTHERS_RATIO", "params:VAL_TO_TEST_RATIO", "params:RANDOM_STATE"],
                outputs=["X_train", "X_test", "X_val", "y_train", "y_test", "y_val"],
                name="split_data_node",
            ),
        ]
    )
