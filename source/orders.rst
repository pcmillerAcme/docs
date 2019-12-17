
.. |br| raw:: html

   <br />

orders
######

``/orders/<*>``

This resource is the root endpoint for all created orders. After any call to ``new`` - which returns an order number - the order animation files can be found in ``/orders/<order_number>/<desired_filetype>`` 
|br|
|br|
**It is important to remember that all content in /orders is only available temporarily.**
|br|
|br|
Subscribers wanting to keep their animation files must do at least one of two things:

1. Download and manage their files as they wish as they are created; older content in the ``/orders`` resource is scrubbed daily for storage re-use. ACME only supports content availability in ``/orders`` for 3 days after creation.

2. Optionally, ACME customers can pay ACME additionally for CDN subscription. ACME provides for automated uploading of generated content to our CDN provider. See the CDN section of this documentaion for details.

Example URLs:
::

    https://api.acme.codes/orders/1444979323_ODFAUQSE/mp4
    https://api.acme.codes/orders/1444979323_ODFAUQSE/gif
    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx
    https://api.acme.codes/orders/1444979323_ODFAUQSE/frames/3
    https://api.acme.codes/orders/1444979323_ODFAUQSE/zip (Limited availability)
    
