def add_gke_segment(powerline):
    import subprocess
    import re
    match = '.+cluster:.+'
    cluster_name = None
    prompt_prefix = '⎈ :'
    kube_cmd = [
        'kubectl',
        'config',
        'view',
        '--minify',
    ]
    cmd_result = subprocess.check_output(kube_cmd)
    results = cmd_result.split('\n')
    for result in results:
        if re.match(match, result):
            cluster_name = result.split()[1]

    if cluster_name:
        powerline.append(cluster_name, Color.GKE_FG, Color.GKE_BG)
    else:
        return
