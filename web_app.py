import streamlit.web.cli as stcli
import os, sys

def resolve_path(path):
    basedir = getattr(sys, '_MEIPASS', os.getcwd())
    return os.path.join(basedir, path)

if __name__ == "__main__":
    # Yahan 'app.py' aapki main file ka naam hona chahiye
    sys.argv = [
        "streamlit",
        "run",
        resolve_path("app.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())
