#!/bin/bash
# Disable GPU
# Run Python scripts in the background
python ./src/client0.py &
python ./src/client1.py &
python ./src/client2.py #&
# python ./src/client3.py &
# python ./src/client4.py &
# python ./src/client5.py &
# python ./src/client6.py &
# python ./src/client7.py &
# python ./src/client8.py &
# python ./src/client9.py #&
# # python ./src/client10.py &
# python ./src/client11.py &
# python ./src/client12.py &
# python ./src/client13.py &
# python ./src/client14.py &
# python ./src/client15.py &
# python ./src/client16.py &
# python ./src/client17.py &
# python ./src/client18.py &
# python ./src/client19.py &
# python ./src/client20.py #&
# python ./src/client21.py &
# python ./src/client22.py &
# python ./src/client23.py &
# python ./src/client24.py &
# python ./src/client25.py &
# python ./src/client26.py &
# python ./src/client27.py &
# python ./src/client28.py &
# python ./src/client29.py &
# python ./src/client30.py &
# python ./src/client31.py &
# python ./src/client32.py &
# python ./src/client33.py &
# python ./src/client34.py &
# python ./src/client35.py &
# python ./src/client36.py &
# python ./src/client37.py &
# python ./src/client38.py &
# python ./src/client39.py &
# python ./src/client40.py &
# python ./src/client41.py &
# python ./src/client42.py &
# python ./src/client43.py &
# python ./src/client44.py &
# python ./src/client45.py &
# python ./src/client46.py &
# python ./src/client47.py &
# python ./src/client48.py &
# python ./src/client49.py 

# Wait for all background jobs to finish
wait

echo "All scripts have finished executing."
