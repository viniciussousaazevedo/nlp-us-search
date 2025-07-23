from dataclasses import dataclass
from typing import List

@dataclass
class FileMatch:
    filename: str
    score: float
    matched_chunks: List[str]

class Scores:
    def __init__(self):
        self.files: List[FileMatch] = []
        self.threshold = 0

    def add_file(self, file_similarity: FileMatch):
        self.files.append(file_similarity)

    def sort(self):
        self.files.sort(key=lambda x: -x.score)

    def get_above(self) -> List[FileMatch]:
        return [f for f in self.files if f.score >= self.threshold]