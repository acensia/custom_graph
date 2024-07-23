from .progress import ProgressReporter
from .typing import PplRunResult

from .config import PplConfig

def run_ppl_with_config(
        config_or_path : PplConfig | str,
        prg_rep = ProgressReporter | None
)->AsyncIterable[PplRunResult]:
    
    if isinstance(config_or_path, str):
        log.info("")

    def create_storage():
        pass
    def create_cache():
        pass
    def create_reporter():
        pass
    def create_input():
        pass
    
    storage = create_storage()
    