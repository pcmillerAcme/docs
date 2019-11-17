
.. |br| raw:: html

   <br />

Animations
##########

The web service hosted at api.acme.codes provides a variety of animations that can be applied to any code or QR code. The list of available animations is provided in human-readible (searchable) and machine readible (`JSON <https://en.wikipedia.org/wiki/JSON>`_) formats by the resources below.

.. _animation-list:

animation-list
""""""""""""""

The /animation-list page displays a human readable web page for reviewing animation thumbnails and text/tag searching available animations. Retail Coderunner pricing is also listed. Each listing is a valid request for the 'anim' argument of the '/new' resource. Note: Spaces in the animation names should be replaced with underscored in api calls.

Real time example link:

`https://api.acme.codes/animation-list <https://api.acme.codes/animation-list>`_

..  _anims-json:

anims-json
""""""""""

The /anims-json resource returns a machine readable JSON-formatted response flat dictionary of available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource. Additional information is also supplied per animation.

.. code-block:: javascript

    {
        "Cube": {
        "blocks": [
            [
                0, 
                2
            ], 
            [
                2, 
                4
            ], 
            [
                4, 
                6
            ], 
            [
                6, 
                8
            ]
        ], 
        "fast_slow_fast": false, 
        "length": null, 
        "price": 20.0, 
        "slow_fast_slow": false, 
        "tags": [
            "tiles", 
            "qrcode", 
            "rotate", 
            "image", 
            "2d", 
            "cube"
        ],
	...
    }

Real time example link:

`https://api.acme.cdes/anims-json <https://api.acme.codes/anims-json>`_

anims-json can return a list limited to animations with matching tags. Here is a call for animations that support taking an input image:
::

/anims-json?tags=image

Here is a call for only animations that take an input image and are spinning animations:
::

/anims-json?tags=image,spin 

Real time example link:

`https://api.acme.codes/anims-json?tags=image <https://api.acme.codes/anims-json?tags=image>`_

