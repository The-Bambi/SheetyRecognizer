import random
import pandas as pd

from typing import Tuple, List, Dict


def make_pitches(scale:List, amnt:int) -> List[str]:
    """
    Make a jumble of [amnt] random notes.
    """
    #TODO add moving weights.
    notes = random.choices(population=scale, k=amnt)
    return notes

def make_rythm(rythm_groups:List[Tuple], amnt:int) -> List[Tuple]:
    """
    Create a list of rythms. For now groups of rythms won't go beyond a quarter note.
    """
    rythms_notflat = random.choices(rythm_groups, weights=[10, 2, 2, 2, 2, ], k=amnt+1) 
    flattened = [i for j in rythms_notflat for i in j]
    return flattened

def make_melody(pitches:List, rythms:List[Tuple]) -> List[str]:
    zipped = list(zip(pitches, rythms)) # I use the fact zip cuts the longer lists to the shortest list
    melody = [f"{i}{j}" for i,j in zipped]
    return melody

def make_data_file(melody, max_notes_per_page) -> Dict[int, str]:
    """
    Returns a dictionary like:
    {
        1 : [music],
        2 : [music],
        ...
        n : [music],
    }
    Kedro saves the dict as a json or sth similar.
    """
    data_dict = {}
    for i, note in enumerate(melody):
        if i//max_notes_per_page not in data_dict:
            data_dict[i//max_notes_per_page] = []
        data_dict[i//max_notes_per_page].append(note)
    return data_dict

def make_lilypond_files(data_dict, lilypond_header, lilypond_end):
    """
    Based on the data dict, make strings that can be compiled by lilypond into sheet music.
    """
    final_dict = {}
    for i, music in data_dict.items():
        final_dict[i] = f"{lilypond_header} {' '.join(music)} {lilypond_end}"
    return final_dict


