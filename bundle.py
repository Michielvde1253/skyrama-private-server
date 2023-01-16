import sys
import os

# Bundled data (extracted to a temp dir)

TMP_BUNDLED_DIR = sys._MEIPASS if getattr(sys, 'frozen', None) else "."

ASSETS_DIR = os.path.join(TMP_BUNDLED_DIR, "assets")
TEMPLATES_DIR = os.path.join(TMP_BUNDLED_DIR, "templates")
STUB_DIR = os.path.join(TMP_BUNDLED_DIR, "stub")
STYLES_DIR = os.path.join(TMP_BUNDLED_DIR, "templates", "styles")

