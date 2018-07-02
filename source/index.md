# api.acme.codes: ReST API

## Introduction

These pages describe the ['Software as a Service' (SaaS)](https://en.wikipedia.org/wiki/Software_as_a_service) provided by [Animated Codes Made Easy LLC](http://www.acme.codes), or 'ACME'. 

ACME's service at api.acme.codes provides near real time creation of customized animations of any scannable code, including QR codes. Standard codes and QR codes (non-animated) can also be created.

If you are a software developer interested in using ACME's service, this documentation is for you. If you are not a software developer, you'll probably be happier visiting [ACME's top page](http://acme.codes). 

This documentation describes the ReST API call sequences for requesting an animated code online. 

The API described in this documentation is available at [https://api.acme.codes](https://api.acme.codes)

The example workflows described in this documentation will function for anyone; in particular non-animated codes can be generated without any payment (for free). However messages embedded into *animated* codes will be prefixed to ACME's website in a way that limits commercial use but still demonstrates ACME's real time encoding ability. All generated demonstration codes are scannable, however the embedded link will only affirm the requested test message rather than contain the original message. To encode messages into animated codes without this prefixed demonstration restriction, a subscription-based business agreement with ACME must first be paid for.

The majority of API calls made available here can be experimented with by anyone with a browser. Simply try the links directly, or copy, edit, and paste them to create your own test codes.

If you have feedback or questions on this documentation, or if you are interested in purchasing bulk quantity near real time animated codes or QR codes through ACME's API, please contact [sales@acme.codes](mailto:sales@acme.codes?subject=From%20RTD:%20Interest%20in%20ACME%20Web%20Service)

Certain design and architectural features of this service are patent pending.

'QR Code' is a registered trademark of DENSO WAVE INCORPORATED

## Basic Request

The minimal request sequence:

1. GET a new order number, receive JSON response containing an **Order Number**.
2. GET the product (or any other information) by referencing the **Order Number**. 

For example, a requesting service could:

    GET: https://api.acme.codes/new?msg=Reading%20ACME%20documentation%20is%20fun!

ACME service would return JSON:

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Now, after some time has passed, the client can retrieve the final product:

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/gif

ACME service would then return an animated gif file. Depending on creation arguments described below, a file similar to this would be returned:

![Acme Animated gif](./_static/AcmeCode_182160.gif 'Animated Code')

Note: An immediate 'gif' resource GET request to an accurate order will initially result in a '202 Accepted' response, and not a '200 OK' return code because the service has not yet completed creating the file. This response page will contain a message clarifying the reason for the temporary inability to return the requested file. The below Standard Request workflow shows how to avoid this response entirely.

## Standard Request

Since ACME animation generation times can vary significantly based on animation complexity (sub-second to > 2 minutes), the more standard transaction sequence provides more options to a client application. 

1. GET a new order, receive JSON response containing an **Order Number**.
2. (Optional) Iteratively GET the **server-side state and order progress** of the animation generation by referencing the **Order Number**, capture the JSON response containing the server-side state information. This can be used to display a real time progress bar feedback window for the client. Then, when the server side progress is > 5%:
3. (Optional) GET the **first frame** (or any frame, with reasonable correlation to the known server-side progress) by referencing the **Order Number**. This can be used to provide accurate visual feedback to the client user of the product as it is being made. Then, when the server-side progress is = 100%:
4. (Optional) GET the final product file size. This information can be used below.
5. GET the final product
6. (Optional) Measure the local file size as it is streamed in from the above call and compare it to the known full file size. This comparison can be used to accurately provide visual progress bar(s) to the client regarding file transmission.

For example, a client application could:

    GET: https://api.acme.codes/new?msg=Reading%20ACME%20documentation%20is%20fun!

ACME service would return JSON:

    {"orderNumber": "1444720642_NLGEDCVP"}
    
Optionally, now the client application can retrieve the server-side state and order progress:

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/progress

ACME service would return JSON:

    {"progress": 12, "queue": 0}
    
The client can repeatedly request the progress resource (every few seconds or so) until the "progress" key is 100, indicating that the order is complete. Also, if the "queue" value is non zero, this indicates the service resources are at their maximum capacity since a queue has formed, indicating a slowdown in the usual turnaround time. This can be communicated to the user to help explain slow or temporarily static progress values.

Optionally, now the client application can retrieve the first frame of an order before the completed animation is available:
    
    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/frames/1

ACME service would return a non-animated single frame gif file:

!['Non-animated Code'](./_static/ACME_SF_1.png 'Single Frame')
    
Optionally, when reported server-side order "progress" is 100%, the client application can request the final product file size:

    GET https://api.acme.codes/orders/1444720642_NLGEDCVP/gif-file-info

ACME service would return JSON:

    {"fileSize": 439441}

Finally, the client application can retrieve the completed animated product, in this case a GIF file of an animation:

    GET: https://api.acme.codes/orders/1444720642_NLGEDCVP/gif

ACME service would then return an animated gif file. Depending on creation arguments described below, a file similar to this would be returned:

!['Animated Code'](./_static/AcmeCode_182160.gif 'Animated Code')

Optionally, the client application can display the transmission progress of the final product as it is streamed from server to client by querying the size of the local streamed file as it arrives and comparing it to the known full file size from the above optional gif-file-info resource.

***

# Resources & Resource Args

## https://acme.codes/anims/**[anim]**/thumbnails/anim.gif

This resource returns a thumbnail-sized animated gif which can aid user's selection from a large animation list. Note thumbnails are hosted out of the acme.codes domain, not api.acme.codes. Example URL:

    https://acme.codes/anims/Spin/thumbnails/anim.gif
    
Example return value:

!['Thumbnail Animated Code'](./_static/anim.gif 'Animated thumbnail')

## https://acme.codes/anims/**[anim]**/thumbnails/image.gif

This resource returns a thumbnail-sized static gif which can aid user's selection from a large animation list. Note thumbnails are hosted out of the acme.codes domain, not api.acme.codes. Example URL:

    https://acme.codes/anims/Spin/thumbnails/image.gif
    
Example return value:

!['Thumbnail Animated Code'](./_static/image.gif 'Static thumbnail')

## /anims-html

/anims-html returns a human readable web page flat listing of the available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource.

    ACME Animations:
    ** All animations subject to copyright claims unless indicated otherwise. **
    flock_simple_circle
    flock_simple_circleCreased
    [...]
    ** All animations subject to copyright claims unless indicated otherwise. **

Real time example link:

<a href="https://api.acme.codes/anims-html">https://api.acme.codes/anims-html</a>

## /anims-json

/anims-json returns a machine readable JSON-formatted response flat dictionary of available animations. Each listing is a valid request for the 'anim' argument of the '/new' resource. Additional information is also supplied per animation.

    {"Tumbling360Pause": {"frames": 150}, "ImageToCodeTileSwap": {"frames": 24}, "WindVanesAll": {"frames": 24}, "Spin": {"frames": 150}, "CircleCreased": {"frames": 180}, "Spin_Fast": {"frames": 150}, "Circle": {"frames": 90}, "WindVanes1Breeze": {"frames": 25}, "WindVanes2Breezes": {"frames": 140},...}

Real time example link:

<a href="https://api.acme.codes/anims-json">https://api.acme.codes/anims-json</a>

anims-json can return a list limited to animations with matching tags. For example: /anims-json?tags=image or /anims-json?tags=image,spin 

<a href="https://api.acme.codes/anims-json?tags=image">https://api.acme.codes/anims-json?tags=image</a>

## /new

/new returns a JSON-formatted response containing the **Order Number** to be used for all subsequent queries and updates to the animation request. Example:

    GET: https://api.acme.codes/new?msg=HelloQrScannersOfTheWorld!
    
Example return value:

    {"orderNumber": "1444720642_NLGEDCVP"}

<table>
    <tr>
    <!--<td style="background-color: #e0e0e0; vertical-align: top;">-->
        <td>Arg:</td>
        <td width=20px></td>
        <td>Description / Example:</td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">anim</td>
        <td></td>
        <td>The animation toa be applied to the code. Setting anim to 'None' will result in an un-animated flat code being returned. See anims-json and anims-html resources for a complete list of valid values for anim. Default = 'Spin'.<br><a href="https://api.acme.codes/new?anim=Spin&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?anim=Spin</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
    <tr>
        <td>format</td>
        <td></td>
        <td>The format of the return value. Default = 'JSON'. Usually <b>format</b> is left undeclared in order inherit the default 'JSON'. However, as a convenience option for humans directly accessing the API, the 'html' option exists. If <b>format</b> set to 'html', <b>/new</b> will return an html web page containing a clickable link to the final gif product. This can be useful for interactive demonstration, testing, and verification of the API directly without relying on a more complex GUI front end. Without the 'html' option and without a front end, the user is left to parse raw JSON and manually assemble the URL, which is not fun for anything but scripts.<br><a href="https://api.acme.codes/new?format=JSON&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?format=JSON</code></a> (Default)<br>
        <a href="https://api.acme.codes/new?format=html&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?format=html</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>    
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">frameNumber</td>
        <td></td>
        <td>Limits the generation of the animation to one specific frame. Use of this is discouraged for normal use. Normal access of individual frames should be through the /orders/[Order#]/frames/[n] resource. However, if the user is creating test suites or similar use cases where it is known in advance that only one frame is needed, it can be helpful to use this argument to optimize test execution time by limiting generated output to just one frame. </td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>imageRotation</td>
        <td></td>
        <td>The rotation to be applied to a supplied image URL<br><a href="https://api.acme.codes/new?anim=Spin&img=https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png&imageRotation=90&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?anim=Spin&img=https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png&imageRotation=90</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">img</td>
        <td></td>
        <td>The image URL to be applied within the animation, if supported by the selected animation.<br><a href="https://api.acme.codes/new?anim=Spin&img=https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?anim=Spin&img=https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>msg</td>
        <td></td>
        <td>The message to be encoded into the code. Default = 'https://acme.codes'<br><a href="https://api.acme.codes/new?msg=GreetingsCustomer!&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?msg=GreetingsCustomer!</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">bgpColor</td>
        <td></td>
        <td>Background Plate Color. Background color. Default = 'FFFFFF' (White). Multiple hex color values can be supplied separated by commas for multi color options. <br>Green background example: <a href="https://api.acme.codes/new?bgpColor=00FF00&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?bgpColor=00FF00</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>pixelColor</td>
        <td></td>
        <td>The color of the base code tiles in hex. Default = '000000' (Black). Multiple hex color values can be supplied separated by commas for multi color options. <br>Red pixel example: <a href="https://api.acme.codes/new?pixelColor=FF0000&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?pixelColor=FF0000</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">partner</td>
        <td></td>
        <td>Client identifier. Default = 'demo'</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="https://api.acme.codes/new?partner=RetainedAcmeClient&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?partner=RetainedAcmeClient</code></a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>remoteIp</td>
        <td></td>
        <td>Intermediary front-end web pages, apps, or automated API's can send (and are sometimes required to send) the IP address of the remote client through this argument.<br><a href="https://api.acme.codes/new?&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?remoteIp=123.456.789.1</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">random_seed</td>
        <td></td>
        <td>Many animations available to clients contain certain randomized elements in the final animations. Explicitly setting randomSeed allows for these randomized elements to be consistent for the client for any given code. This argument also allows for consistent results in our automated test systems.<br><a href="https://api.acme.codes/new?random_seed=5&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?random_seed=5</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>stencil</td>
        <td></td>
        <td>Stencil option. Rather than create a positive pattern of dark tiles on a white background to form the code, create the negative pattern of white tiles against a transparent background to form the code (complete with white border frame), like a <a href="https://en.wikipedia.org/wiki/Stencil">stencil</a>. This allows for a client to use the resulting animation as an overlay to a custom darker image. Care must be taken to ensure the code is still scannable in these conditions; since final scannability is only determinable on the client side, scannability with this option is fully the responsibility of the client. Also, unless and until the stencil version of the animated code is actually on top of a dark background, the initial delivery will be functionally invisible when viewed against the white default of browser backgrounds. Default = false</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="https://api.acme.codes/new?stencil=true&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?stencil=true</code></a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">tileShape</td>
        <td></td>
        <td>Shape of the tiles to use in QR codes. Valid set: ['square', 'circle'] Default = square.<br><a href="https://api.acme.codes/new?tileShape=circle&xres=400&yres=400&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?tileShape=circle&xres=400&yres=400</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td>xres</td>
        <td></td>
        <td>X Resolution, or Pixel Width, of the generated animation. Note if this value is not in harmony with yres, cropping can occur in the final product. Default = 150</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td><a href="https://api.acme.codes/new?xres=400&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?xres=400</code></a></td>
    </tr>
    <tr height=20px>
    </tr>
    <tr>
        <td style="background-color: #f0f0f0;">yres</td>
        <td></td>
        <td>Y Resolution, or Pixel Height, of the generated animation.  Note if this value is not in harmony with xres, cropping can occur in the final product. Default = 150<br><a href="https://api.acme.codes/new?yres=400&remoteIp=readthedocs.io"><code>https://api.acme.codes/new?yres=400</code></a></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

## /orders/**[#]**/fbx

This resource returns the complete animated [FBX](https://en.wikipedia.org/wiki/FBX) binary stream. There is a high variability of time to completion as driven by animation complexity, including times that may exceed the timeout period of some browsers. It is therefore recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100, then request the fbx file. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx

## /orders/**[#]**/fbx/**[TS]**

This resource is an alias to /orders/**[#]**/fbx. This is a convenience resource which is helpful in some programmatic circumstances to bypass the caching mechanism of client-side frameworks. By putting any timestamp (TS) value after fbx, the client code is forced - through this resource alias - to always get the latest /orders/**[#]**/fbx. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx/1464382911

## /orders/**[#]**/fbx-file-info

This resource returns a JSON-formatted response containing a 'fileSize' key:value pair. The value of fileSize is zero until the file creation is completed, at which point it is permanently the file size of the finished fbx animation file. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/fbx-file-info
    
Example return value:

    {"fileSize":  1124656}

## /orders/**[#]**/frames/**[#]**

This resource returns a single frame gif corresponding to the frame number of the animation. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/frames/33

## /orders/**[#]**/gif

This resource returns the complete animated gif binary stream. There is a high variability of time to completion as driven by animation complexity, including times that may exceed the timeout period of some browsers. It is therefore recommended to query orders/**[OrderNumber]**/progress resource first, and after progress has reached a value of 100 request the gif. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/gif

## /orders/**[#]**/gif/**[TS]**

This resource is an alias to /orders/**[#]**/gif. This is a convenience resource which is helpful in some programmatic circumstances to bypass the caching mechanism of client-side frameworks. By putting any timestamp (TS) value after gif, the client code is forced - through this resource alias - to always get the latest /orders/**[#]**/gif.  Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/gif/1464382911

## /orders/**[#]**/gif-file

This resource is another alias for the /gif resource, but wraps the return response with 'Content-Disposition' as 'attachment', allowing browsers to treat the returned gif as an explicit file to be saved, rather than display it as an inline image on the displayed web page. When this resource is called, client browsers will download the gif file automatically to a specific download directory, or pop-up a browser to allow the user to specify the file name and location on their system. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/gif-file

## /orders/**[#]**/gif-file-info

This resource returns a JSON-formatted response containing a 'fileSize' key:value pair. The value of fileSize is zero until the file creation is completed, at which point it is permanently the file size of the final finished gif animation file. Example URL:

    https://api.acme.codes/orders/1444979323_ODFAUQSE/gif-file-info
    
Example return value:

    {"fileSize": 439441}

## /orders/**[#]**/progress

This resource returns a JSON-formatted response containing information key:value pairs about the specified order since the most recent edit. Pairs include "progress", which returns an integer in the range [0-100], and represents the percentage of completion for the most recently requested animated code. This progress information is useful to communicate to end users how much longer they will have to wait until their order update is completed. Also, "queue" returns the current size of the backup request queue. If queue is non-zero, the system is at maximum capacity and progress speed will be delayed. If queue is non-zero, most front end client systems communicate this information to users to help assure them as to why processing is slower than usual. Example URL:

     https://api.acme.codes/orders/1444979323_ODFAUQSE/progress
     
 Example return values:
    
    {"queue": 10, "progress": 0}
    {"queue": 0, "progress": 0}
    {"queue": 0, "progress": 15}
    {"queue": 0, "progress": 100}

## /price-list

This resource returns standard html web page with a sortable, searchable, and filterable price list of animations.

Real time example link:

<a href="https://api.acme.codes/price-list">https://api.acme.codes/price-list</a>

## /version

This resource returns a JSON-formatted response containing software build and date information about this service. 

    {"buildNumber": 1747, "buildTime": "Tue Oct 20 22:14:11 2015", "version": "0.5", "branch": "master"}

Real time example link:

<a href="https://api.acme.codes/version">https://api.acme.codes/version</a>
