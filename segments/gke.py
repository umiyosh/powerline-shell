import subprocess
import re


def add_gke_segment(powerline):
    match = '.+cluster:.+'
    cluster_name = None
    prompt_prefix = ' ⎈ : '.decode('utf-8')
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
            cluster_name = result.split()[1] + ' '

    fore_ground = Color.GKE_FG
    back_ground = Color.GKE_BG
    if 'prd' in cluster_name:
        fore_ground = Color.GKE_PRD_FG
        back_ground = Color.GKE_PRD_BG
    if cluster_name:
        powerline.append(prompt_prefix + cluster_name, fore_ground, back_ground)
    else:
        return
