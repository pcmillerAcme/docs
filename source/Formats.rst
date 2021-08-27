
.. |br| raw:: html

   <br />

Formats
#######


.. _output:

Output
------

Acme's API can return the following file formats:

-  `mp4 <https://en.wikipedia.org/wiki/MPEG-4_Part_14>`_  |br| The industry standard compressed movie file playable on almost any modern system. This is the default deliverable format for all ACME animated QR codes. |br|  |br|
-  `png <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`_  |br|  Web standard image file format; used to return individual animation frames for customers requiring uncompressed animation quality. |br|  |br|
-  `gif <https://en.wikipedia.org/wiki/GIF>`_   |br|  Most widely displayable format, comes at the costs of large file size, long creation times, and reduced color palettes. Default is off. |br|  |br|
-  `fbx <https://en.wikipedia.org/wiki/FBX>`_   |br| 3d industry standard scene definition file. Default is off. |br|  |br|
-  `zip <https://en.wikipedia.org/wiki/ZIP_(file_format)>`_   |br| Compressed file containing all frames of an animation; used by customers wanting to apply their own compression into animation files. Available to subscribers only. |br|  |br|

All of the above formats can be directly toggled on or off as arguments to the ``/new`` endpoint when each animation is created.


.. _input:

Input
-----

Images can be uploaded to ACME's api to be integrated in each custom animation. **We recommend only uploading the most commonly supported formats, such as jpg/jpeg, tif, and png.** Our pipeline will accept a much broader set of file format extensions:

    'bmp',
    'deepexr',
    'dib',
    'eps',
    'exr',
    'gif',
    'icns',
    'ico',
    'im',
    'jpeg',
    'jpg',
    'msp',
    'paml',
    'pcx',
    'pdf',
    'ppm',
    'png',
    'sgi'
    'spider'
    'svg'
    'tga',
    'tif',
    'webp',
    'xbm',
    'xvThumbnails'

However, within each of these formats, many different options form an ocean of different option sets which we cannot support. If this occurs, please take the time to convert your image files to a more common industry standard file - say one that can be displayed on a web browser - before uploading them to our service to be animated.
|br|
|br|
A note on gifs: We have found on occasion some customers upload animated gifs into our pipeline. This is not currently supported - only the first frame of the gif will be integrated. This is an option for customers willing to pay for custom animation creation. Contact sales@acme.codes if interested in this kind of hybrid animation.
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|

