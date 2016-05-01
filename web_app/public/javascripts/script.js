angular.module('expressmusic',['ui.router'])

.config(function($stateProvider, $urlRouterProvider) {
	$urlRouterProvider.otherwise("/app");
	$stateProvider
	.state('app',{
		url: '/app',
		templateUrl: 'home',
		controller: 'HomeCtrl'
	})
	.state('more',{
		url: '/more/:id',
		templateUrl: 'more',
		controller: 'MoreCtrl'
	})
})

.controller('HomeCtrl', function($scope, $http){
	$http.get('results').then(function(res){
		$scope.clusters = res.data.artist;
	});
})
.controller('MoreCtrl', function($scope, $stateParams, $http){
	$http.get('results').then(function(res){
		var similars = res.data.artist[Number($stateParams.id)];
		similars = similars.splice(1, similars.length);

		$scope.similarSongs = similars;

	});
})