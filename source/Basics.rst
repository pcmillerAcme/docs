
.. |br| raw:: html

   <br />

Basics
######

There are two call sequences: the Animated QR code sequence and the Standard QR code sequence.

Animated Sequence
"""""""""""""""""

To generate an animated QR code, the API call sequence is:

=====  ==================  ==================================================
1.     /new                Initiate QR code creation with optional parameters
2.     /order/#/progress   Repeat progress check until animation is completed
3.     /order/#/<mp4File>  Retrieve the mp4 animation file
=====  ==================  ==================================================

Some animations take a few seconds to create, while others take many minutes. This sequence supports immediate API responses and informing clients of progress without hanging or '202 in progress` return codes.


Standard Sequence
"""""""""""""""""

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
