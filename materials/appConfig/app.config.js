'use strict';

angular.module('{{MENU.name}}', [
  {% for obj in MATERIALS_PKGS_DEP if obj.type == "component" %} {% if loop.last %}
    '{{obj.name}}'
  {% else %}
    '{{obj.name}}',
  {% endif %} {% endfor %}
]).config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
	  $locationProvider.hashPrefix('!');


	    $routeProvider
                {% for obj in MENU.menu_nodes %}
	        .when('{{obj.arg}}', { template: '<{{obj.name}}></{{obj.name}}>'})
                {% endfor %}
                {% for obj in MENU.menu_nodes if obj.index %}
	        .otherwise('{{obj.arg}}');
		{% endfor %}

}]);

