//  Remove n exclamation marks in the sentence from left to right. n is positive integer.
// Examples

// remove("Hi!",1) === "Hi"
// remove("Hi!",100) === "Hi"
// remove("Hi!!!",1) === "Hi!!"
// remove("Hi!!!",100) === "Hi"
// remove("!Hi",1) === "Hi"
// remove("!Hi!",1) === "Hi!"
// remove("!Hi!",100) === "Hi"
// remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
// remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
// remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
// remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"


function remove(s,n){
  let count = n
  let arr = s.split("")
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "!") {
      if (count !== 0) {
        arr.splice(i, 1); 
        count--;
        i--;  
      }
    }
  }
  return arr.join("")
  
}
