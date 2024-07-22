from .progress import ProgressReporter
from .typing import PplRunResult

def run_ppl_with_config(
        prg_rep = ProgressReporter | None
)->AsyncIterable[PplRunResult]:
    def create_storage():
        pass
    def create_cache():
        pass
    def create_reporter():
        pass
    def create_input():
        pass
    
    storage = create_storage()
    