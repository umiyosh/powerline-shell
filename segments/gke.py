import subprocess
import re


def add_gke_segment(powerline):
    cluster_match = '.+cluster:.+'
    namespace_match = '.+namespace:.+'
    cluster_name = None
    namespace_name = None
    if not py3:
        prompt_prefix = ' ⎈ : '.decode('utf-8')
    else:
        prompt_prefix = ' ⎈ : '
    kube_cmd = [
        'kubectl',
        'config',
        'view',
        '--minify',
    ]
    cmd_result = subprocess.check_output(kube_cmd)
    results = cmd_result.decode('utf-8').split('\n')
    for result in results:
        if re.match(cluster_match, result):
            cluster_name = result.split()[1] + ' '
        if re.match(namespace_match, result):
            namespace_name = result.split()[1] + ' '

    cluster_fore_ground = Color.GKE_FG
    cluster_back_ground = Color.GKE_BG
    namespace_fore_ground = Color.GKE_NS_FG
    namespace_back_ground = Color.GKE_NS_BG
    if 'prd' in cluster_name:
        cluster_fore_ground = Color.GKE_PRD_FG
        cluster_back_ground = Color.GKE_PRD_BG
    if cluster_name and namespace_name:
        #  if cluster_name :
        powerline.append(prompt_prefix + cluster_name, cluster_fore_ground,
                         cluster_back_ground)
        powerline.append(namespace_name, namespace_fore_ground,
                         namespace_back_ground)
    elif cluster_name:
        powerline.append(namespace_name, namespace_fore_ground,
                         namespace_back_ground)
    else:
        return
