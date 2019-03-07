
.. |br| raw:: html

   <br />

mp4
###

This resource returns the complete animated `mp4 <https://en.wikipedia.org/wiki/MPEG-4_Part_14>`_ binary stream. Other than individual rendered frames, mp4 is the most quickly completed format of the animation formats provided by ACME. Still, it is always recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100, then request the mp4 file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4

mp4/[timestamp]
###############

This resource is an alias to /orders/**[#]**/mp4. This is a convenience resource which is helpful in some programmatic circumstances to bypass the caching mechanism of client-side frameworks. By putting any timestamp (TS) value after mp4, the client code is forced - through this resource alias - to always get the latest /orders/**[#]**/mp4. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4/1464382911

mp4-file
########

This resource returns the same mp4 stream as the above, but when called from within a browser, a "File Save As..' dialog box will appear asking the user where they would like to download the remote file to. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4-file

mp4-file-info
#############

This resource returns a JSON-formatted response containing a 'fileSize' key:value pair. The value of fileSize is zero until the file creation is completed, at which point it is permanently the file size of the finished mp4 animation file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4-file-info

Example return value:
::

    {"fileSize":  114656}

    
