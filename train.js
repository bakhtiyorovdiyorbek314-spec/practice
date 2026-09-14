//TASK-G
// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.
function getHighestIndex(list) {
  let max = list[0];

  for (i = 0; i < list.length; i++) {
    if (list[i] > max) {
      max = list[i];
    }
  }
  let index = list.indexOf(max);
  return index;
}

result = getHighestIndex([5, 21, 12, 21, 8]);
console.log(result);

//TASK F
// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function findDoublers(a) {
//   const nechta = {};

//   for (i = 0; i < a.length; i++) {
//     const letter = a[i];
//     if (nechta[letter]) {
//       //oldin uchragan bolsa
//       return true;
//     }
//     nechta[letter] = true; //korilgani
//   }
//   return false;
// }
// bormi = findDoublers("hello");
// console.log("bormi:", bormi);

// bormi = findDoublers("fruit");
// console.log("bormi:", bormi);

//TASK-E
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// const chappa=[5,3,8,1,0, 'room', 'door','bath ']

// chappa.reverse();

// console.log("after chappa:",chappa);

// function getReverse(a) {
//   const turn = a.split("").reverse().join(""); //split orqali arrayga aylantiramiz,
//   //reverse orqali arrayni teskari ogirib,
//   //join orqali yana string ga aylantirib .

//   console.log(turn);
// }

// checkContent("hello");
