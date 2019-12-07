
.. |br| raw:: html

   <br />

image
#####

``/orders/<order number>/image``

This resource is a Restul POST target for a remote client to upload an image to an existing order. After the image is receieved by api.acme.codes, the order is automatically refreshed and begins processing anew as if the order was just created. |br|
|br|
After posting to the ``image`` resource, it is recommended to check the ``progress`` resource iteratively for completion, since requests for mp4s immediately following a post to ``image`` will return `202 responses <https://restfulapi.net/http-status-202-accepted>`_  as the animation process takes time to complete.
|br|
|br|
Reminder: this ``image`` resource is one of two ways to create an animation with a custom image. The two patterns of animation creation with custom images are:
 
1. Ensure the image is published on the web, make a call to the ``/new`` resource with the ``img1`` argument set to the web address of the published image.
2. Create the order with a call to ``/new``, directly upload the image to the order after the order has been created.

|br|
The advantage of the first pattern is that only one call to ``new`` must be made. The disadvantage of the first pattern is that the image must be published via http/https on the internet. 
|br|
|br|
The advantage of the second pattern is that the custom image does not need to be published on the internet in advance of the call to ``/new``. The disadvantage is that two calls to the api must be made to create the desired animation. 
|br|
|br|

Example URL:
::

     https://api.acme.codes/orders/1444979323_ODFAUQSE/image

     
Example return values:
::
    
    (None, but <200> OK status code)

See the SDK section of this documentation for detailed working examples of POSTing to the ``image`` resource.

