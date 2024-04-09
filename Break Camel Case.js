// Complete the solution so that the function will break up camel casing, using a space between words.

// Example
// "camelCasing"  =>  "camel Casing"
// "identifier"   =>  "identifier"
// ""             =>  ""

function solution(string) {
  return string === "" ?  string : string.replace(/([a-z])([A-Z])/g, '$1 $2');
}
