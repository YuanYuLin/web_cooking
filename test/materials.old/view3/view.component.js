{% import SPICES('angular') as NG %}
{% call NG.JSMAIN('view3', ['libCore']) %}

    libCore.setMsg("menu_top_obj", {"title":"View3", "list":[{"title":"V3-1"},{"title":"V3-2"}]});
    self.Name = "AAAAA";
    self.click = function click() {

        {% if MENU['name'] == "common" %}
        self.Name="TestCommon";
        {% endif %}

        {% if MENU['name'] == "fubon" %}
        self.Name="BBBBB";
        {% endif %}
    }

{% endcall %}
