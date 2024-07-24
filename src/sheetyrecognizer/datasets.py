from kedro.io import AbstractDataset
import os
import glob


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


class LilypondFilesLoader(AbstractDataset):
    def __init__(self, filepath):
        self._filepath = filepath

    def _load(self):
        return glob.glob(self.filepath)

    def _save(self):
        raise NotImplementedError("Saving is not supported for LilypondFilesLoader")

    def _describe(self):
        return f"Loads a list of files from given directory."
