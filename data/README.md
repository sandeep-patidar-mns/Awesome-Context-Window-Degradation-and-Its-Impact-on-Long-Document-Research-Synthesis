# Data Directory Guide

This directory documents dataset acquisition, licensing, schema, and preprocessing rules for the experimental study.

**Guidelines**:
- Do not commit restricted, proprietary, or oversized raw datasets directly to version control.
- Provide automated download scripts and checksum validation in `scripts/`.
- Ensure strict data separation (train / validation / test) to prevent data leakage.
