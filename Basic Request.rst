Basic Request
-------------

The minimal request sequence:

1. POST a request to ACME service, capture JSON **Order Number** response.
2. GET the the product (or any other information) by referencing the **Order Number**. 


For example, a requesting service could:
::

    POST: http://service.acme.codes/new?msg=GreetingsCustomer!


ACME service would return JSON:
::

    {orderNumber: 3284729}
    
Now the requesting servcice could retrieve the final product:

::

    GET: http://service.acme.codes/orders/3284729/gif


ACME service would then return a gif file:

.. image:: http://66.214.238.230/acmePivot


