from pycloudflared import try_cloudflare

from modules.shared import cmd_opts

from gradio import strings

import os

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    try:
        tunnel_url = try_cloudflare(port=port, verbose=False)
        os.environ['webui_url'] = tunnel_url.tunnel
        colab_url = os.getenv('colab_url')
        strings.en["SHARE_LINK_MESSAGE"] = f"Public WebUI Colab URL: {tunnel_url.tunnel}"
    except RuntimeError:
        print("[1;33mCloudflared failed to start. Use the public link instead.") #yellow color
        print('[0m') #revert the color back to default
    
