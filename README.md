####OpenCV face detection from EEN video####

This project uses the OpenCV library and a little python to loop through the EEN generated thumbnails and identify faces.  

The get.py script pulls the last 500 thumbnails for a given camera:

    python get.py <username> <password> <camera_esn>

It will store the images in the src directory

    python example.py

It draws a green box around the face and saves the image in the done foler.

####Tips and Tricks####

    # deletes small files
    find -size -3b | xargs rm -f;

    # start webserver to easily share files
    python -m SimpleHTTPServer 8000
 
