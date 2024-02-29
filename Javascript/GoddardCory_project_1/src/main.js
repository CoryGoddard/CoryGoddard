
// waits until page is loaded to create the keyboard
document.addEventListener('readystatechange', () => {    
    if (document.readyState == 'complete') createKeyboard();
});
 
// list of possible words
words = [
    "beach", "shell", "seagull", "coral", "whale",
    "dolphin", "jellyfish", "starfish", "shark", "oyster", "lagoon",
    "island", "sailboat", "octopus", "lighthouse", "seashore", "turtle",
    "pelican", "seascape", "marlin", "tropical", "flippers", "mermaid", "plankton", "surfboard",
    "coast", "anchor", "harbor", "shipwreck", "seaweed", "shoreline", "underwater", "cruise",
    "tidal", "fishing", "sandcastle", "current","fathom","fjord",
    "gondola", "narwhal", "sunset", "beacon", "sailfish", "seabird", "oceanography", "harpoon",
    "flounder", "barracuda", "lobster", "mariner", "atoll", "shorebird", "trident", "buoyancy",
    "maritime", "inlet", "tideland", "shipmate", "siren", "manatee", "tidewater", "monsoon", "wharf", 
    "waterfront", "pelagic", "anemone", "archipelago", "cetacean", "seagreen", "seasalt", "whirlpool", "tidepool", 
    "seafloor", "shipyard", "seafood", "salty", "tidalwave", "deepblue", "oceanic", "aquatic", 
    "nautical", "porthole", "atmosphere", "seashell", "shipshape", 
    "seaworthy", "splash", "submarine", "sunny", "vessel", "voyage", "wading",
    "windsurf", "wreck", "yacht", "zooplankton", "seabreeze", "goggles", "sandbar", "islet", "latitude",
    "longitude", "outflow", "pilings", "rigging", "sailing", 
    "seafaring", "shanty", "shore", "sound", "starboard",
    "tiller", "undertow", "water"
];

// generates a random number that fits within the index range (length) of the words list
chosenIndex = Math.floor(Math.random()*words.length)
// grabs the chosen word and splits into an array
chosenWord = words[chosenIndex];
word = chosenWord.split("");

// makes progress into an array of the same length as the word, but as -'s
progress = chosenWord.split("");
for (let i = 0; i < progress.length;i++) {
    progress[i] = "-";
}

// number of guesses so far
guesses = 0;
// index of previous messages
prevMessage = 0;
// arrays with correct/incorrect messages
incorrectMessages = ["Try something else.", "Incorrect.", "That doesn't work.", "Not quite there.", "Keep trying."];
correctMessages = ["Great job!", "Keep it up!", "Excellent!", "Well done!", "Keep it going!"];

// variables for sharkie, fishie, and their position's, as they are used alot
let shark = document.getElementById("sharkie");
let fish = document.getElementById("fishie");
let sharkPos = getPositionAtCenter(shark);
let fishPos = getPositionAtCenter(fish);

// determines the amount of different letters in the word
count = 0;
for (let i = 0; i < word.length;i++) {
    if (!(word[i] in word.slice(0,i))) {
        count += 1;
    }
}

// determines the minimum guess count, max guess count, and distance that sharkie should move for each guess
minGuesses = count;
maxGuesses = count + 6;
const distance = (fishPos.x - sharkPos.x) / (count + 8);

// function to build the keyboard
function createKeyboard() {
    let keyboard = document.getElementById("keyboard");
    let htmlCode = "";
    let row1 = ["Q","W","E","R","T","Y","U","I","O","P"];
    let row2 = ["A","S","D","F","G","H","J","K","L"];
    let row3 = ["Z","X","C","V","B","N","M"];

    // adds each button on row 1 to the keyboard
    htmlCode += "<div class=\"row1\">"
    for (let index = 0; index <= 9;index++) {
        let curr = "btn" + row1[index];
        htmlCode += "<input id=\"" + curr + "\" class=\"row1Key\" value = \"" + row1[index] + "\" type=\"button\" onclick=\"input(this);\" />";
    }
    htmlCode += "</div></br>"

    // adds each button on row 2 to the keyboard
    htmlCode += "<div class=\"row2\">"
    for (let index = 0; index <= 8;index++) {
        let curr = "btn" + row2[index];
        htmlCode += "<input id=\"" + curr + "\" class=\"row2Key\" value = \"" + row2[index] + "\" type=\"button\" onclick=\"input(this);\" />";
    }
    htmlCode += "</div></br>"

    // adds each button on row 3 to the keyboard
    htmlCode += "<div class=\"row3\">"
    for (let index = 0; index <= 6;index++) {
        let curr = "btn" + row3[index];
        htmlCode += "<input id=\"" + curr + "\" class=\"row3Key\" value = \"" + row3[index] + "\" type=\"button\" onclick=\"input(this);\" />";
    }

    // adds the reset button to the keyboard
    htmlCode += "<button onclick=\"window.location.reload()\"class=\"resetButton\" id=\"resetButton\">Reset</button></div></br>"
    
    // adds keyboard to the page
    keyboard.innerHTML = htmlCode

    // makes the progress pop up for the first time, and passes a starting message
    updateDisplay("Make a Guess!")
}

// function used by each keyboard key to make a guess
function input(element) {
    // gets the value of the pressed key
    let key = element.value;

    // determines if the guessed letter is in the word
    let isCorrect = false;
    if (word.includes(key.toLowerCase())) {
        isCorrect = true;
        for (index in word) {
            if (word[index] == key.toLowerCase()) {
                progress[index] = key;
            }
        }
    }
    // disables the guessed key
    element.disabled = true;

    // moves the shark to the right by the determined distance
    let left = document.getElementById("left");
    currLeft = left.style.width;
    currLeft = parseFloat(currLeft);
    newLeft = currLeft + distance;
    left.style.width = newLeft + "px";
    // changes shark image once the number of guesses has reached the minimum amount of guesses
    if (count == 0) {
        let sharkImg = document.getElementById("sharkie");
        sharkImg.src = "images/sharkOpen.png"
    }
    // decrements count to determine when the shark's mouth should open
    count -= 1;

    // increment the guess count by 1
    guesses += 1;
    // update the display, passes boolean to display an incorrect or correct message
    updateDisplay(isCorrect);
}

// function to update the state of the word and the number of guesses, then display a message
function updateDisplay(isCorrect) {
    // grab all changing text fields
    let wordField = document.getElementById("word");
    let guessesField = document.getElementById("guesses");
    let messagesField = document.getElementById("messages");

    // displays the guessed characters so far
    chars = "";
    for (char in progress) {
        chars += progress[char];
    }
    wordField.innerHTML = chars;

    // displays the new number of guesses
    guessesField.innerHTML = "GUESSES:" + guesses;

    // displays a message depending on isCorrect:
    /// if true: display a correct message
    /// if false: display incorrect message
    /// else: isCorrect is the message that needs displayed(only used at the beginning, but could be useful)
    let message = "";
    let index = 0;
    if (isCorrect === true) {
        index = Math.floor(Math.random() * 5);
        // if the message is the same index as the previous message, display the next possible message
        if (index == prevMessage) {
            index += 1;
        }
        if (index > 4) {
            index = 0;
        }
        message = correctMessages[index];
        prevMessage = index;
    } else if (isCorrect === false) {
        index = Math.floor(Math.random() * 5);
        // if the message is the same index as the previous message, display the next possible message
        if (index == prevMessage) {
            index += 1;
        }
        if (index > 4) {
            index = 0;
        }
        message = incorrectMessages[index];
        prevMessage = index;
    } else {
        message = isCorrect;
    }
    
    // display the message
    messagesField.innerHTML = message;

    // determine if the game is done (word is complete, or guess limit is hit),
    // if it is, pass to the finishGame function 
    if (!(progress.includes('-'))) {
        finishGame(messagesField, true);
    } else if (guesses >= maxGuesses) {
        finishGame(messagesField, false);
    }
}

// function to finish the game(disable keyboard, display finish message, ...)
function finishGame(messagesField, won) {
    // disables the keyboard
    let keyboard = document.getElementById("keyboard");
    let keys = keyboard.getElementsByTagName("input");
    for (keyIndex in keys) {
        keys[keyIndex].disabled = true;
    }

    // used to change the word's color depending on if the user got it
    let wordHighlight = document.getElementById("word");
    if (won) {
        // turns the shark around
        let sharkImg = document.getElementById("sharkie");
        sharkImg.src = "images/sharkFlipped.png";
        wordHighlight.style.color = "green";

        // displays a win message depending on how many guesses it took
        if (guesses <= minGuesses) {
            // makes sharkie cry if the number of guesses is the minimum
            sharkImg.src = "images/sharkCry.png"
            messagesField.innerHTML = "Great Guessing! You Won!";
        } else if (guesses <= (minGuesses + 2)) {
            messagesField.innerHTML = "You got there! Good job!";
        } else if (guesses <= (minGuesses + 5)) {
            messagesField.innerHTML = "Cutting it close, but you got there!";
        } else {
            messagesField.innerHTML = "You barely saved the fish.";
        }
    } else {
        // displays entire word to show user what the word was, makes it red
        finishWord();
        wordHighlight.style.color = "red";

        // moves the shark one last time to cover the fish
        // (before this, the shark would get too close and would still cover the fish on a win)
        let left = document.getElementById("left");
        currLeft = left.style.width;
        currLeft = parseFloat(currLeft);
        newLeft = currLeft + distance;
        left.style.width = newLeft + "px";

        // changes shark to closed mouth image, showing he ate the fish
        let sharkImg = document.getElementById("sharkie");
        sharkImg.src = "images/shark.png";

        // displays losing message
        messagesField.innerHTML = "The shark got a meal! You lose.";
    }
}

// gets the x and y coordinates of the center of an image
// used to determine the distance sharkie needs to move after each guess
function getPositionAtCenter(element) {
    const {top, left, width, height} = element.getBoundingClientRect();
    return {
        x: left + width / 2,
        y: top + height / 2
      };
}

// finishes the entire word, used when the user loses the game
function finishWord() {
    for (let i = 0;i < progress.length; i++) {
        progress[i] = word[i].toUpperCase();
    }
    updateDisplay(false);
}