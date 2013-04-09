$(function() {

    var $el;

    $(".zoomer").live("click", function(e) {
                
        $el = $(this);
    
        $("<img />", {
        
            "src": $el.attr("href"),
            "class": "larger"
        
        }).load(function(e) {
	
		e.preventDefault();
        
            $(this)
                .appendTo("body")
                .width($el.find(".orig").width())
                .position({
                    "of": $el.find(".orig"),
        			"my": "center center",
        			"at": "center center",
        			"offset": "0 -9"
			     })
                .animate({
                    width: 450,
                    }, {
                        duration: 1000,
                        easing: "easeOutQuad",
                        step: function(i) {
                            $(this).position({
                                "of": $el.find(".orig"),
                    			"my": "center center",
                    			"at": "center center",
                    			"offset": "0 -9"
            			     })
                        }
                    
                    }
                )
        })
        return false;
    });

	$(".larger").live("click", function() {
	
		$(this).fadeOut(400, function() {
			
			$(this).remove();
			
		})
		
	});
});