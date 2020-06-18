
.. |br| raw:: html

   <br />

new
###

``/new`` 


``/new`` starts the creation process of a new animated code and returns a response containing the **Order Number** to be used for all subsequent queries about (and certain limited updates to) the started animation. 


Example:
::

    GET: https://api.acme.codes/new?msg=HelloQrScannersOfTheWorld!
    
Example return value:
::

    {"orderNumber": "1444720642_NLGEDCVP"}

|br|
**Below are the optional arguments when calling the** ``/new`` **resource:**


.. _apiKey:

apiKey
------

First, it's important to remember that sending a value for the ``apiKey`` argument is optional; we do this so any developer can learn, experiment with, and integrate the API at any time. See the SDK section of this documentation for working examples to be used by anyone. Of course, if no ``apiKey`` argument is supplied, the service will watermark the custom portions of the animation and limit the embedded message to a demo page that proves the message can be put into the code by our API, but limits any practical use of the code.
|br|
|br|
To generate animated codes without watermarking and without message demo wrapping, a valid `API Key <https://en.wikipedia.org/wiki/Application_programming_interface_key>`_ associated with a paid subscription to ACME.CODES must be subitted in this argument. Contact sales@acme.codes to be given a temporary "try-it-out" API key or purchase a permanent API Key for completely unlocked codes.

.. _anim:

anim
----

The animation to be applied to the code. See ``anims-json`` and ``animation-list`` resources for a complete list of valid values for anim. Default = 'Exchange'. 

.. _applyFrameNumbers:

applyFrameNumbers
-----------------

This setting allows for diagnostic per frame overlays of a frame hand and frame count to ensure altered animations are rendered correctly for expected total and block times.

.. _bgpColor:

bgpColor
--------

Background Plate Color. Background color. Default = '``FFFFFF``' (White). Multiple hex color values can be supplied separated by commas for multi color options. Green background example: ``https://api.acme.codes/new?bgpColor=00FF00``


.. _bitRate:

bitRate
-------

Bitrate argument for encoding mp4 files. Defines the target bitrate for the mp4 streaming encoder. Default is 0; when set to 0, allows the mp4 encoder to adjust the bitrate as can be best for the animation. When explicitly set, the higher this number, the higher the quality of the delivered mp4 file, as well as the larger the mp4 file size. Example to create a higher than normal fidelity mp4 file: ``https://api.acme.codes/new?bitRate=1200``

.. _blocks:

blocks
------

One of ACME's most popular arguments for refining generated animations to preference. For any given animation, ``blocks=`` allows for arbitrary timing of the blocked portions of the animation. Each animation has default block timing; for example, the block timing of a code to image and back animation would be 2 seconds of the code, two seconds animating to the image, 2 second hold of the image, and finally 2 second animation back to the code. (Note: the last two seconds are so 'minus the last frame' in order to support smooth looping transitions.) ``blocks=`` allows for overriding of any animation's default block timing. |br| |br| So, say an animation is wanted that instead animates the code display for one second, then animates to the image in 5 seconds, then holds the image for 2 seconds, then animates back to the code in 3 seconds. With the block argument comma separated values representing the absolute times for blocks to start and stop, the needed argument would be ``blocks=0-1,1-6,6-8,8-11``. All values are in seconds, not frames. |br| |br| Float values fully supported: ``0-2.44,2.44-6`` is ok. |br| |br| It is important to note some animations have only one block (Spin for example), while others usually have 4, and still others have overlapping animation block times. Default block values are given with the ``/anims-json`` resource. ``blocks`` values are also subjected to the ``length`` argument. 
   

.. _cdn:

cdn
---

For paying subscribers only, this argument flags the request for animation files to be automatically uploaded to our Cloud Service Provider. Default value is 0. When set to 1/True, generated animation product files will be uploaded to a dynamically determined subdirectory of one of ACME's CDN endpoint domains. See the `CDN section <https://acme.readthedocs.io/en/latest/CDN.html>`_ of this documentation for more details. Note this argument must be accompanied with an apiKey associated with a CDN subscription account enabled by ACME.

For example, a subscriber who as paid for CDN services can call:

``https://api.acme.codes/new?cdn=1&apiKey=<yourApiKeyHere>&gif=0&fbx=0&msg=helloFromAcme``

which will generate a response with the additional information of the location of where the published animation files will be available after ``progress`` is 100:

``{"orderNumber": "1576574190_8Z0U000D", "cdnMp4": "https://cdn.api.acme.codes/2019/12/17/e4983b0f-3688-48c1-a49a-f9345a5fb703/AcmeCode_283150.mp4"}``

.. _chromaRange:

chromaRange
-----------

Supports the breadth of color range to be used in chromaKeys arg. Default value is 5.


.. _fbx:

fbx
---

Create fbx file. Default=True


.. _fitFactor:

fitFactor
---------

This controls the fraction of the framed code which fills the camera view. If set to a low values close to ``0``, the code will be very small in the frame, while if set to 1, the code will touch the borders. Note that some animations will alter the default fitFactor to ensure all of the animation is properly viewable, but explicit setting of fitFactor will override animation influences. Default is ``fitFactor=0.9``


.. _format:

format
------

The desired format of the return value. Default = 'JSON'. Usually format is left undeclared in order inherit the default 'JSON'. However, two other options exist: 'html' and 'png'. |br| |br| The 'html' option exists for people interatcing and learning about the ACME API with a browser, and will return an html web page containing a clickable link to the final order products. This can be useful for interactive demonstration, testing, and verification of the API directly without relying on a more complex GUI front end. Without the 'html' option and without a front end, the user is left to parse raw JSON and manually assemble the URL, which is not fun for anything but scripts. |br| |br| Also, there is the 'png' format option, which directly returns a png file format **only if non-animated codes have been requested** with ``anim=staticCodeOnly``. See '`Non-animated Codes <https://acme.readthedocs.io/en/latest/Non-animated%20Codes.html>`_' for details.  |br| |br|  Examples: |br| |br| ``https://api.acme.codes/new?format=JSON`` (Default) |br| |br| ``https://api.acme.codes/new?format=html`` |br| |br| ``https://api.acme.codes/new?format=png&anim=staticCodeOnly``


.. _fps:

fps
---

Another one of ACME's popular settings; Frames Per Second. All animations are defined in terms of time, so any animation can be rendered at any industry standard FPS while maintaining the same animation timing. The higher the FPS, the higher the 'look and feel' of the smoothness of the animation. At the time of this document's writing, the ACME default is 15FPS, but this will soon shift to 30FPS. Control over FPS can have significant effect over final animation file size, in particular gif files.


.. _frameNumber:

frameNumber
-----------

Limits the generation of the animation to one specific frame. Use of this is discouraged for normal use. Normal access of individual frames should be through the /orders/[Order#]/frames/[n] resource. However, if the user is creating test suites or similar use cases where it is known in advance that only one frame is needed, it can be helpful to use this argument to optimize test execution time by limiting generated output to just one frame.


.. _frames:

frames
------

Create rendered frames file. Default=True. Required for most usage. By turning off, delivery times for fbx files is reduced, which is helpful for people wanting only digital 3d files.


.. _gif:

gif
---

Create gif file. Default=True. Note gif generation requires the longest processing time of all other creation processes.


.. _imageRotation:

imageRotation
-------------

The rotation to be applied to a supplied image URL.
Eample:
``https://api.acme.codes/new?anim=Spin&img1=https://www.acme.ink/demos/acmecodes/tImg/img1.png&imageRotation=90``


.. _img1:

img1
----

The image URL to be applied within the animation, if supported by the selected animation. 

Example:
``https://api.acme.codes/new?anim=Spin&img1=https://www.acme.ink/demos/acmecodes/tImg/img1.png``

Overview: there are two ways to supply an image to an ACME animation:

1. At initial order creation time, by supplying a URL to an image published on the internet via the ``img1=`` argument for the ``/new`` resource, an image can be inserted into an animation right from the start. The advantage here is the image goes in 'all at once' in *one* call. The disadvantage is the image must already exist over http/https and be published on the internet before the call to ``/new`` is made. 
|br|
|br|
2. Alternatively, a different call sequnce can be used. After the intial order has been created via a call to ``/new``, a POST of an image to the ``image`` resource will trigger the order animation to be refreshed after order upload is complete. The advantage is the image need never be published on the internet, while the disadvantage is that two seperate calls must be made to create the animation.

Also important are the supported file formats of the provided images. The API supports a wide rang of industry standard file formats including PSD, GIF, JPEG, PNG, Targa, TIFF, XPM, ICO, SVG.


.. _length:

length
======

Length, in seconds, to constrain or expand the animation time length. So, if a default animation's time is 4 seconds, using ``length=2`` or ``length=10`` can be used to customize and shorten or extend the length of the animation. Length is applied on top of - but still respecing the relative values of - the ``blocks`` argument. Think of of the  ``length`` argument as stretching or shrinking any explicitly defined or default values of the block timing. Default value of ``length`` is specific to each animation, and can be derived from the last value of the default ``blocks`` value in ``/anims-json``.


.. _mp4:

mp4
---

Create mp4 file. Default=True


.. _msg:

msg
---

The message to be encoded into the code. Default = 'https://acme.codes' ``https://api.acme.codes/new?msg=GreetingsCustomer!``


.. _multiSampleEnable:

multiSampleEnable
-----------------

Also known in the industry as anti-aliasing, this setting improves the edge smoothness for high contrast borders that are at an angle. The 'jaggies', or staircase-like outline of simple renderings of angled edges are smoothed by sampling (measuring / calculating) multiple times the expected tonal within each pixel. Though this can slow down frame creation time, today's hardward GPU powered rendering (including ACME's default renderer), any slowdown is negligible per frame, but can add up to measurable amounts when multiplied over many frames to be rendered in an animation. Default is on.


.. _multiSampleCount:

multiSampleCount
----------------

If ``multiSampleEnable`` is on, this setting controls the number of additional samples to be made per pixel. Default is 32, the highest available. 


.. _motionBlurEnable:

motionBlurEnable
----------------

Motion blur is one of the corenerstones of quality animations; if an object is moving quickly within a single frame, it needs to look blurry with the motion as would be expected by any image capturing device. Without motion blur, animations or video have an unnatural 'crisp', or 'sharp' feel. And, like most quality improving features, slows down creation time substantially. Some cusomters prefer the crisp feel, so this setting allows for control of motion blur. Default is ``motionBlurEnable=True``, though some animations default to disabling it without an explicit override.


.. _motionBlurSampleCount:

motionBlurSampleCount
---------------------


This controls the number of samples taking for applying motion blur per frame. Default is ``motionBlurSampleCount=32``


.. _motionBlurShutterOpenFraction:

motionBlurShutterOpenFraction
-----------------------------


This controls the fraction of a frame that the renderer's virtual camera shutter is open. ``0`` = shutter is never open, while ``1`` = shutter is open the entire frame. Default is ``motionBlurShutterOpenFraction=0.2``


.. _partner:

partner
-------

Client identifier. Default = 'demo' |br| Example: ``https://api.acme.codes/new?partner=RetainedAcmeClient``


.. _pictureFrame:

pictureFrame
------------

For animations combining both a scannable code and a provided image, ``pictureFrame`` allows control over the scaling of the image or the code to be within the confines of the other. Specifically, if ``pictureFrame=code``, then the image is scaled in the animation to be within the boundaries of the code. If ``pictureFrame=image``, the code is scaled in the animation to be within the boundaries of the image. Default: ``pictureFrame=code``.


.. _pixelColor:

pixelColor
----------

The color of the base code tiles in hex. Default = ``'000000'`` (Black). Multiple hex color values can be supplied separated by commas for multi color options. Red pixel example: ``https://api.acme.codes/new?pixelColor=FF0000``



.. _pixelType:

pixelType
---------

Shape of the pixels (or "tiles") to use in QR codes. Valid set: ['square', 'circle'] Default = square. ``https://api.acme.codes/new?pixelType=circle&xres=400&yres=400``

Result:

.. image:: ./_static/ACME_Circle.png



.. _random_seed:

random_seed
-----------

Many animations available to clients contain certain randomized elements in the final animations. Explicitly setting randomSeed allows for these randomized elements to be consistent for the client for any given code. This argument also allows for consistent results in our automated test systems. ``https://api.acme.codes/new?random_seed=5``


.. _remoteIp:

remoteIp
--------

Intermediary front-end web pages, apps, or automated API's can send (and are sometimes required to send) the IP address of the remote client through this argument. ``https://api.acme.codes/new?remoteIp=123.456.789.1``


.. _stencil:

stencil
-------

Stencil option; rather than create a positive pattern of dark tiles on a **white background** to form the code, create the negative pattern of white tiles against a **transparent background** to form the code (complete with white border frame), `like a stencil <https://en.wikipedia.org/wiki/Stencil>`_ . This allows for a client to use the resulting animation as an overlay to a custom darker image, animation, or video. |br| |br| Care must be taken to ensure the code is still scannable in these conditions; since final scannability is only determinable on the client side, scannability with this option is fully the responsibility of the client. Also, unless and until the stencil version of the animated code is actually on top of a dark background, the initial delivery will be functionally invisible when viewed against the white default of browser backgrounds. Default = false |br| Example: ``https://api.acme.codes/new?stencil=true``


.. _transparentBackground:

transparentBackground
---------------------

Removes the background plane and allows for full transparency. Note transparency is only supported in gif file formats. This argument is used in conjunction with the ``stencil`` argument, in some cases automatically.


.. _transpTriggerValue:

transpTriggerValue
------------------


For animations supporting tile creation limited as a function of transparency in the image, this argument defines the value considered to be transparent. Default value is ``0``.


.. _xres:

xres
----


X Resolution, or Pixel Width, of the generated animation. Note if this value is not in harmony with yres, cropping can occur in the final product. Default = ``150`` ``https://api.acme.codes/new?xres=400``

.. _yres:

yres
----


Y Resolution, or Pixel Height, of the generated animation. Note if this value is not in harmony with xres, cropping can occur in the final product. Default = ``150`` ``https://api.acme.codes/new?yres=400``

