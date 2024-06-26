//Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

function descendingOrder(n){
  return parseInt(String(n).split('').sort().reverse().join(''))
}


//Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
//For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

function sumTwoSmallestNumbers(numbers) {  
  //Code here
  let newArr = numbers.sort((a, b) => a - b)
  return newArr[0] + newArr[1]
}


//Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
//The output should be two capital letters with a dot separating them.
//It should look like this:
//Sam Harris => S.H
//patrick feeney => P.

function abbrevName(name){
  let [fname, lname] = name.toUpperCase().split(" ")
  return `${fname[0]}.${lname[0]}`
}


// 3/20 lvl 6
//Given a string of words, you need to find the highest scoring word.
//Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
//For example, the score of abad is 8 (1 + 2 + 1 + 4).
//You need to return the highest scoring word as a string.
//If two words score the same, return the word that appears earliest in the original string.
//All letters will be lowercase and all inputs will be valid.

function high(x){
  let alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
  ];

  
  let words = x.split(" ");
  let highestScore = 0;
  let highestScoreWord = "";
  
  for (let word of words) {
    let lettersSum = 0;
    
    for (let letter of word) {
      lettersSum += alphabets.indexOf(letter) + 1;
    }
    
    if (lettersSum > highestScore) {
      highestScore = lettersSum;
      highestScoreWord = word;
    }
  }
  
  return highestScoreWord;
}


// 3.21
// Write Number in Expanded Form
// You will be given a number and you will need to return it as a string in Expanded Form. For example:
// expandedForm(12); // Should return '10 + 2'
// expandedForm(42); // Should return '40 + 2'
// expandedForm(70304); // Should return '70000 + 300 + 4'

const expandedForm = n => n.toString()
                            .split("")
                            .reverse()
                            .map( (a, i) => a * Math.pow(10, i))
                            .filter(a => a > 0)
                            .reverse()
                            .join(" + ");



// In this kata you are required to, given a string, replace every letter with its position in the alphabet.

// If anything in the text isn't a letter, ignore it and don't return it.

// "a" = 1, "b" = 2, etc.

// Example
// alphabetPosition("The sunset sets at twelve o' clock.")
// Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )



function alphabetPosition(text) {
  var result = "";
  for (var i = 0; i < text.length; i++){
    var code = text.toUpperCase().charCodeAt(i)
    if (code > 64 && code < 91) result += (code - 64) + " ";
  }

  return result.slice(0, result.length-1);
}

// 3.22 8
// Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).
// Examples
// n = 0  ==> [1]        # [2^0]
// n = 1  ==> [1, 2]     # [2^0, 2^1]
// n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]

function powersOfTwo(n){
  let totals = [];
  for (let i = 0; i <=n; i++){
    totals.push(2 ** i)
  }
  return totals
}

// 3.25
// Two Sum
// Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two different items in the array that, when added together, give the target value. The indices of these items should then be returned in a tuple / list (depending on your language) like so: (index1, index2).
// For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
// The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers; target will always be the sum of two different items from that array).
// Based on: https://leetcode.com/problems/two-sum/


function twoSum(numbers, target) {
  let targetedNumbers = []
    for (let i = 0; i < numbers.length; i++){
      for(let j = i+ 1; j < numbers.length; j++){
            if(numbers[i] + numbers[j] === target){
              return [i, j]
            }
          }
        }
}




// 3.26 8
// Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
// Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

function lovefunc(flower1, flower2){
  // moment of truth
  return (((flower1 % 2 === 0)&& (flower2 % 2 === 1)) ||((flower1 % 2 === 1)&& (flower2 % 2 === 0)))
}

function lovefunc(flower1, flower2){
  return flower1 % 2 !== flower2 % 2;
}


// 3.27 8
// Debugging sayHello function
// The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
// Example output:
// Hello, Mr. Spock

function sayHello(name) {
  return `Hello, ${name}` 
}

// 3.28 8
// Our football team has finished the championship.
// Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.
// For example: ["3:1", "2:2", "0:1", ...]
// Points are awarded for each match as follows:
// if x > y: 3 points (win)
// if x < y: 0 points (loss)
// if x = y: 1 point (tie)
// We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

function points(games) {
  let score = 0
  games.map(game =>{
        if (game[0] > game[2]) {
      score += 3
    } else if (game[0] === game[2]){
      score += 1
    }
  })  
  return score
}


// 3.29 level 6
// The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
// What if the string is empty? Then the result should be empty object literal, {}.

function count (string) {  
  var count = {};
  string.split('').forEach((s) => {
     count[s] ? count[s]++ : count[s] = 1;
  });
  return count;
}


// 4.1 level 7
// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false


function XO(str) {
    //code here
  let x = 0;
  let o = 0;
  for(let i = 0; i<str.length; i++){
    if(str[i].toLowerCase() === "x") {
      x++
    } else if (str[i].toLowerCase() === "o"){
      o++
    }
  }
  return x === o
}


// 4.2 level 6
// Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
// For example (Input --> Output):
// 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
// 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
// 4 --> 0 (because 4 is already a one-digit number)

function persistence(num) {
   //code me
  let output = 0
  num = num.toString();
  while (num.length > 1){
    output++;
    num = num.split('').map(Number).reduce((a, b) => a * b).toString();
  }
  return output
}

// 4.3 level 6
// Build Tower
// Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
// For example, a tower with 3 floors looks like this:
// [
//   "  *  ",
//   " *** ", 
//   "*****"
// ]
// And a tower with 6 floors looks like this:
// [
//   "     *     ", 
//   "    ***    ", 
//   "   *****   ", 
//   "  *******  ", 
//   " ********* ", 
//   "***********"
// ]

function towerBuilder(nFloors) {
  // build here
  var tower = [];
  for (var i = 0; i < nFloors; i++){
    tower.push(" ".repeat(nFloors - i -1) + "*".repeat((i*2) +1) + " ".repeat(nFloors - i -1));
      
  }
  return tower
}
