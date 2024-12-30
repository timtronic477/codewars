// Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined if any of the values aren't numbers.

function cubeOdd(arr) {
  if (!Array.isArray(arr) || arr.some(item => typeof item !== 'number')) {
    return undefined;
  }

  const cubed = arr.map(i => i ** 3);

  let sum = 0;
  for (let i = 0; i < cubed.length; i++) {
    if (Math.abs(cubed[i] % 2) === 1) {
      sum += cubed[i];
    }
  }

  return sum;
}
