# acme.codes: ReST API

## Introduction

These pages describe the ReST API call sequences for requesting an animated code online.

The service is provided by [Animated Codes Made Easy LLC](http://www.acme.codes), or 'ACME'. 

ACME provides near real time creation of customized animations of any scannable code, including QR codes. 

The API described in this documentation is available at [service.acme.codes](http://service.acme.codes) and [api.acme.codes](http://api.acme.codes)

The example workflows described in this documentation will function for anyone, but the encoded messages will be prefixed to ACME's website in a way that limits commercial use but still demonstrates ACME's real time encoding ability. To encode messages without this prefixed demonstration restriction, a business agreement with ACME must first be paid for.

The majority of API calls made available here can be experimented with by anyone with a browser. Simply try the links directly, or copy, edit, and paste them to create your own test codes.

Please contact sales@acme.codes if you are interested in purchasing bulk quantity near real time animated codes or QR codes through ACME's API.

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
3. (Optional) GET the **first frame** (or any frame, with reasonable patience) by referencing the **Order Number**. Then, when the progress is = 100%:
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

***

# Resources & Resource Args

## /anims-html

/anims-html returns a human readable web page flat listing of the available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource.

<a href="http://service.acme.codes/anims-html">http://service.acme.codes/anims-html</a>

## /anims-json

/anims-json returns a machine readable JSON string hierarchy definition of available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource. Additional information is also supplied per animation.

<a href="http://service.acme.codes/anims-json">http://service.acme.codes/anims-json</a>

## /new

/new returns a JSON string containing the **Order Number** to be used for all subsequent queries and updates to the animation request. Example:

    GET: http://service.acme.codes/new?msg=HelloQrScannersOfTheWorld!
    
Example return value:

    {"orderNumber": "1444720642_NLGEDCVP"}

<table>
    <tr>
        <td>Arg:</td>
        <td width=20px></td>
        <td>Description / Example:</td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>anim</td>
        <td></td>
        <td>The animation to be applied to the code. Default = 'spinning_90_oscillate'</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?anim=tumbling_360_walk">http://service.acme.codes/new?anim=tumbling_360_walk</a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>msg</td>
        <td></td>
        <td>The message to be encoded into the code. Default = 'http://acme.codes'</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?msg=GreetingsCustomer!">http://service.acme.codes/new?msg=GreetingsCustomer!</a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>partner</td>
        <td></td>
        <td>Client identifier. Default = 'demo'</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?partner=RetainedAcmeClient">http://service.acme.codes/new?partner=RetainedAcmeClient</a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>stencil</td>
        <td></td>
        <td>Stencil option. Rather than create a positive pattern of dark tiles on a white background to form the code, create the negative pattern of white tiles against a transparent background to form the code (complete with white border frame), like a <a href="https://en.wikipedia.org/wiki/Stencil">stencil</a>. This allows for a client to use the resulting animation as an overlay to a custom darker image. Care must be taken to ensure the code is still scannable in these conditions; since final scanability is only determinable on the client side, scannability with this option is fully the responsibility of the client. Also, unless and until the stencil version of the animated code is actually on top of a dark background, the initial delivery will be functionally invisible when viewed against the white default of browser backgrounds. Default = false</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?stencil=true">http://service.acme.codes/new?stencil=true</a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>xres</td>
        <td></td>
        <td>X Resolution, or Pixel Width, of the generated animation. Note if this value is not in harmony with yres, cropping can occur in the final product. Default = 100</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?xres=400">http://service.acme.codes/new?xres=400</a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>yres</td>
        <td></td>
        <td>Y Resolution, or Pixel Height, of the generated animation.  Note if this value is not in harmony with xres, cropping can occur in the final product. Default = 100 </td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="http://service.acme.codes/new?yres=400">http://service.acme.codes/new?yres=400</a></td>
    </tr>
</table>

## /orders/**[#]**/gif

No arguments. This resource returns completed full animated gif binary stream. There is a high variability of time to completion as driven by animation complexity, including times that may exceed the timeout period of some browsers. It is therefore recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100 request the gif. Example URL:

    http://service.acme.codes/orders/1444979323_ODFAUQSE/gif

## /orders/**[#]**/progress

No arguments. This resource returns a JSON string containing a 'progress' key:value pair. The value of progress is always an integer in the range [0-100]. Examples:

     http://service.acme.codes/orders/1444979323_ODFAUQSE/gif
     
 Example return values:
    
    {"progress": 0}
    {"progress": 15}
    {"progress": 100}

## /orders/**[#]**/frames/**[#]**

No arguments. This resource returns a single frame gif corresponding to the frame number of the animation. Example URL:

    http://service.acme.codes/orders/1444979323_ODFAUQSE/frames/33
