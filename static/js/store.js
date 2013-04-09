$(function() {

    var $el; 

    $(".product-jump").tooltip({
    
        "open": function() {
        
            $el = $(this);
        
            $(this).tooltip("widget").position({
            
                "my": "center top",
                "at": "center bottom",
                "of": $el,
                "offset": "0 -26"
            
            });
        
        }
    
    });

});