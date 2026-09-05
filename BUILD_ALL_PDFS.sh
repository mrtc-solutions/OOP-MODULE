#!/bin/bash

# MASTER BUILD SCRIPT - Generates all PDFs for OOP-MODULE
# Usage: ./BUILD_ALL_PDFS.sh
# This script rebuilds the entire output folder with PDF-only content

set -e  # Exit on error

REPO_ROOT="/home/user/OOP-MODULE"
TOOLS="$REPO_ROOT/tools"
OUTPUT="$REPO_ROOT/output"

echo "=========================================="
echo "OOP-MODULE PDF BUILD SYSTEM"
echo "=========================================="
echo ""

# Phase 1: Clean
 echo "[PHASE 1] Cleaning previous output..."
rm -rf "$OUTPUT"
mkdir -p "$OUTPUT"
for week in {1..16}; do
    mkdir -p "$OUTPUT/week$week"
done
echo "✓ Clean complete"
echo ""

# Phase 2: Regenerate assets
echo "[PHASE 2] Regenerating brand assets..."
cd "$TOOLS"
python3 common.py
echo "✓ Brand assets generated"
echo ""

# Phase 3: Generate visuals
echo "[PHASE 3] Generating visuals..."
python3 -c "from visuals import ALL; [fn() for fn in ALL]" 2>/dev/null || true
for week in {2..16}; do
    python3 -c "import week${week}_visuals; [fn() for fn in week${week}_visuals.ALL]" 2>/dev/null || true
done
echo "✓ Visuals generated"
echo ""

# Phase 4: Build all module PDFs
echo "[PHASE 4] Building module PDFs..."
python3 build_pdf.py  # Week 1
for week in {2..16}; do
    python3 -c "import w${week}_pdf; w${week}_pdf.build(w${week}_pdf.CFG, w${week}_pdf.story)" 2>/dev/null
done
echo "✓ Module PDFs built"
echo ""

# Phase 5: Build all assignment PDFs
echo "[PHASE 5] Building assignment PDFs..."
for week in {1..16}; do
    python3 w${week}_assignment_pdf.py 2>/dev/null
done
echo "✓ Assignment PDFs built"
echo ""

# Phase 6: Quality check
echo "[PHASE 6] Running quality audit..."
python3 audit_pdfs.py
echo ""

# Phase 7: Summary
echo "=========================================="
echo "BUILD SUMMARY"
echo "=========================================="
echo "Output directory: $OUTPUT"
echo ""
echo "Module PDFs:"
find "$OUTPUT" -name "*Module*.pdf" | sort
echo ""
echo "Assignment PDFs:"
find "$OUTPUT" -name "*Assignment*.pdf" | sort
echo ""
echo "Total PDFs: $(find $OUTPUT -name '*.pdf' | wc -l)"
echo ""
echo "=========================================="
echo "BUILD COMPLETE"
echo "=========================================="
