
.. |br| raw:: html

   <br />

fbx
###

 ``/orders/<order number>/fbx``

`FBX <https://en.wikipedia.org/wiki/FBX>`_ files are an industry standard file format for exchanging animated 3d files between 3d apps. This data is not rendered images, but rather the original 3d scene information. Since no rendering or encoding is necessary, this ACME product take very little time to complete within the request pipeline.

fbx
"""

This resource returns the complete animated FBX binary stream. There is a high variability of time to completion as driven by animation complexity, including times that may exceed the timeout period of some browsers. It is therefore recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100, then request the fbx file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx

fbx/[timestamp]
"""""""""""""""

This resource is an alias to /orders/**[#]**/fbx. This is a convenience resource which is helpful in some programmatic circumstances to bypass the caching mechanism of client-side frameworks. By putting any timestamp (TS) value after fbx, the client code is forced - through this resource alias - to always get the latest /orders/**[#]**/fbx. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx/1464382911

fbx-file
""""""""

This resource returns the same fbx stream as the above, but when called from within a browser, a "File Save As..' dialog box will appear asking the user where they would like to download the remote file to. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx-file

    
fbx-file-info
"""""""""""""

This resource returns a JSON-formatted response containing a 'fileSize' key:value pair. The value of fileSize is zero until the file creation is completed, at which point it is permanently the file size of the finished fbx animation file. Example URL:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx-file-info

Example return value:
::

    {"fileSize":  1124656}

    
