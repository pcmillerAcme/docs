
.. |br| raw:: html

   <br />

mp4
###

``/orders/<order number>/mp4``

`Mp4 <https://en.wikipedia.org/wiki/MPEG-4_Part_14>`_ files are the most common and popular ACME deliverable for completed animation files. Mp4 files are the best combination of small size and system display compatability  - though still not as widely compatible as gif files, which are almost universally displayable. Mp4 files also support much more precise timing during playback than gifs, and also can support embedded sound.

mp4
"""

This standard mp4 resource returns the complete animated mp4 binary stream. Other than individual rendered frames, mp4 is the most quickly completed format of the animation formats provided by ACME. After frames are created, mp4 files are usually generated in less than a second. Still, it is always recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100, then request the mp4 file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4

mp4/[timestamp]
"""""""""""""""

This resource is an alias to /orders/**[#]**/mp4. This is a convenience resource which is helpful in some programmatic circumstances to bypass the caching mechanism of client-side frameworks. By putting any timestamp (TS) value after mp4, the client code is forced - through this resource alias - to always get the latest /orders/**[#]**/mp4. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4/1464382911

mp4-file
""""""""

This resource returns the same mp4 stream as the above, but when called from within a browser, a "File Save As..' dialog box will appear asking the user where they would like to download the remote file to. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4-file

mp4-file-info
"""""""""""""

This resource returns a JSON-formatted response containing a 'fileSize' key:value pair. The value of fileSize is zero until the file creation is completed, at which point it is permanently the file size of the finished mp4 animation file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4-file-info

Example return value:
::

    {"fileSize":  114656}

anim.mp4
""""""""

This alternative mp4 resource returns the mp4 of an animation order via a static web hosting directory. This is provided for certain browsers which can be extremely particular about the data structures of streamed media data, and as a result the standard /mp4 resource above will not load on these browsers. Using this anim.mp4 resource instead serves as a workaround for users wanting more broad browser support. One result of this file based support however is a much shorter provided download time from ACME; anim.mp4 files are deleted from availability within 3 hours. Since all users are expected to attain their mp4s upon animation completion, this short time window is not known to be a problem, and again the standard mp4 resource is available for much longer. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/anim.mp4

    
