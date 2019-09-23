import "./byeie"; // loučíme se s IE
import { text, comments } from "./data";

Object.keys(text).forEach(o => {
  let tmp = `<div id="par_${o}" class="row"><div class="txt">${text[o]}</div>`
  if (o in comments) {
    tmp += `<div class="cmnt">${comments[o]}</div>`
  } else {
    tmp += `<div class="cmnt_empty"></div>`
  }
  document.getElementById("textbx").innerHTML += tmp + `</div>`
})
