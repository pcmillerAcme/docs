
.. |br| raw:: html

   <br />

new
###

``/new`` starts the creation process of a new animated code and returns a response containing the **Order Number** to be used for all subsequent queries about and updates to the started animation. Example:
::

    GET: https://api.acme.codes/new?msg=HelloQrScannersOfTheWorld!
    
Example return value:
::

    {"orderNumber": "1444720642_NLGEDCVP"}

Below are the optional arguments when calling the ``/new`` resource. 

.. list-table:: Arguments for /new:
   :widths: auto
   :header-rows: 1

   * - Arg:
     - Description/Examples/Default Values:
   * - ``apiKey``
     - For users with temporary "try-it-out" or fully paid subscriptions wanting unlocked codes rather than the default free Locked Demonstration codes, a valid `API Key <https://en.wikipedia.org/wiki/Application_programming_interface_key>`_ must be subitted in this argument for all newly created codes. Contact sales@acme.codes to be given a temporary "try-it-out" API key or purchase a permanent API Key for completely unlocked codes.
   * - ``anim``
     - The animation to be applied to the code. See anims-json and animation-list resources for a complete list of valid values for anim. Default = 'Exchange'. ``https://api.acme.codes/new?anim=Exchange``
   * - ``applyFrameNumbers``
     - This setting allows for diagnostic per frame overlays of a frame hand and frame count to ensure altered animations are rendered correctly for expected total and block times.
   * - ``bgpColor``
     - Background Plate Color. Background color. Default = 'FFFFFF' (White). Multiple hex color values can be supplied separated by commas for multi color options. Green background example: ``https://api.acme.codes/new?bgpColor=00FF00``
   * - ``blocks``
     - One of ACME's most popular arguments for refining generated animations to preference. For any given animation, ``blocks=`` allows for arbitrary timing of the blocked portions of the animation. Each animation has default block timing; for example, the block timing of a code to image and back animation would be 2 seconds of the code, two seconds animating to the image, 2 second hold of the image, and finally 2 second animation back to the code. (Note: the last two seconds are so 'minus the last frame' in order to support smooth looping transitions.) ``blocks=`` allows for overriding of any animation's default block timing. So, say an animation is wanted that instead animates the code display for one second, then animates to the image in 5 seconds, then holds the image for 2 seconds, then animates back to the code in 3 seconds. With the block argument comma separated values representing the absolute times for blocks to start and stop, the needed argument would be ``blocks=0-1,1-6,6-8,8-11``. All values are in seconds, not frames. Float values fully supported: 0-2.44,2.44-6 is ok. It is important to note some animations have only one block (Spin for example), while others usually have 4, and still others have overlapping animation block times. Default block values are given with the ``/anims-json`` resource. ``blocks`` values are also subjected to the ``length`` argument. 
   * - ``chromaKeys``
     - Certain animations support the notion of pixel tiles not being present for the portion of the animation where only the image is displayed. This field supports multiple chroma keys to be used. Default value is None. 
   * - ``chromaRange``
     - Supports the breadth of color range to be used in chromaKeys arg. Default value is 5.
   * - ``fbx``
     - Create fbx file. Default=True
   * - ``fitFactor``
     - This controls the fraction of the framed code which fills the camera view. If set to a low values close to 0, the code will be very small in the frame, while if set to 1, the code will touch the borders. Note that some animations will alter the default fitFactor to ensure all of the animation is properly viewable, but explicit setting of fitFactor will override animation influences. Default is ``fitFactor=0.9``
   * - ``format``
     - The format of the return value. Default = 'JSON'. Usually format is left undeclared in order inherit the default 'JSON'. However, as a convenience option for humans directly accessing the API, the 'html' option exists. If format set to 'html', /new will return an html web page containing a clickable link to the final gif product. This can be useful for interactive demonstration, testing, and verification of the API directly without relying on a more complex GUI front end. Without the 'html' option and without a front end, the user is left to parse raw JSON and manually assemble the URL, which is not fun for anything but scripts. ``https://api.acme.codes/new?format=JSON`` (Default) ``https://api.acme.codes/new?format=html``
   * - ``fps``
     - Another one of ACME's popular settings; Frames Per Second. All animations are defined in terms of time, so any animation can be rendered at any industry standard FPS while maintaining the same animation timing. The higher the FPS, the higher the 'look and feel' of the smoothness of the animation. At the time of this document's writing, the ACME default is 15FPS, but this will soon shift to 30FPS. Control over FPS can have significant effect over final animation file size, in particular gif files.
   * - ``frameNumber``
     - Limits the generation of the animation to one specific frame. Use of this is discouraged for normal use. Normal access of individual frames should be through the /orders/[Order#]/frames/[n] resource. However, if the user is creating test suites or similar use cases where it is known in advance that only one frame is needed, it can be helpful to use this argument to optimize test execution time by limiting generated output to just one frame.
   * - ``frames``
     - Create rendered frames file. Default=True. Required for most usage. By turning off, delivery times for fbx files is reduced, which is helpful for people wanting only digital 3d files.
   * - ``gif``
     - Create gif file. Default=True. Note gif generation requires the longest processing time of all other creation processes.
   * - ``imageRotation``
     - The rotation to be applied to a supplied image URL ``https://api.acme.codes/new?anim=Spin&img1=https://www.acme.ink/demos/acmecodes/tImg/img1.png&imageRotation=90``
   * - ``img1``
     - The image URL to be applied within the animation, if supported by the selected animation. ``https://api.acme.codes/new?anim=Spin&img1=https://www.acme.ink/demos/acmecodes/tImg/img1.png``
   * - ``length``
     - Length, in seconds, to constrain or expand the animation time length. So, if a default animation's time is 4 seconds, using ``length=2`` or ``length=10`` can be used to customize and shorten or extend the length of the animation. Length is applied on top of - but still respecing the relative values of - the ``blocks`` argument. Think of of the  ``length`` argument as stretching or shrinking any explicitly defined or default values of the block timing. Default value of ``length`` is specific to each animation, and can be derived from the last value of the default ``blocks`` value in ``/anims-json``.
   * - ``mp4``
     - Create mp4 file. Default=True
   * - ``msg``
     - The message to be encoded into the code. Default = 'https://acme.codes' ``https://api.acme.codes/new?msg=GreetingsCustomer!``
   * - ``multiSampleEnable``
     - Also known in the industry as anti-aliasing, this setting improves the edge smoothness for high contrast borders that are at an angle. The 'jaggies', or staircase-like outline of simple renderings of angled edges are smoothed by sampling (measuring / calculating) multiple times the expected tonal within each pixel. Though this can slow down frame creation time, today's hardward GPU powered rendering (including ACME's default renderer), any slowdown is negligible per frame, but can add up to measurable amounts when multiplied over many frames to be rendered in an animation. Default is on.
   * - ``multiSampleCount``
     - If ``multiSampleEnable`` is on, this setting controls the number of additional samples to be made per pixel. Default is 32, the highest available. 
   * - ``motionBlurEnable``
     - Motion blur is one of the corenerstones of quality animations; if an object is moving quickly within a single frame, it needs to look blurry with the motion as would be expected by any image capturing device. Without motion blur, animations or video have an unnatural 'crisp', or 'sharp' feel. And, like most quality improving features, slows down creation time substantially. Some cusomters prefer the crisp feel, so this setting allows for control of motion blur. Default is ``motionBlurEnable=True``, though some animations default to disabling it without an explicit override.
   * - ``motionBlurSampleCount``
     - This controls the number of samples taking for applying motion blur per frame. Default is ``motionBlurSampleCount=32``
   * - ``motionBlurShutterOpenFraction``
     - This controls the fraction of a frame that the renderer's virtual camera shutter is open. 0=shutter is never open, while 1=shutter is open the entire frame. Default is ``motionBlurShutterOpenFraction=0.2``
   * - ``partner``
     - Client identifier. Default = 'demo' ``https://api.acme.codes/new?partner=RetainedAcmeClient``
   * - ``pictureFrame``
     - For animations combining both a scannable code and a provided image, ``pictureFrame`` allows control over the scaling of the image or the code to be within the confines of the other. Specifically, if ``pictureFrame=code``, then the image is scaled in the animation to be within the boundaries of the code. If ``pictureFrame=image``, the code is scaled in the animation to be within the boundaries of the image. Default: ``pictureFrame=code``.
   * - ``pixelColor``
     - The color of the base code tiles in hex. Default = '000000' (Black). Multiple hex color values can be supplied separated by commas for multi color options. Red pixel example: ``https://api.acme.codes/new?pixelColor=FF0000``
   * - ``random_seed``
     - Many animations available to clients contain certain randomized elements in the final animations. Explicitly setting randomSeed allows for these randomized elements to be consistent for the client for any given code. This argument also allows for consistent results in our automated test systems. ``https://api.acme.codes/new?random_seed=5``
   * - ``remoteIp``
     - Intermediary front-end web pages, apps, or automated API's can send (and are sometimes required to send) the IP address of the remote client through this argument. ``https://api.acme.codes/new?remoteIp=123.456.789.1``
   * - ``stencil``
     - Stencil option. Rather than create a positive pattern of dark tiles on a white background to form the code, create the negative pattern of white tiles against a transparent background to form the code (complete with white border frame), like a stencil. This allows for a client to use the resulting animation as an overlay to a custom darker image. Care must be taken to ensure the code is still scannable in these conditions; since final scannability is only determinable on the client side, scannability with this option is fully the responsibility of the client. Also, unless and until the stencil version of the animated code is actually on top of a dark background, the initial delivery will be functionally invisible when viewed against the white default of browser backgrounds. Default = false ``https://api.acme.codes/new?stencil=true``
   * - ``tileShape``
     - Shape of the tiles to use in QR codes. Valid set: ['square', 'circle'] Default = square. ``https://api.acme.codes/new?tileShape=circle&xres=400&yres=400``
   * - ``transparentBackground``
     - Removes the background plane and allows for full transparency. Note transparency is only supported in gif file formats. This argument is used in conjunction with the ``stencil`` argument, in some cases automatically.
   * - ``transpTriggerValue``
     - For animations supporting tile creation limited as a function of transparency in the image, this argument defines the value considered to be transparent. Default value is 0.
   * - ``xres``
     - X Resolution, or Pixel Width, of the generated animation. Note if this value is not in harmony with yres, cropping can occur in the final product. Default = 150 ``https://api.acme.codes/new?xres=400``
   * - ``yres``
     - Y Resolution, or Pixel Height, of the generated animation. Note if this value is not in harmony with xres, cropping can occur in the final product. Default = 150 ``https://api.acme.codes/new?yres=400``

