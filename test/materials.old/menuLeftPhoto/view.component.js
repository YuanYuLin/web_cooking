{% import SPICES('angular') as NG %}
{% call NG.JSMAIN('menuLeftPhoto', ['libCore']) %}
    self.user_status = "GUEST";
    libCore.getMsg(function(event, type, value){
        if(type == "user_status") {
            self.user_status = value;
	}
    });
{% endcall %}
