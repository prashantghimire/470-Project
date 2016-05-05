angular.module('expressmusic',['ui.router'])

    .config(function($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise("/app");
        $stateProvider
            .state('app',{
                url: '/app',
                templateUrl: 'home',
                controller: 'HomeCtrl',
            })
            .state('suggestions',{
                url: '/suggestions',
                templateUrl: 'suggestions',
                controller: 'HomeCtrl',
            })
            .state('more',{
                url: '/more/:id',
                templateUrl: 'more',
                controller: 'MoreCtrl'
            })
    })
    .controller('HomeCtrl', function($scope, $http){
        
        $scope.run = function (index) {
            $scope.choiceArray[index] = !$scope.choiceArray[index];
        }
        $http.get('results').then(function(res){
            $scope.clusters = res.data.artist;
            $scope.songs = res.data.songs;
        });
    })
    .controller('MoreCtrl', function($scope, $stateParams, $http){
        $http.get('results').then(function(res){
            var similars = res.data.artist[Number($stateParams.id)];
            similars = similars.splice(1, similars.length);
            $scope.similarArtists = similars;
            var newSongs = res.data.songs[Number($stateParams.id)];
            newSongs = newSongs.splice(1, newSongs.length);
            $scope.songs = newSongs;
        });
    })
    .controller('CheckCtrl', ['$scope', function($scope) {
        $scope.choiceArray = [false,false,false,false,false,false,false,false,false,false];
    }])