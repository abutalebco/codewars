function oddOrEven(array) {
   const total = array.reduce((acc, count) => acc + count, 0)
   if (total % 2 == 0) {
     return "even"
   } else {
     return "odd"
   }
}