SERVER_URL = 'http://192.168.99.100:8000';

angular.module('starter.services', [])

.factory('Suggestions', function() {
  var data = [{
    id: 1,
    icon: 'img/heart.png',
    title: 'High heart-rate detected!',
    summary: 'Your heart-rate seems to be above the normal range. Wanna try meditating?',
    markup: 'Check out this yoga for beginners <a href="https://www.youtube.com/watch?v=v7AYKMP6rOE">video</a>!'
  }, {
    id: 2,
    icon: 'img/shoe.png',
    title: 'High BMI level detected!',
    summary: 'Your BMI level seems to be higher than the healthy range. Can you power walk?',
    markup: 'Check out this Power Walking 101 <a href="https://www.prevention.com/fitness/power-walking-blast-fat">guide</a>!'
  }];

  return {
    all: function() {
      return data;
    },
    remove: function(suggestion) {
      data.splice(data.indexOf(suggestion), 1);
    },
    get: function(id) {
      for (var i = 0; i < data.length; i++) {
        if (data[i].id === parseInt(id)) {
          return data[i];
        }
      }
      return null;
    }
  };
})
.factory('Chats', function() {
  // Might use a resource here that returns a JSON array

  // Some fake testing data
  var chats = [{
    id: 0,
    name: 'Ben Sparrow',
    lastText: 'You on your way?',
    face: 'img/ben.png'
  }, {
    id: 1,
    name: 'Max Lynx',
    lastText: 'Hey, it\'s me',
    face: 'img/max.png'
  }, {
    id: 2,
    name: 'Adam Bradleyson',
    lastText: 'I should buy a boat',
    face: 'img/adam.jpg'
  }, {
    id: 3,
    name: 'Perry Governor',
    lastText: 'Look at my mukluks!',
    face: 'img/perry.png'
  }, {
    id: 4,
    name: 'Mike Harrington',
    lastText: 'This is wicked good ice cream.',
    face: 'img/mike.png'
  }];

  return {
    all: function() {
      return chats;
    },
    remove: function(chat) {
      chats.splice(chats.indexOf(chat), 1);
    },
    get: function(chatId) {
      for (var i = 0; i < chats.length; i++) {
        if (chats[i].id === parseInt(chatId)) {
          return chats[i];
        }
      }
      return null;
    }
  };
});
