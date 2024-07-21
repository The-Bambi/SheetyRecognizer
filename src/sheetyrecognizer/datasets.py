from kedro.io import AbstractDataset
import os

class DictToLilypondFiles(AbstractDataset):
    def __init__(self, filepath):
        self._filepath = filepath

    def _load(self):
        raise NotImplementedError("Loading is not supported for DictToLilypondFiles")

    def _save(self, data):
        for filename, content in data.items():
            file_path = f"{self._filepath}/{filename}.ly"
            with open(file_path, 'w') as file:
                file.write(content)

    def _describe(self):
        return f"Save dictionary of melodies to multiple files with base filepath: {self._filepath}"
