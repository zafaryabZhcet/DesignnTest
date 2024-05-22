#!/bin/bash

# Run Python scripts in the background
python ./src/client0.py &
python ./src/client1.py &
python ./src/client2.py &
python ./src/client3.py &
python ./src/client4.py
# python ./src/client5.py &
# python ./src/client6.py &
# python ./src/client7.py &
# python ./src/client8.py &
# python ./src/client9.py &

# Wait for all background jobs to finish
wait

echo "All scripts have finished executing."
