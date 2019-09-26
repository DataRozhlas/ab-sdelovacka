import "./byeie"; // loučíme se s IE
import { text, comments } from "./data";

Object.keys(text).forEach(o => {
  let tmp = `<div id="par_${o}" class="row"><div class="txt">${text[o]}</div>`
  if (o in comments) {
    tmp += `<div class="cmnt" id="cmnt_${o}">${comments[o]}</div>`
  } else {
    tmp += `<div class="cmnt_empty"></div>`
  }
  document.getElementById("textbx").innerHTML += tmp + `</div>`
})

let cst= document.getElementsByClassName('cmnt')
Array.from(cst, e => e.addEventListener('click', ev => {
  document.getElementById(ev.target.id).classList.add('exp')
}))