//TASK-E
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// const chappa=[5,3,8,1,0, 'room', 'door','bath ']

// chappa.reverse();

// console.log("after chappa:",chappa);

function getReverse(a) {
  const turn = a.split("").reverse().join(""); //split orqali arrayga aylantiramiz,
  //reverse orqali arrayni teskari ogirib,
  //join orqali yana string ga aylantirib .

  console.log(turn);
}

checkContent("hello");
