angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, $timeout, $ionicPush) {
  $ionicPush.unregister()
    .then(() => {
      $ionicPush.register()
        .then((token) => {
          $ionicPush.saveToken(token)
            .then((token) => {
              localStorage.setItem('pushtoken', JSON.stringify(token));
            });
        })
      });

  $scope.$on('cloud:push:notification', (event, data) => {
    // data.message is of type PushMessage (http://docs.ionic.io/api/client/pushmessage/)
    const { title, text, payload } = data.message;
    alert('Received push notification: ' + title + '\n' + text + '\n' + JSON.stringify(payload));
  });

  // Steps
  $scope.steps = {
    labels: ['Μέχρι τώρα', 'Απομένουν'],
    data: [30, 70],
    colors: ['#86adc2', '#d3d3d3'],
    options: {
      legend: {
        display: true
      }
    }
  };

  // Heart-rate
  $scope.hr = {
    labels: ['Δευτέρα', 'Τρίτη', 'Τετάρτη', 'Πέμπτη', 'Παρασκευή', 'Σάββατο', 'Κυριακή'],
    data: [
      [110, 115, 120, 95, 130, 122, 118],
      [100, 100, 100, 100, 100, 100, 100],
      [120, 120, 120, 120, 120, 120, 120],
    ],
    series: ['Actual', 'Recommended Low', 'Recommended High'],
    options: {
      showLines: true
    }
  };

  // BMI
  $scope.bmi = {
    labels: ['Αύγουστος', 'Σεπτέμβρης', 'Οκτώβρης', 'Νοέμβρης', 'Δεκέμβρης', 'Γενάρης'],
    series: ['Actual'],
    data: [30, 29, 27, 27, 25, 24],
    colors: ['#f12d3a', '#faa54a', '#faa54a', '#faa54a', '#faa54a', '#3bb4af'],
    options: {
      scales: {
        xAxes: [{
          display: true,
          ticks: {
              min: 10,
              max: 40
          }
      }]
    }
    }
  };
}) // 12 - 40

.controller('ChatsCtrl', function($scope, Suggestions) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.suggestions = Suggestions.all();
  $scope.remove = function(suggestion) {
    Suggestions.remove(suggestion);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Suggestions) {
  $scope.suggestion = Suggestions.get($stateParams.id);
})

.controller('AccountCtrl', function($scope) {
  $scope.pushtoken = JSON.parse(localStorage.getItem('pushtoken'));
});
