{% import SPICES('angular') as NG %}

{% call NG.JSMAIN('view1', ['libCore']) %}

    libCore.setMsg("menu_top_obj", {"title":"View1", "list":[{"title":"V1-1", "click_parm":'fn_v1_1'},{"title":"V1-2", "click_parm":'fn_v1_2'}]});

    self.Name = "BA BA BA";

{% endcall %}
