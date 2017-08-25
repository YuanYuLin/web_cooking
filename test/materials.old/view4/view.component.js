{% import SPICES('angular') as NG %}
{% call NG.JSMAIN('view4', ['libCore']) %}

    libCore.setMsg("menu_top_obj", {"title":"View4", "list":[{"title":"V4-1"},{"title":"V4-2"}]});
    libCore.doHttpGet('api/system.json', function(is_successed, response){
        if(is_successed) {
            self.data_system = response.data;
	} else {
            console.log("Failed to get 'api/system.json'");
	}
    });

    libCore.doHttpGet('api/memory.json', function(is_successed, response){
        if(is_successed) {
            self.data_memory = response.data;
	} else {
            console.log("Failed to get 'api/memory.json'");
	}
    });

{% endcall %}
