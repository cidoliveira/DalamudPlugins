"""Merge plugins/*.json into pluginmaster.json, the file Dalamud reads.

Usage:
    python tools/build_pluginmaster.py

Each plugins/<Name>.json holds one plugin's manifest: the plugin's packaged manifest plus its
download links. Dalamud expects a list of them, so this sorts and concatenates them, refusing a
manifest that's missing what Dalamud needs to list or install the plugin.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ("InternalName", "Name", "Author", "AssemblyVersion", "DalamudApiLevel", "DownloadLinkInstall")


def load(path: Path) -> dict:
    with path.open(encoding="utf-8-sig") as f:
        manifest = json.load(f)
    missing = [key for key in REQUIRED if not manifest.get(key)]
    if missing:
        raise ValueError(f"{path.name}: missing {', '.join(missing)}")
    manifest.setdefault("DownloadLinkUpdate", manifest["DownloadLinkInstall"])
    manifest.setdefault("DownloadLinkTesting", manifest["DownloadLinkInstall"])
    return manifest


def main() -> int:
    manifests = [load(path) for path in sorted((ROOT / "plugins").glob("*.json"))]
    names = [m["InternalName"] for m in manifests]
    duplicates = {name for name in names if names.count(name) > 1}
    if duplicates:
        print(f"Duplicate InternalName: {', '.join(sorted(duplicates))}", file=sys.stderr)
        return 1
    manifests.sort(key=lambda m: m["Name"].lower())
    output = ROOT / "pluginmaster.json"
    with output.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(manifests, f, ensure_ascii=False, indent=2)
        f.write("\n")
    for m in manifests:
        print(f"{m['Name']} ({m['InternalName']}) {m['AssemblyVersion']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
