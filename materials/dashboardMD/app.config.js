'use strict';

angular.module('{{MENU.name}}', [
  'ngRoute',
  {% for obj in MENU.node_root %} {% if loop.last %}
    '{{obj.name}}'
  {% else %}
    '{{obj.name}}',
  {% endif %} {% endfor %}
]);

angular.module('{{MENU.name}}').
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
	  $locationProvider.hashPrefix('!');


	    $routeProvider
                {% for obj in MENU.node_root %}
	        .when('/{{obj.name}}', { template: '<{{obj.name}}></{{obj.name}}>'})
                {% endfor %}
                {% for obj in MENU.node_root if obj.index %}
	        .otherwise('/{{obj.name}}');
		{% endfor %}

}]);

