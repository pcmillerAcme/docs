
.. |br| raw:: html

   <br />

Basics
######

Examples
""""""""

Here's the simplest call to our service to generate a **standard** QR code (not one of our higher end animated codes):

`https://api.acme.codes/new?msg=myAwesomeLittleStore.com/purchasePages/redBicycle&format=png <https://api.acme.codes/new?msg=myAwesomeLittleStore.com/purchasePages/redBicycle&format=png>`_

The above call defaults to returning a low resolution image containing the scannable QR code. Here's a call with parameters to request a code with higher resolution, and some custom colors in the registration eyes:

`https://api.acme.codes/new?msg=myAwesomeLittleStore.com/purchasePages/redBicycle&format=png&xres=800&yres=800&eyeColor=0000aa <https://api.acme.codes/new?msg=myAwesomeLittleStore.com/purchasePages/redBicycle&format=png&xres=800&yres=800&eyeColor=0000aa>`_

Notice full anti aliased quality, and that these calls are GET's and easily can work in your browser directly.

These standard QR codes are created in very little time, so and actual image is directly returned. Animated QR codes require much more time to create than is acceptable for an internet query/response, so the call sequence is a few more steps to avoid unacceptably long response times.

Call Sequences
""""""""""""""

There are two call sequences: the Animated QR code sequence and the Standard QR code sequence demonstrated above.

Animated QR codes
+++++++++++++++++


To generate an animated QR code, the API call sequence is:

=====  ==================  ==================================================
1.     /new                Initiate QR code creation with optional parameters, receive order number and location where final animation will be published
2.     /order/#/progress   Repeat progress check until animation is completed
3.     /order/#/<mp4File>  Retrieve the mp4 animation file
=====  ==================  ==================================================

Some animations take a few seconds to create, while others take many minutes. This sequence supports immediate API responses and informing clients of progress without hanging or having to write code to support '202 - in progress` return codes.

Standard QR codes
+++++++++++++++++

To generate a standard QR code, the API call sequence is:

=====  =====  ======================================================================
1.     /new   Initiate creation with desired parameters, receive png image response
=====  =====  ======================================================================

Standard QR code creation time is less than a second, so this sequence supports direct return of requested content.

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
|br|
|br|
