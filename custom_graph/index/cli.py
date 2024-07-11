from pathlib import Path
from custom_graph.index.progress import ProgressReporter
from custom_graph.index.run import _run_pipeline

def index_cli(init:bool, root:str):
    prg_rep = ProgressReporter()
    if init:
        init_project(root, prg_rep)
        return
    
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


def init_project(path:str, progress_report:ProgressReporter):
    root = Path(path)
    root.mkdir(parents=True, exist_ok=True)
    if progress_report:
        progress_report.info("Initialize the custom_graphrag project")