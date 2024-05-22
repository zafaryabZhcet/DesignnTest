#!/bin/bash

# Run Python scripts in the background
python script1.py &
python script2.py &
python script3.py &
python script4.py &

# Wait for all background jobs to finish
wait

echo "All scripts have finished executing."