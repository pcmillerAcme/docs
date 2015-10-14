# service.acme.codes: ReST API

## Introduction

These pages describe the ReST API call sequences for requesting an animated code online.

The service is provided by [Animated Codes Made Easy LLC](http://www.acme.codes), or 'ACME'. 

ACME provides near real time creation of customized animations of any scannable code, including QR codes. 

The API described in this documentation is available at [service.acme.codes](http://service.acme.codes) and [api.acme.codes](http://api.acme.codes)

Please note that access to this service requires a contract with ACME, please contact sales@acme.codes

'QR Code' is a registered trademark of DENSO WAVE INCORPORATED

## Basic Request

The minimal request sequence:

1. GET a new order number, receive JSON response containing an **Order Number**.
2. GET the product (or any other information) by referencing the **Order Number**. 

For example, a requesting service could:

    GET: http://service.acme.codes/new?msg=GreetingsCustomer!

ACME service would return JSON:

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now the client can retrieve the final product:

    GET: http://service.acme.codes/orders/1444720642_NLGEDCVP/gif

ACME service would then return a gif file:

![Acme Animated gif](http://service.acme.codes/acmePivot 'Animated Code')

## Standard Request

Since ACME animation generation times can vary significantly based on animation complexity (sub-second to > 2 minutes), the more standard transaction sequence provides more options to the calling application. 

1. GET a new order, receive JSON response containing an **Order Number**.
2. (Optional) Iteratively GET the **progress** of the product generation by referencing the **Order Number**, capture the JSON progress information. This can be used to feed into a progress bar feedback window for the client. Then, when the progress is > 5%:
3. (Optional) GET the first frame (or any frame, with reasonable patience) by referencing the **Order Number**. Then, when the progress is = 100%:
4. GET the final product 

For example, a requesting service could:

    GET: http://service.acme.codes/new?msg=GreetingsCustomer!

ACME service would return JSON:

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now the requesting service can retrieve the progress of the order:

    GET: http://service.acme.codes/orders/1444720642_NLGEDCVP/progress

ACME service would return JSON:

    {"progress": 12}
    
Now the requesting service can retrieve the first frame of an order before the completed animation is available:
    
    GET: http://service.acme.codes/orders/1444720642_NLGEDCVP/frames/1

ACME service would return a non-animated single frame gif file:

!['Non-animated Code'](http://service.acme.codes/acmePivotSingleFrame 'Single Frame')
    
When reported progress is 100%, the requesting service can retrieve the final animated product, in this case a GIF file of an animation:

    GET: http://service.acme.codes/orders/1444720642_NLGEDCVP/gif

ACME service would return an animated gif file:

!['Animated Code'](http://service.acme.codes/acmePivot 'Animated Code')



