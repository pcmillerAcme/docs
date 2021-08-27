
.. |br| raw:: html

   <br />

Endpoints
#########

/new
""""

``/new`` starts the creation process of a new animated code and returns a JSON formatted response containing the **Order Number** to be used for all subsequent queries about (and certain limited updates to) the started animation. Also, the final media file location will be returned, though it will not be available until the progress endpoint indicates creation is complete.


Example:
::

    GET https://api.acme.codes/new?msg=HelloQrScannersOfTheWorld!

Return JSON:
::

    {"orderNumber": "1629832688_3F9UYOQ9", "mp4": "https://api.acme.codes/orders/1629832688_3F9UYOQ9/AcmeCode_810403.mp4"}

Note if a custom image it to be integrated into the code, this endpoint must be targeted with a POST, along with the image in the post body.
::

    POST https://api.acme.codes/new?msg=ThisCodeHasAnImage!

See the `Parameters <./Parameters.html>`_ definition for the options affecting QR code creation, and SDK for working service call examples.

/orders/#/progress
""""""""""""""""""

The /orders/#/progress endpoint returns a JSON-formatted response indicating the current state of code creation. Since animated QR code creation time is highly variant (minimum times of a few seconds and maximum times up to 30 minutes), calling this resource is essential to confirm that animation creation is proceeding, and knowing when creation has  completed, at which point the last call of retrieving the animation media file (mp4, gif, fbx) can be done.

Returned values include:

“progress”:  float value in the range [0-100] which represents the percentage of completion for the most recently requested animated code.

“stage”: a string description of the type of work currently being done to create the order. Example values include:

'Order Creation'
'Order Definition'
'Animation'
'Rendering'
'Watermarking'
'Gif Creation'
'Mp4 Creation'
'Internal File Verification'
'External File Verification'
'Order Complete'


“queue”: an integer of the count of un started orders currently in the request queue. If queue is non-zero, the system is at maximum capacity and progress speed will be delayed. If queue is non-zero, most front end client systems communicate this information to users to help assure them as to why processing is slower than usual.

Example URL:

https://api.acme.codes/orders/1444979323_ODFAUQSE/progress

Example return values:
::

    {"queue": 10, "progress": 0, "stage": "Workspace Creation"}
    {"queue": 0, "progress": 3, "stage": "Order Creation"}
    {"queue": 0, "progress": 15.9 "stage": "Animation"}
    {"queue": 0, "progress": 55.6, "stage": "Rendering"}
    {"queue": 0, "progress": 100, "stage": "Order Complete"}

/orders/#/<mediaFile>
"""""""""""""""""""""

The /orders/#/<mediaFile> refer to target mp4, fbx, gif, png, or zip files. This endpoint is rarely derived because the full path to this endpoint and the target media file to be retrieved is always returned in the response to the original call to ``/new``

/anims
""""""

The /anims resource returns a machine readable JSON-formatted response flat list of available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource.

.. code-block:: javascript

    ["Breeze", "Breeze_Long", "Circle", "Circle_Ducks", "Cube", "Cubie", "Cubie_Image", "Cubist_Smooth", "Exchange", "Graviton", "Gravity", "Kaleidoscope", "Kaleidoscope_OffsetA", "Kaleidoscope_OffsetB", "Pinwheel", "Pinwheel_Walking", "Quicksilver", "Spin", "Spin_Right", "Spinfast", "Spinfast_Right", "SpriteSquad", "Still", "Vanish"]

Real time example link:

`https://api.acme.cdes/anims <https://api.acme.codes/anims>`_

/anims/<anim>
"""""""""""""

More detailed information on each animation is available in the corresponding path. |br|
Example details include internal animation block timing, animation lable tag values, default time length, and current retail prices.

.. code-block:: javascript

    {"length": null, "blocks": [[0, 10]], "price": 1.0, "tags": ["qrcode", "spin", "rotating", "constant", "image", "clockwise", "3d"]}

Real time example link:

`https://api.acme.cdes/anims/Spin <https://api.acme.codes/anims/Spin>`_


/version
""""""""

This resource returns a JSON-formatted response containing software build and date information about this service.

.. code-block:: javascript

    {"buildNumber": 12123, "buildTime": "Mon Aug 23 15:41:41 2021", "version": "0.8", "branch": "master", "buildMachine": "RCentral_bf03"}

Real time example link:

`https://api.acme.cdes/version <https://api.acme.codes/version>`_


