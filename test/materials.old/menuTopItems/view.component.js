{% import SPICES('angular') as NG %}

{% call NG.JSMAIN('menuTopItems', ['libCore']) %}
    self.menu_top_title = "Home";
    libCore.getMsg(function(event, type, value) {
        if(type == "menu_top_obj") {
            var menu_top = value;
            self.menu_top_title = menu_top.title;
	    self.menu_top_list = menu_top.list;
	}
    });

    self.click_fn = function(click_parm) {
	    console.log(click_parm);
	    alert(click_parm);
    };
{% endcall %}
