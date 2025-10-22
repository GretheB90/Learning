// Pick a random number between 1 and 10:

let secretNumber = Math.floor(Math.random() * 10) + 1;
//Math.random() = gives a random number like 0.52, 0.93, etc
//* 10          = makes it go from 0 to 9.99
//Math.floor()  = rounds it down to a whole number (0 to 9)
//+ 1 → makes it 1 to 10

// Ask the user for a guess:
//let guess = prompt("Guess a number between 1 and 10:");
let guess;

// Keep looping until the guess is correct:
while (guess != secretNumber) {
    //Ask the user for a guess
    guess = prompt("Guess a number between 1 and 10:");

    //Convert guess to a number (because prompt gives us text):
    guess = Number(guess);


    // Check the guess:
    if (guess == secretNumber) {
        alert("You got it! The number was " + secretNumber);
    } else if (guess < secretNumber) {
        alert("Too low, try again.");
    } else {
        alert("Too high! Try again.");
    }
}

//How to play:
// 1. Open your browser
// 2. Right click -> Inspect -> Console tab
// 3. Copy and paste the code in
// 4. Press Enter. A prompt box will show up. Put your guess in it and press Enter.
