from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics

def child_exit(server, worker):
    """
    Docstring for child_exit
    
    :param server: Description
    :param worker: Description
    """
    GunicornInternalPrometheusMetrics.mark_process_dead_on_child_exit(worker.pid)