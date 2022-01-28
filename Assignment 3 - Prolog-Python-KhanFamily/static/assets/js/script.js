var sendForm = document.querySelector('#chatform'),
  textInput = document.querySelector('.chatbox'),
  chatList = document.querySelector('.chatlist'),
  userBubble = document.querySelectorAll('.userInput'),
  botBubble = document.querySelectorAll('.bot__output'),
  animateBotBubble = document.querySelectorAll('.bot__input--animation'),
  overview = document.querySelector('.chatbot__overview'),
  hasCorrectInput,
  imgLoader = false,
  animationCounter = 1,
  animationBubbleDelay = 600,
  input,
  names,
  previousInput,
  isReaction = false,
  unkwnCommReaction = "I didn't quite get that.",
  chatbotButton = document.querySelector(".submit-button")





var server = "http://127.0.0.1:5000";
// var op_num = {'sum':[3,4]};
// function update_var()
// {
//   var n1 = parseFloat($("#n1").val());
//   var n2 = parseFloat($("#n2").val());
//   op_num['sum']=[n1,n2];
// }
function sendUserInfo() {

  var userInfo = textInput.value

  var appdir = '/processUserInfo';
  // var send_msg = "<p>Sending numbers</p>";
  // var received_msg = "<p>Result returned</p>";
  // update_var();
  // console.log(send_msg);
  // $('#message').html(send_msg);
  $.ajax({
    type: "POST",
    url: server + appdir,
    data: JSON.stringify(userInfo),
    dataType: 'json'
  }).done(function (data) {
    console.log(data);
    names = data['sum'];

  });

}









sendForm.onkeydown = function (e) {
  if (e.keyCode == 13) {
    e.preventDefault();

    //No mix ups with upper and lowercases
    var input = textInput.value.toLowerCase();

    //Empty textarea fix
    if (input.length > 0) {
      createBubble(input)
    }
  }
};



sendForm.addEventListener('submit', function (e) {
  //so form doesnt submit page (no page refresh)
  e.preventDefault();

  //No mix ups with upper and lowercases
  var input = textInput.value.toLowerCase();

  //Empty textarea fix
  if (input.length > 0) {
    createBubble(input)
  }
}) //end of eventlistener



var createBubble = function (input) {
  //create input bubble
  var chatBubble = document.createElement('li');
  chatBubble.classList.add('userInput');

  //adds input of textarea to chatbubble list item
  chatBubble.innerHTML = input;

  //adds chatBubble to chatlist
  chatList.appendChild(chatBubble)

  checkInput(input);
}

var checkInput = function (input) {
  hasCorrectInput = false;
  isReaction = false;
  //Checks all text values in possibleInput
  for (var textVal in possibleInput) {
    //If user reacts with "yes" and the previous input was in textVal
    // if (input == "yes" || input.indexOf("yes") >= 0) {
    //   if (previousInput == textVal) {
    //     console.log("sausigheid");

    //     isReaction = true;
    //     hasCorrectInput = true;
    //     botResponse(textVal);
    //     break
    //   }

    // }
    // if (input == "no" && previousInput == textVal) {
    //   unkwnCommReaction = "For a list of commands type: Commands";
    //   unknownCommand("I'm sorry to hear that :(")
    //   unknownCommand(unkwnCommReaction);
    //   hasCorrectInput = true;
    //   break
    // }
    //Is a word of the input also in possibleInput object?
    if (input == textVal) {
      console.log("succes");
      hasCorrectInput = true;
      botResponse(textVal);
      break
    }

  }
  //When input is not in possibleInput
  if (hasCorrectInput == false) {
    console.log("failed");
    unknownCommand(unkwnCommReaction);
    hasCorrectInput = true;
  }
}

// debugger;

function botResponse(textVal) {
  //sets previous input to that what was called
  // previousInput = input;

  //create response bubble
  var userBubble = document.createElement('li');
  userBubble.classList.add('bot__output');

  if (isReaction == true) {
    if (typeof reactionInput[textVal] === "function") {
      //adds input of textarea to chatbubble list item
      userBubble.innerHTML = reactionInput[textVal]();
    } else {
      userBubble.innerHTML = reactionInput[textVal];
    }
  }

  if (isReaction == false) {
    //Is the command a function?
    if (typeof possibleInput[textVal] === "function") {
      // console.log(possibleInput[textVal] +" is a function");
      //adds input of textarea to chatbubble list item
      userBubble.innerHTML = possibleInput[textVal]();
    } else {
      userBubble.innerHTML = possibleInput[textVal];
    }
  }
  //add list item to chatlist
  chatList.appendChild(userBubble) //adds chatBubble to chatlist
  // function sendUserInfo() {
  // let userInfo ={
  //   var str= textInput.toString();
  //   'name': str

  //   // 'type': 'Admin',
  // }
  // var num = 15;


  // var userInfo = textInput.value.toString();
  // const request = new XMLHttpRequest()
  // request.open('POST', `/processUserInfo/${JSON.stringify(userInfo)}`)
  // request.onload = () => {
  //   const flaskMessage = request.responseText
  //   console.log(flaskMessage)
  // }
  // request.send()


  // }

  // reset text area input
  textInput.value = "";
}

function unknownCommand(unkwnCommReaction) {
  // animationCounter = 1;

  //create response bubble
  var failedResponse = document.createElement('li');

  failedResponse.classList.add('bot__output');
  failedResponse.classList.add('bot__output--failed');

  //Add text to failedResponse
  failedResponse.innerHTML = unkwnCommReaction; //adds input of textarea to chatbubble list item

  //add list item to chatlist
  chatList.appendChild(failedResponse) //adds chatBubble to chatlist

  animateBotOutput();

  // reset text area input
  // textInput.value = "";

  //Sets chatlist scroll to bottom
  chatList.scrollTop = chatList.scrollHeight;

  animationCounter = 1;
}

function responseText(e) {

  var response = document.createElement('li');

  response.classList.add('bot__output');

  //Adds whatever is given to responseText() to response bubble
  response.innerHTML = e;

  chatList.appendChild(response);

  animateBotOutput();

  console.log(response.clientHeight);

  //Sets chatlist scroll to bottom
  setTimeout(function () {
    chatList.scrollTop = chatList.scrollHeight;
    console.log(response.clientHeight);
  }, 0)
}

function responseImg(e) {
  var image = new Image();

  image.classList.add('bot__output');
  //Custom class for styling
  image.classList.add('bot__outputImage');
  //Gets the image
  image.src = "/images/" + e;
  chatList.appendChild(image);

  animateBotOutput()
  if (image.completed) {
    chatList.scrollTop = chatList.scrollTop + image.scrollHeight;
  }
  else {
    image.addEventListener('load', function () {
      chatList.scrollTop = chatList.scrollTop + image.scrollHeight;
    })
  }
}

//change to SCSS loop
function animateBotOutput() {
  chatList.lastElementChild.style.animationDelay = (animationCounter * animationBubbleDelay) + "ms";
  animationCounter++;
  chatList.lastElementChild.style.animationPlayState = "running";
}

function commandReset(e) {
  animationCounter = 1;
  // previousInput = Object.keys(possibleInput)[e];

}

var possibleInput = {
  "1": function () {
    responseText("Enter name of person whose Baap is required :");
    commandReset(2);
    return
  },
  "2": function () {
    responseText("Enter name of person whose Maa is required :");
    commandReset(2);
    return
  },
  "3": function () {
    responseText("Enter name of person whose Beti is required :");
    commandReset(2);
    return
  },
  "4": function () {
    responseText("Enter name of person whose Beta is required :");
    commandReset(2);
    return
  },

  '5': function () {
    responseText("Enter name of person whose Dada is required :");
    commandReset(2);
    return
  },

  '6': function () {
    responseText("Enter name of person whose Nana is required :");
    commandReset(2);
    return
  },

  '7': function () {
    responseText("Enter name of person whose Dadi is required :");
    commandReset(2);
    return
  },
  '8': function () {
    responseText("Enter name of person whose Nani is required :");
    commandReset(2);
    return
  },
  '9': function () {
    responseText("Enter name of person whose Sala is required :");
    commandReset(2);
    return
  },

  'a': function () {
    responseText("Enter name of person whose Bahu is required :");
    commandReset(2);
    return
  },

  'b': function () {
    responseText("Enter name of person whose Pota is required :");
    commandReset(2);
    return
  },

  'c': function () {
    responseText("Enter name of person whose Poti is required :");
    commandReset(2);
    return
  },

  'd': function () {
    responseText("Enter name of person whose Nawasa is required :");
    commandReset(2);
    return
  },

  'e': function () {
    responseText("Enter name of person whose Nawasi is required :");
    commandReset(2);
    return
  },


  'f': function () {
    responseText("Enter name of person whose susar is required :");
    commandReset(2);
    return
  },

  'g': function () {
    responseText("Enter name of person whose susar is required :");
    commandReset(2);
    return
  },

  'h': function () {
    responseText("Enter name of person whose Baapdada is required :");
    commandReset(2);
    return
  },

  'i': function () {
    responseText("Enter name of person whose Khala is required :");
    commandReset(2);
    return
  },

  'j': function () {
    responseText("Enter name of person whose Chachataya is required :");
    commandReset(2);
    return
  },



  "rabia": function () {

    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "chotekhan": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },

  "chotirani": function () {
    commandReset(2);
    return
  },
  "barrekhan": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "barrirani": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "salim": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "kausar": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "nadir": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "asad": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "nahid": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "sumra": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "rizwan": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "burhan": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "rashid": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "akram": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "salima": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  },
  "sanam": function () {
    if (names != '') {
      responseText(names);
    }
    else {
      responseText('No Relations Found');
    }
    commandReset(2);
    return
  }

}