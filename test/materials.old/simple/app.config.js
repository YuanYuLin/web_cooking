'use strict';

angular.module('{{menu.name}}', [
  'ngRoute',
  {% for obj in menu.node_root %} {% if loop.last %}
    '{{obj.name}}'
  {% else %}
    '{{obj.name}}',
  {% endif %} {% endfor %}
]);

angular.module('{{menu.name}}').
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
	  $locationProvider.hashPrefix('!');


	    $routeProvider
                {% for obj in menu.node_root %}
	        .when('/{{obj.name}}', { template: '<{{obj.name}}></{{obj.name}}>'})
                {% endfor %}
                {% for obj in menu.node_root if obj.index %}
	        .otherwise('/{{obj.name}}');
		{% endfor %}

}]);

