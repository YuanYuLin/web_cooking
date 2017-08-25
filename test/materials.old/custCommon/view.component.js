{% import SPICES('angular') as NG %}

{% call NG.JSCONTROLLER(MENU.name, 'custController', ['$scope', 'libCore']) %}

    $scope.action_login = function action_login() {
	    console.log("TEST");
	    libCore.setMsg("user_status", "Login...");
    }

{% endcall %}
