import time


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

    def create_postprocess_steps(
            
    ):
        return config.post_process if config is not None else None
    
    prg_rep = prg_rep or NullPrgRep()
    storage = create_storage()

    async for table in run_ppl(

    ):
        yield table

async def run_ppl(
        
)->AsyncIterable[PplRunResult]:
    
    start_time = time.time()
    