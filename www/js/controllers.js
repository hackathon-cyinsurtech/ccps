angular.module('starter.controllers', [])

.controller('DashCtrl', function($scope, $timeout, $ionicPush) {
  $ionicPush.unregister()
    .then(() => {
      $ionicPush.register()
        .then((token) => {
          $ionicPush.saveToken(token);
        })
      });

  $scope.$on('cloud:push:notification', (event, data) => {
    // data.message is of type PushMessage (http://docs.ionic.io/api/client/pushmessage/)
    const { title, text, payload } = data.message;
    alert('Received push notification: ' + title + '\n' + text + '\n' + JSON.stringify(payload));
  });

  $scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
  $scope.series = ['Series A', 'Series B'];
  $scope.data = [
    [65, 59, 80, 81, 56, 55, 40],
    [28, 48, 40, 19, 86, 27, 90]
  ];
  $scope.onClick = function (points, evt) {
    console.log(points, evt);
  };
  
  // Simulate async data update
  $timeout(function () {
    $scope.data = [
      [28, 48, 40, 19, 86, 27, 90],
      [65, 59, 80, 81, 56, 55, 40]
    ];
  }, 1000);
})

.controller('ChatsCtrl', function($scope, Chats) {
  // With the new view caching in Ionic, Controllers are only called
  // when they are recreated or on app start, instead of every page change.
  // To listen for when this page is active (for example, to refresh data),
  // listen for the $ionicView.enter event:
  //
  //$scope.$on('$ionicView.enter', function(e) {
  //});

  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  
});
