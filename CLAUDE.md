# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a HALE UAV (High-Altitude Long-Endurance Unmanned Aerial Vehicle) research project - an academic engineering thesis/project. The repository contains:

- **Research papers** (`downloaded_pdfs/`, `existing_pdfs/`) - Literature on solar-powered UAVs, aeroelasticity, structural design, flight control
- **Project reports** (`main reports/`, `second_report/`) - Thesis documentation
- **Data collection script** (`download_papers.py`) - Web scraper for downloading relevant PDFs

## Python Environment

Dependencies are in `requirements.txt`:
- requests
- beautifulsoup4
- fake-useragent

A virtual environment exists at `venv/`. Activate with:
```bash
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Main Script

**download_papers.py** - Searches DuckDuckGo for HALE UAV-related PDFs and downloads them to `downloaded_pdfs/`. Uses multiple search queries covering:
- Core solar HALE UAV design
- Energy & power systems (MPPT, batteries, solar cells)
- Aerodynamics & flexible wing structures
- Flight control & mission planning
- Specific vehicles (Zephyr, Helios, AtlantikSolar)

Run:
```bash
python download_papers.py
```

## Directory Structure

## Directory Structure

hale_uav_research/
├── download_papers.py          # PDF downloader/scraper
├── requirements.txt            # Python dependencies
├── downloaded_pdfs/            # Downloaded research papers (primary literature pool)
├── existing_pdfs/              # Reference PDFs, original design papers
├── Personal Findings/          # My own analysis notes and simulation findings
│   └── HALE_UAV_Technical_Report.md  # Personal technical summary
├── main reports/               # Semester-wise submitted reports (read-only reference)
│   └── EYP Report 8th Sem.pdf  # Last submitted report
└── second_report/              # Active working directory for new report
    ├── report_v4.md            # CURRENT LATEST VERSION — use as baseline
    ├── report_outline.md       # Section structure to follow
    ├── citation_rules.md       # Citation format rules — always follow this
    └── source_mapping_v3.md    # Which paper maps to which claim

## Key Research Topics

The project focuses on:
- Solar-powered UAV design methodology
- Very flexible aircraft aeroelasticity
- Lightweight composite structures
- Energy management systems
- Perpetual endurance flight

## Report Writing Rules

- **Baseline**: Always read `second_report/report_v4.md` first before any writing task
- **Output**: New content goes into `second_report/report_v5.md` (create if missing, copy v4 as base)
- **Citations**: Always follow `second_report/citation_rules.md` — never invent citation formats
- **Source mapping**: Update `second_report/source_mapping_v3.md` when adding new cited papers
- **Do NOT rewrite** existing sections unless I explicitly say so
- **Do NOT delete** content — only append or refine
- When researching new topics, use subagents to read PDFs so main context stays clean
- Ask before making structural changes to the report outline

# Academic Report Proofreading Agent

This agent coordinates 24 specialist sub-agents to deliver comprehensive proofreading of academic reports. Each sub-agent targets a distinct quality dimension. Run this agent against any academic report file to receive structured, actionable feedback across all areas.

---

## Usage

claude "Proofread the academic report at ./second_report/report_v4.md using the academic proofreading agent"

Or reference a `.txt` / `.md` / `.docx` file:

```bash
claude "Run the full academic proofreader on ./my_report.md"
```
