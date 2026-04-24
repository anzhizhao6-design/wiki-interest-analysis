#!/bin/bash

echo "Starting Wikipedia Interest Analysis Tool..."

# 自动进入虚拟环境
source venv/bin/activate

echo "Choose mode:"
echo "1. Run Streamlit UI"
echo "2. Run CLI (main.py)"

read choice

if [ "$choice" = "1" ]; then
    echo "Launching Streamlit UI..."
    streamlit run app.py
elif [ "$choice" = "2" ]; then
    echo "Running CLI pipeline..."
    python3 main.py
else
    echo "Invalid choice"
fi