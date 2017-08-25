'use strict';

angular.module('{{menu.name}}.hook', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/hook', {
    templateUrl: 'hook/hook.html',
    controller: 'HookCtrl'
  });
}])

.controller('HookCtrl', [function() {
    var self = this;
}]);
