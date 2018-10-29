import subprocess
import os

def add_gvm_segment(powerline):
    env = os.getenv('GVM_ROOT')
    if env is None:
        return

    cmd_result = subprocess.check_output('gvm-prompt')
    go_version = cmd_result.decode('utf-8').split('\n')[0]
    bg = Color.GVM_BG
    fg = Color.GVM_FG
    powerline.append(' %s ' % go_version, fg, bg)
