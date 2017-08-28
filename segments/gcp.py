def add_gcp_segment(powerline):
    import os
    gcpconfig = os.path.expanduser('~/.config/gcloud/active_config')

    if os.path.exists(gcpconfig):
        with open(gcpconfig, 'r') as gf:
            conf = gf.read()
    else:
        return

    powerline.append(conf, Color.GCP_FG, Color.GCP_BG)
