
.. |br| raw:: html

   <br />

    
order_image
###########

This resource is a POST target for uploading and updating the image (``img1=`` argument) *after* the order has been created. 

Two arguments must be provided to the /order_image resource: ``image_file`` and ``order``. ``image_file`` must contain the binary image, and ``order`` must contain the order number.

Overview: there are two ways to supply an image to an ACME animation:

1. At initial order creation time, by supplying a URL to an image published on the internet via the ``img1=`` argument for the ``/new`` resource, an image can be inserted into an animation right from the start. The advantage here is the image goes in 'all at once' in *one* call. The disadvantage is the image must already exist over http/https and be published on the internet before the call to ``/new`` is made. 
|br|
|br|
2. Alternatively, a different call sequnce can be used. After the intial order has been created via a call to ``/new``, a POST of an image to order_image will trigger the order animation to be refreshed after order upload is complete. The advantage is the image need never be published on the internet, while the disadvantage is that two seperate calls must be made to create the animation.

Also important are the supported file formats of the provided images. The API supports a wide rang of industry standard file formats including PSD, GIF, JPEG, PNG, Targa, TIFF, XPM, ICO, SVG.