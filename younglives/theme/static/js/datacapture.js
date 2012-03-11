jQuery(function($){

    // After deletes we need to redirect to the target page.
    function redirectbasehref(el, responseText) {
        var mo = responseText.match(/<base href="(.+?)"/i);
        if (mo.length === 2) {
            return mo[1];
        }
        return location;
    }

    // capture data form
    $('a.capturePopup').prepOverlay(
        {
            subtype: 'ajax',
            width: '440px',
            filter: common_content_filter,
            formselector: 'form',
            noform: function(el) {return noformerrorshow(el, 'redirect');},
            redirect: redirectbasehref
        }
    );

});
