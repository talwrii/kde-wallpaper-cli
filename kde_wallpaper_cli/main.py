#!/usr/bin/env python
import argparse
import subprocess
import shutil

from pathlib import Path


def set_wallpaper(p: Path):
    p = p.resolve()

    script = """
    desktops().forEach(d => {
        d.currentConfigGroup = Array("Wallpaper",
                                     "org.kde.image",
                                     "General");
        d.writeConfig("Image", "file://FILEPATH");
        d.reloadConfig();
    });
    """.replace("FILEPATH", str(p))


    if shutil.which("qdbus6"):
        prog = "qdbus6"
    elif shutil.which("qdbus5"):
        prog = "qdbus5"
    elif shutil.which("qdbus"):
        prog = "qdbus"

    cmd = [
        prog,
        "org.kde.plasmashell",
        "/PlasmaShell",
        "org.kde.PlasmaShell.evaluateScript",
        script,
    ]

    subprocess.check_call(cmd, stdout=subprocess.DEVNULL)


PARSER = argparse.ArgumentParser(description='Set wallpaper for KDE', epilog="@readwithai 📖 https://readwithai.substack.com/p/my-productivity-tools ⚡️ machine-aided reading ✒️")
PARSER.add_argument('file')

def main():
    args = PARSER.parse_args()
    set_wallpaper(Path(args.file))


if __name__ == "__main__":
    main()
