var $tournament = $('.tournament'),
    $bracket = $('<ul class="bracket"><li></li><li></li></ul>');

var participants = ['Jeewantha','Chamoda','Adam', 'Matt', 'Evan', 'Abby', 'Heather', 'Christina', 'Ryan', 'Tyler', 'Steve', 'Steph', 'Jenna', 'Derek', 'Mike', 'Sam'];

function buildBracket($el, p1, p2) {
  if(!p1 && !p2) {
    $el.append($bracket.clone());
  }
}

buildBracket($tournament);

var level = 0,
    section = 0,
    $brackets,
    $previousBrackets;

while(level < 4) {
  $brackets = $('.bracket');
  
  $brackets = $brackets.filter(function(i, el) {
    if($previousBrackets) {
      if($.inArray(el, $previousBrackets) >= 0) {
        return false; 
      }
    }
    return true;
  });
  
  if(!$previousBrackets) {
    $previousBrackets = $brackets;
  }
  else {
    $previousBrackets = $.merge($previousBrackets, $brackets);
  }
  
  $brackets.each(function() {
    $(this).find('li:empty').each(function() {
      buildBracket($(this));
    });
  });
  
  level++;
}

function getRivals() {
  var p1i = Math.floor(participants.length * Math.random()),
      p1 = participants[p1i];
  participants.splice(p1i, 1);
  var p2i = Math.floor(participants.length * Math.random()),
      p2 = participants[p2i];
  participants.splice(p2i, 1);
  return [p1, p2];
}

function cleanUp() {
  var $brackets = $('.bracket'),
      removed = false;
  for(var i = 0; i < $brackets.length; i++) {
    // break before there aren't enough spots
    if($('li:empty').length === participants.length) break;
    
    var empty = true;
    $brackets.eq(i).find('li').each(function() {
      if(!$(this).is(':empty')) {
        empty = false;
      }
    });
    if(empty) {
      $brackets.eq(i).remove();
      removed = true;
    }
  }
  return removed;
}

// just do it over and over
while(cleanUp()) { }

var $empty = $('li:empty');
for(var i = 0; i < participants.length; i++) {
  if(i%2===0){
    $empty.eq(i).html('<button style="color:red;border: 2px solid Tomato;">' + participants[i] + '</button>');
  }
  else{
    $empty.eq(i).html('<button style="color:Blue;border: 2px solid DodgerBlue;">' + participants[i] + '</button>');
  }
}

function changeToButtons() {
  $('.bracket').each(function() {
    var $winner = $(this).children('.winner');
    if($winner.length === 0) {
      var $winners = $(this).children('li').children('ul').children('.winner');
      if($winners.length === 2) {
        $winners.each(function() {
          $(this).html('<button class="winner">' + $(this).text() + '</button>');
        });
      }
    }
  });
}

$(document).on('click', 'button', function() {
  var $ul;
  if(!$(this).hasClass('winner')) {
    $ul = $(this).parent().parent();
  }
  else {
    $ul = $(this).parent().parent().parent().parent();
    console.log($ul);
  }
  $ul.append($('<li class="winner">' + $(this).text() + '</li>'));
  $ul.find('button').each(function() {
    $(this).replaceWith($(this).text());
  });
  changeToButtons();
});