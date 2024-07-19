import time
import sys
from pathlib import Path


from . import PplConfig ## relative import
from .init_content import INIT_YAML, INIT_DOTENV ## relative import
from .graph.extractors.graph.prompts import GRAPH_EXTRACTION_PROMPT
from .graph.extractors.community.prompts import COMMUNITY_REPORT_PROMPT
from .progress import ProgressReporter ## relative import
from .run import _run_pipeline ## relative import

def index_cli(
        init:bool,
        root:str,
        resume : str | None,
        verbose:bool,
        overlay_defaults:bool
    ):
    run_id = resume or time.strftime("%Y%m%d-%H%M%S")
    _enable_logging(root, run_id, verbose)
    prg_rep = _get_prg_rep()

    if init:
        _init_project(root, prg_rep)
        sys.exit(0)
    
    if overlay_defaults:
        ppl_config : str | PplConfig = _create_default_config(

        )
    else :
        pass
    cache = ""
    pipeline_emit = ""
    encountered_errors = False
    
    def _run_workflow(
            prg_rep : ProgressReporter | None
    ):
        
        for output in _run_pipeline(prg_rep=prg_rep):
            pass


    # input_table()
    # select()
    # join()
    # binarize()
    # output_table()

def _enable_logging(
        root_dir:str,
        run_id:str,
        verbose:bool) -> None :
    loggig_file=(
        Path(root_dir) / "output" / run_id / "reports" / "indexing-engine.log"
    )
    loggig_file.parent.mkdir(parents=True, exist_ok=True)

    loggig_file.touch(exist_ok=True)

def _get_prg_rep(rep_type:str|None)->ProgressReporter:
    if rep_type is None or rep_type == "rich":
        return None
    if rep_type == "print":
        return None
    if rep_type == "none":
        return None
    
    msg = f"Invalid progress reporter type : {rep_type}"
    raise ValueError(msg)


def _init_project(path:str, prg_rep:ProgressReporter) -> None:
    prg_rep.info(f"Initializing project at {path}")
    root = Path(path)
    if not root.exists():
        root.mkdir(parents=True, exist_ok=False) ## test exist_ok flag's 
    
    settings_yaml = root / "settings.yaml"
    if settings_yaml.exists():
        msg = f"Project already initialized at {root}"
        raise ValueError(msg)
    
    dotenv = root / ".env"
    if not dotenv.exists():
        with settings_yaml.open('w') as file:
            file.write(INIT_YAML)

    with dotenv.open('w') as file:
        file.write(INIT_DOTENV)

    prompts_dir = root / "prompts"

    if not prompts_dir.exists():
        prompts_dir.mkdir(parents=True, exist_ok=True)
    
    entity_extr = prompts_dir / "entity_extr.txt"
    if not entity_extr.exists():
        with entity_extr.open('w') as file:
            file.write(GRAPH_EXTRACTION_PROMPT)
    
    community_report = prompts_dir / "community_report.txt"
    if not community_report.exists():
        with community_report.open('w') as file:
            file.write(COMMUNITY_REPORT_PROMPT)

