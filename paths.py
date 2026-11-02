"""Folders the pipeline writes to, anchored to this repository rather than the
current working directory, so running main.py from anywhere writes to the same place."""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
