// Welcome.

// In this kata you are required to, given a string, replace every letter with its position in the alphabet.

// If anything in the text isn't a letter, ignore it and don't return it.

// "a" = 1, "b" = 2, etc.

// Example
// alphabet_position("The sunset sets at twelve o' clock.")
// Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
function alphabetPosition(text) {
    new_text = text.toLowerCase()
    let position = []
    for (i = 0; i < new_text.length; i++){
      if (new_text.charCodeAt(i) -96 >=1 && new_text.charCodeAt(i)-96 <=26){
         position.push(new_text.charCodeAt(i)- 96);
      }
    }
    return position.join(' ')
  }
